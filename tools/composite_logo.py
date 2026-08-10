#!/usr/bin/env python3
"""Compoe o logo correto sobre a marcacao adulterada dos frames de partida.

O PROBLEMA
    A geracao escreveu ruido tipografico no lugar de USE ZERO HORA(R), e o
    proprio "OH" do frame nao e' o monograma da marca — sao duas letras soltas.
    Como as formas velha e nova nao coincidem traco a traco, nao basta pintar
    por cima: sobra tinta velha nas folgas.

COMO
 1. SUPRESSAO da tinta velha por abertura morfologica em escala de cinza, com
    elemento maior que a espessura do traco. Abertura devolve o nivel do fundo
    escuro por baixo seguindo o gradiente de luz. Inpaint nao serve: puxa valor
    dos vizinhos claros e deixa borrao (testado e reprovado, ver
    docs/anti_ai_checklist_log.md).

 2. REPOSICAO DE TEXTURA. Suprimir a tinta apaga junto a malha pontilhada do
    neoprene, e area lisa denuncia o remendo. Injeta-se a alta frequencia de um
    trecho vizinho de tecido, COM CORTE DE OUTLIERS: sem esse corte vem junto
    as gotas d'agua do trecho de origem, carimbando gotas falsas (tambem
    testado e reprovado).

 3. ARTE NOVA re-iluminada. A arte canonica entra so como mascara de onde ha
    relevo. O brilho da tinta nao e' arbitrado: mede-se no proprio frame a
    resposta da tinta velha (quanto ela e' mais clara que o fundo local) e
    aplica-se a mesma resposta a nova. Assim o logo herda a luz do frame —
    contraluz quente em sf_002, mais rasante em sf_001 — em vez de importar a
    luz de estudio da macro.

 4. RELEVO sutil por deslocamento de 1 px na direcao da luz, medida no proprio
    gradiente de fundo da janela.

ESCOPO
    Tudo restrito a mascara do badge / etiqueta. O relatorio traz a
    porcentagem exata de pixels alterados na imagem inteira.
"""
import numpy as np, cv2, json, sys

REGIOES = [
    dict(frame='assets/start_frames/sf_002_setup_a_plano_medio_16x9.png',
         nome='peito', arte='assets/wardrobe/badge_chest_art.png', tipo='disco',
         cx=1523, cy=623, r=44, r_arte=430, se=13, thr=8, tex=(-115, 0)),
    dict(frame='assets/start_frames/sf_002_setup_a_plano_medio_16x9.png',
         nome='coxa', arte='assets/wardrobe/label_thigh_art.png', tipo='caixa',
         cx=1580, cy=1439, hw=58, hh=21, se=11, thr=7, tex=(0, -85)),
    dict(frame='assets/start_frames/sf_001_setup_a_encontro_camera_3x4.png',
         nome='peito', arte='assets/wardrobe/badge_chest_art.png', tipo='disco',
         cx=1058, cy=665, r=41, r_arte=430, se=13, thr=8, tex=(-110, 0)),
    dict(frame='assets/start_frames/sf_001_setup_a_encontro_camera_3x4.png',
         nome='coxa', arte='assets/wardrobe/label_thigh_art.png', tipo='caixa',
         cx=1100, cy=1535, hw=56, hh=20, se=11, thr=7, tex=(0, -80)),
]

P = 120


def escopo(shape, reg, ox, oy):
    h, w = shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    if reg['tipo'] == 'disco':
        return (((xx - ox) ** 2 + (yy - oy) ** 2) <= reg['r'] ** 2).astype(np.float32)
    return ((np.abs(xx - ox) <= reg['hw']) & (np.abs(yy - oy) <= reg['hh'])).astype(np.float32)


