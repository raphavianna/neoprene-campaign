#!/usr/bin/env python3
"""Extrai a ARTE do logo (albedo) das macros de produto, separada da luz.

POR QUE SEPARAR ARTE DE LUZ
    As macros sao fotos de estudio: luz frontal, brilho especular no relevo de
    borracha, sombra propria do bisel. Os frames de partida tem contraluz de
    golden hour sobre tecido molhado. Deformar a foto direto para dentro do
    frame importaria a iluminacao errada junto — e' o defeito classico que faz
    o logo parecer adesivo colado.

    Entao aqui se extrai apenas QUAIS AREAS sao relevo branco (a arte), jogando
    fora a iluminacao da macro. O relevo e' reconstruido depois, no compositing,
    coerente com a luz de cada frame.

RETIFICACAO
    As macros foram fotografadas em angulo, entao o badge circular aparece como
    elipse. O anel externo do proprio logo e' um circulo perfeito no plano da
    peca — serve de referencia geometrica muito melhor que a borda do disco de
    borracha, que tem baixo contraste contra o tecido. Ajusta-se a elipse ao
    anel e mapeia-se ela para circulo, retificando a arte inteira junto.

SAIDA
    PNG RGBA em alta resolucao com a arte em branco e fundo transparente,
    pronto para ser deformado para dentro de qualquer take, em qualquer escala.
"""
import numpy as np, cv2, json, sys

CANVAS = 1000          # lado do canvas retificado
R_ANEL = 430           # raio alvo do anel externo no canvas


def maior_anel(mask):
    """Componente cujo bbox e' o maior — o anel externo do badge."""
    n, lab, st, _ = cv2.connectedComponentsWithStats(mask.astype(np.uint8), 8)
    melhor, area_bbox = None, -1
    for i in range(1, n):
        w, h = st[i, cv2.CC_STAT_WIDTH], st[i, cv2.CC_STAT_HEIGHT]
        if w * h > area_bbox:
            area_bbox, melhor = w * h, i
    return (lab == melhor)


def extrai_badge(path, thr=140):
    im = cv2.imread(path)
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    arte = g > thr

    anel = maior_anel(arte)
    ys, xs = np.where(anel)
    pts = np.stack([xs, ys], 1).astype(np.float32)
    (cx, cy), (d1, d2), ang = cv2.fitEllipse(pts)

    # elipse -> circulo: desfaz rotacao, iguala os eixos, reaplica escala
    a, b = d1 / 2.0, d2 / 2.0
    th = np.deg2rad(ang)
    R = np.array([[np.cos(th), np.sin(th)], [-np.sin(th), np.cos(th)]])
    # R leva ao referencial dos eixos da elipse, Sc iguala os eixos, R.T volta
    # a orientacao original. Sem o R.T final a arte sai girada pelo angulo do
    # eixo da elipse, que nao tem relacao com o "de pe" do badge.
    Sc = np.array([[R_ANEL / a, 0], [0, R_ANEL / b]])
    M2 = R.T @ Sc @ R
    M = np.zeros((2, 3), np.float32)
    M[:, :2] = M2
    M[:, 2] = np.array([CANVAS / 2, CANVAS / 2]) - M2 @ np.array([cx, cy])

    art_ret = cv2.warpAffine(arte.astype(np.uint8) * 255, M, (CANVAS, CANVAS),
                             flags=cv2.INTER_LINEAR, borderValue=0)
    foto_ret = cv2.warpAffine(im, M, (CANVAS, CANVAS), flags=cv2.INTER_CUBIC,
                              borderValue=0)

    # "de pe" do badge: o arco de texto tem de ficar centrado embaixo. Mede-se
    # a media circular dos angulos da arte na faixa de raio do arco e gira-se
    # para leva-la a 90 graus (baixo, em coordenadas de imagem).
    yy, xx = np.mgrid[0:CANVAS, 0:CANVAS].astype(np.float32)
    dx_, dy_ = xx - CANVAS / 2, yy - CANVAS / 2
    rr = np.sqrt(dx_ ** 2 + dy_ ** 2)

    # isola as LETRAS do arco: componentes pequenos com centroide na faixa de
    # raio do arco. Exclui o anel (componente enorme) e o monograma (idem),
    # cuja parte inferior invadiria a faixa e enviesaria a medida.
    n, lab, st, cen = cv2.connectedComponentsWithStats((art_ret > 128).astype(np.uint8), 8)
    tot = (art_ret > 128).sum()
    angs = []
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] > 0.03 * tot:
            continue
        px, py = cen[i][0] - CANVAS / 2, cen[i][1] - CANVAS / 2
        r = np.hypot(px, py)
        if 0.70 * R_ANEL < r < 0.97 * R_ANEL:
            angs.append(np.degrees(np.arctan2(py, px)) % 360)
    if len(angs) >= 4:
        a_ord = np.sort(np.array(angs))
        ang_arco = float((a_ord.min() + a_ord.max()) / 2)   # centro do arco
    else:
        faixa = (art_ret > 128) & (rr > 0.72 * R_ANEL) & (rr < 0.95 * R_ANEL)
        t = np.arctan2(dy_[faixa], dx_[faixa])
        ang_arco = float(np.degrees(np.arctan2(np.sin(t).mean(), np.cos(t).mean())) % 360)
    giro = 90.0 - ang_arco
    Rg = cv2.getRotationMatrix2D((CANVAS / 2, CANVAS / 2), -giro, 1.0)
    art_ret = cv2.warpAffine(art_ret, Rg, (CANVAS, CANVAS), flags=cv2.INTER_LINEAR)
    foto_ret = cv2.warpAffine(foto_ret, Rg, (CANVAS, CANVAS), flags=cv2.INTER_CUBIC)

    return art_ret, foto_ret, dict(centro=[round(float(cx), 1), round(float(cy), 1)],
                                   eixos=[round(float(d1), 1), round(float(d2), 1)],
                                   angulo_elipse=round(float(ang), 2),
                                   razao_eixos=round(float(d1 / d2), 4),
                                   angulo_arco=round(float(ang_arco), 2),
                                   giro_aplicado=round(float(giro), 2))