def arte_no_frame(reg, shape, ox, oy):
    """Deforma a arte canonica para a geometria medida no frame."""
    a = cv2.imread(reg['arte'], cv2.IMREAD_UNCHANGED)[:, :, 3].astype(np.float32) / 255.0
    h, w = shape
    out = np.zeros((h, w), np.float32)
    if reg['tipo'] == 'disco':
        k = (2.0 * reg['r']) / (2.0 * reg['r_arte'])      # anel da arte -> raio no frame
        M = np.float32([[k, 0, ox - k * (a.shape[1] / 2)],
                        [0, k, oy - k * (a.shape[0] / 2)]])
    else:
        kx = (2.0 * reg['hw']) / a.shape[1]
        ky = (2.0 * reg['hh']) / a.shape[0]
        M = np.float32([[kx, 0, ox - reg['hw']], [0, ky, oy - reg['hh']]])
    cv2.warpAffine(a, M, (w, h), dst=out, flags=cv2.INTER_AREA,
                   borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    return np.clip(out, 0, 1)


def textura_limpa(img, x0, y0, shape, dxdy):
    """Alta frequencia de tecido vizinho, com outliers cortados.

    O corte e' o que impede que gotas d'agua do trecho de origem sejam
    carimbadas dentro do patch.
    """
    dx, dy = dxdy
    sy, sx = y0 + dy, x0 + dx
    src = img[sy:sy + shape[0], sx:sx + shape[1]]
    if src.shape[:2] != shape:
        return None
    d = src.astype(np.float32) - cv2.GaussianBlur(src.astype(np.uint8), (0, 0), 2.0).astype(np.float32)
    s = d.std()
    return np.clip(d, -2.0 * s, 2.0 * s)


def compoe(img, reg):
    x0, y0 = max(0, reg['cx'] - P), max(0, reg['cy'] - P)
    x1, y1 = min(img.shape[1], reg['cx'] + P), min(img.shape[0], reg['cy'] + P)
    win = img[y0:y1, x0:x1].astype(np.float32)
    ox, oy = reg['cx'] - x0, reg['cy'] - y0
    esc = escopo(win.shape[:2], reg, ox, oy)
    esc_s = cv2.GaussianBlur(esc, (0, 0), 1.5)

    w8 = win.round().astype(np.uint8)
    g = cv2.cvtColor(w8, cv2.COLOR_BGR2GRAY).astype(np.float32)
    gf = cv2.cvtColor(cv2.medianBlur(w8, 15), cv2.COLOR_BGR2GRAY).astype(np.float32)

    # 1 — tinta velha
    tinta = ((g - gf) > reg['thr']).astype(np.uint8) * (esc > 0.5).astype(np.uint8)
    tinta = cv2.morphologyEx(tinta, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    tinta_d = cv2.dilate(tinta, np.ones((5, 5), np.uint8)) * (esc > 0.5).astype(np.uint8)

    sel = tinta.astype(bool)
    if sel.sum() < 50:
        return img, None
    # ENERGIA de tinta, nao mediana por pixel. Na escala do frame (~88 px de
    # badge) os tracos novos saem antialiasados com alpha ~0.5, e um ganho por
    # mediana os deixaria com metade do brilho — foi o que aconteceu na
    # primeira versao. Casar a soma do excesso de luminancia reproduz o mesmo
    # peso visual da marcacao original.
    # por CANAL: a tinta da peca e' creme quente, nao neutra. Somar o mesmo
    # ganho em B, G e R sobre fundo escuro quente devolve um cinza — foi o que
    # apareceu na segunda versao. A proporcao entre canais vem medida.
    # calibracao pelo PICO, nao pela energia media. A tinta original tem nucleo
    # claro com borda suave; media e energia sao puxadas para baixo pelos pixels
    # de borda e devolvem metade do contraste (medido: 46 contra 91). O
    # percentil 90 do excesso reproduz o nucleo.
    med = cv2.medianBlur(w8, 15).astype(np.float32)
    ganho_c = np.array([float(np.percentile(np.clip(win[:, :, c] - med[:, :, c], 0, None)[sel], 90))
                        for c in range(3)])

    # 2 — suprime e repoe textura
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (reg['se'], reg['se']))
    aberto = cv2.morphologyEx(w8, cv2.MORPH_OPEN, k).astype(np.float32)
    m_sup = cv2.GaussianBlur(tinta_d.astype(np.float32), (0, 0), 1.0)[:, :, None]
    base = win * (1 - m_sup) + aberto * m_sup
    tex = textura_limpa(img, x0, y0, win.shape[:2], reg['tex'])
    if tex is not None:
        base = base + tex * m_sup
    # NAO se corrige o vies da supressao por deslocamento medido: tentado e
    # reprovado. O anel de tecido "limpo" disponivel dentro do disco fica no
    # lado escuro do gradiente, entao a comparacao devolve sinal invertido e a
    # correcao CLAREIA o disco em vez de escurecer (medido: fundo foi de 61
    # para 86, contra 54 do original). Sem ela o residuo fica em +6.8 niveis.

    # 3 — arte nova, re-iluminada pela resposta medida no frame
    A = arte_no_frame(reg, win.shape[:2], ox, oy) * esc_s
    # 4 — relevo: direcao da luz pelo gradiente do fundo
    gy, gx = np.gradient(cv2.GaussianBlur(gf, (0, 0), 6.0))
    ux, uy = float(gx.mean()), float(gy.mean())
    n = max(1e-6, np.hypot(ux, uy))
    ux, uy = ux / n, uy / n
    M1 = np.float32([[1, 0, ux], [0, 1, uy]])
    M2 = np.float32([[1, 0, -ux], [0, 1, -uy]])
    luz = cv2.warpAffine(A, M1, (A.shape[1], A.shape[0]))
    som = cv2.warpAffine(A, M2, (A.shape[1], A.shape[0]))
    # amplitude baixa de proposito: com o ganho calibrado no pico (~145),
    # fatores de 0.35 viravam halos de ~50 niveis em volta de cada traco,
    # lidos como veu sobre o disco.
    relevo = np.clip(luz - A, 0, 1) * 0.10 - np.clip(som - A, 0, 1) * 0.08

    add = (A[:, :, None] + relevo[:, :, None]) * ganho_c[None, None, :]
    out = np.clip(base + add, 0, 255)

    img[y0:y1, x0:x1] = out
    return img, dict(ganho_bgr=[round(float(v), 1) for v in ganho_c],
                     px_tinta_velha=int(sel.sum()),
                     px_arte_nova=int((A > 0.5).sum()),
                     luz=[round(ux, 2), round(uy, 2)])


def main():
    S = '/tmp/claude-0/-home-user-neoprene-campaign/2a358ccf-002b-5c2c-9538-4f719f033e34/scratchpad/'
    por = {}
    for r in REGIOES:
        por.setdefault(r['frame'], []).append(r)
    rel = []
    for frame, regs in por.items():
        src = cv2.imread(frame, cv2.IMREAD_UNCHANGED)
        img0 = src[:, :, :3].astype(np.float32)
        cur = img0.copy()
        det = []
        for reg in regs:
            cur, info = compoe(cur, reg)
            det.append(dict(nome=reg['nome'], **(info or {})))
        out = cur.round().astype(np.uint8)
        if src.shape[2] == 4:
            out = np.dstack([out, src[:, :, 3]])
        cv2.imwrite(frame, out, [cv2.IMWRITE_PNG_COMPRESSION, 6])
        d = np.abs(cur - img0).max(axis=2)
        rel.append(dict(file=frame, regioes=det, changed_px=int((d > 1).sum()),
                        changed_pct=round(100 * float((d > 1).sum()) / d.size, 4)))
        for reg in regs:
            R = 85
            a = img0[reg['cy'] - R:reg['cy'] + R, reg['cx'] - R:reg['cx'] + R].astype(np.uint8)
            b = out[reg['cy'] - R:reg['cy'] + R, reg['cx'] - R:reg['cx'] + R][:, :, :3]
            Z = 4
            a = cv2.resize(a, (2 * R * Z, 2 * R * Z), interpolation=cv2.INTER_NEAREST)
            b = cv2.resize(b, (2 * R * Z, 2 * R * Z), interpolation=cv2.INTER_NEAREST)
            gap = np.full((a.shape[0], 12, 3), 255, np.uint8)
            cv2.imwrite(f"{S}cp_{frame.split('/')[-1][:6]}_{reg['nome']}.png",
                        np.hstack([a, gap, b]))
    print(json.dumps(rel, indent=2, ensure_ascii=False))
    sys.stdout.flush()


if __name__ == '__main__':
    main()