def refaz_registrado(art):
    """Redesenha o simbolo ® e limpa a sujeira ao redor dele.

    Na macro o ® tem 45 px e a foto nao resolve os tracos do R: o limiar global
    ainda quebrava o anel do lado escuro e deixava um respingo solto. Limiar
    local fecha o anel, mas o miolo continua ruido — nao ganha legibilidade.

    O ® e' simbolo UNIVERSAL PADRONIZADO (circulo com R), nao tipografia da
    marca. Redesenha-lo nao e' o mesmo que redesenhar "USE ZERO HORA", que
    continua vindo integralmente da geometria medida. Diametro, espessura de
    traco e posicao saem do proprio simbolo extraido; so a forma interna do R
    e' desenhada.
    """
    n, lab, st, cen = cv2.connectedComponentsWithStats((art > 128).astype(np.uint8), 8)
    tot = (art > 128).sum()
    alvo, extras = None, []
    for i in range(1, n):
        a = st[i, cv2.CC_STAT_AREA]
        if a > 0.03 * tot:
            continue
        px, py = cen[i][0] - CANVAS / 2, cen[i][1] - CANVAS / 2
        r = np.hypot(px, py)
        if not (0.70 * R_ANEL < r < 0.99 * R_ANEL):
            continue
        ang = np.degrees(np.arctan2(py, px)) % 360
        if a < 120:                       # respingo
            extras.append(i)
        elif alvo is None or a < st[alvo, cv2.CC_STAT_AREA]:
            alvo, ang_alvo = i, ang       # o ® e' o menor glifo do arco

    out = art.copy()
    for i in extras + [alvo]:
        out[lab == i] = 0

    x, y = st[alvo, cv2.CC_STAT_LEFT], st[alvo, cv2.CC_STAT_TOP]
    w, h = st[alvo, cv2.CC_STAT_WIDTH], st[alvo, cv2.CC_STAT_HEIGHT]
    dia = max(w, h)
    cxs, cys = x + w / 2.0, y + h / 2.0

    Z = 8
    L = int(dia * 2 * Z)
    tile = np.zeros((L, L), np.uint8)
    c = (L // 2, L // 2)
    stroke = max(2, int(round(0.16 * dia * Z)))
    cv2.circle(tile, c, int(dia / 2 * Z - stroke / 2), 255, stroke, cv2.LINE_AA)
    fs = cv2.getFontScaleFromHeight(cv2.FONT_HERSHEY_DUPLEX,
                                    int(dia / 2 * Z * 0.95), max(1, stroke // 2))
    (tw, th), _ = cv2.getTextSize('R', cv2.FONT_HERSHEY_DUPLEX, fs, max(1, stroke // 2))
    cv2.putText(tile, 'R', (c[0] - tw // 2, c[1] + th // 2), cv2.FONT_HERSHEY_DUPLEX,
                fs, 255, max(1, stroke // 2), cv2.LINE_AA)
    # segue a inclinacao do arco, como as demais letras
    Rg = cv2.getRotationMatrix2D(c, -(ang_alvo - 90.0), 1.0)
    tile = cv2.warpAffine(tile, Rg, (L, L), flags=cv2.INTER_LINEAR)
    tile = cv2.resize(tile, (int(dia * 2), int(dia * 2)), interpolation=cv2.INTER_AREA)

    tx, ty = int(round(cxs - dia)), int(round(cys - dia))
    reg = out[ty:ty + tile.shape[0], tx:tx + tile.shape[1]]
    out[ty:ty + tile.shape[0], tx:tx + tile.shape[1]] = np.maximum(reg, tile)
    return out, dict(diametro=int(dia), angulo=round(float(ang_alvo), 1),
                     respingos_removidos=len(extras))


def main():
    S = '/tmp/claude-0/-home-user-neoprene-campaign/2a358ccf-002b-5c2c-9538-4f719f033e34/scratchpad/'
    art, foto, info = extrai_badge('assets/_raw/LOGO-VERT.png')
    art, reg_info = refaz_registrado(art)
    print(json.dumps(dict(fonte='LOGO-VERT.png', **info, registrado=reg_info), indent=2))

    art_s = cv2.GaussianBlur(art, (0, 0), 1.0)
    rgba = np.dstack([np.full_like(art_s, 255)] * 3 + [art_s])
    cv2.imwrite('assets/wardrobe/badge_chest_art.png', rgba)

    cv2.imwrite(S + 'ex_ret_foto.png', foto)
    cv2.imwrite(S + 'ex_ret_art.png', art_s)
    ov = foto.copy()
    ov[art_s > 128] = (0, 0, 255)
    cv2.imwrite(S + 'ex_ret_overlay.png', ov)
    sys.stdout.flush()


if __name__ == '__main__':
    main()


# ---------------------------------------------------------------------------
# Etiqueta horizontal da coxa
# ---------------------------------------------------------------------------

LAB_W, LAB_H = 1200, 312          # canvas canonico da etiqueta

# cantos do retangulo gravado interno da plaqueta, lidos em crop com grade.
# A plaqueta nao separa do tecido por brilho — fundo e borracha tem
# luminancia parecida — entao a geometria vem de leitura direta, nao de
# limiar. O trapezio confere: lado direito ~7% mais alto que o esquerdo,
# coerente com a perspectiva da foto.
CANTOS_ETIQUETA = np.float32([[76, 289], [677, 351], [665, 514], [64, 441]])


def extrai_etiqueta(path='assets/_raw/LOGOS-HORI.png', thr=150):
    im = cv2.imread(path)
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    arte = (g > thr).astype(np.uint8) * 255

    dst = np.float32([[0, 0], [LAB_W, 0], [LAB_W, LAB_H], [0, LAB_H]])
    H = cv2.getPerspectiveTransform(CANTOS_ETIQUETA, dst)
    art_ret = cv2.warpPerspective(arte, H, (LAB_W, LAB_H), flags=cv2.INTER_LINEAR)
    foto_ret = cv2.warpPerspective(im, H, (LAB_W, LAB_H), flags=cv2.INTER_CUBIC)

    # descarta o que sobrou da moldura: so o miolo interessa
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    art_ret = cv2.morphologyEx(art_ret, cv2.MORPH_OPEN, k)
    return art_ret, foto_ret, H


def limpa_etiqueta(art, area_min=250, topo=0.14):
    """Descarta o pontilhado da costura da moldura, que o limiar captura junto.

    Sao componentes pequenos e alinhados na faixa superior; a arte util (OH,
    barras, letras, ondas) tem area bem maior e vive na faixa central.
    """
    n, lab, st, cen = cv2.connectedComponentsWithStats((art > 128).astype(np.uint8), 8)
    out = np.zeros_like(art)
    mantidos = 0
    for i in range(1, n):
        if st[i, cv2.CC_STAT_AREA] < area_min:
            continue
        if cen[i][1] < topo * art.shape[0]:
            continue
        out[lab == i] = 255
        mantidos += 1
    return out, mantidos


def main_etiqueta():
    art, foto, H = extrai_etiqueta()
    art, n = limpa_etiqueta(art)
    art_s = cv2.GaussianBlur(art, (0, 0), 1.0)
    rgba = np.dstack([np.full_like(art_s, 255)] * 3 + [art_s])
    cv2.imwrite('assets/wardrobe/label_thigh_art.png', rgba)
    return dict(componentes=n, px_arte=int((art > 128).sum()),
                canvas=[LAB_W, LAB_H])
