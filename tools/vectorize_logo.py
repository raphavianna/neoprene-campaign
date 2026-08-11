#!/usr/bin/env python3
"""Vetoriza a arte do badge extraida por extract_logo_art.py.

POR QUE VETOR
    A arte raster ja resolve os frames atuais (600 px de fonte contra 90 px de
    alvo, com sobra). O SVG existe para o resto da campanha: qualquer take,
    qualquer escala, sem nunca mais depender de reamostrar foto de produto.

COMO
    Contornos com hierarquia (para preservar os vazados: o miolo do O, os
    contra-formas das letras), suavizacao leve antes do tracado para tirar o
    serrilhado do limiar sobre foto, e simplificacao poligonal com tolerancia
    sub-pixel. Coordenadas normalizadas num viewBox de 1000x1000 com o anel
    externo centrado — o mesmo referencial que o compositing usa.

O QUE NAO SE FAZ AQUI
    Nao se substitui o anel tracado por um circulo ideal, nem se "reconstroi"
    letra nenhuma a partir de fonte parecida. Tudo que sai no SVG veio da
    geometria medida na macro do produto. Aproximar tipografia de marca no
    chute e' exatamente o erro que este projeto existe para nao cometer.
"""
import numpy as np, cv2, json, sys

CANVAS = 1000
EPS = 0.6          # tolerancia de simplificacao, em px do canvas


def suaviza(mask):
    m = cv2.GaussianBlur(mask.astype(np.float32), (0, 0), 1.6)
    m = (m > 127).astype(np.uint8) * 255
    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, k)
    return cv2.morphologyEx(m, cv2.MORPH_CLOSE, k)


def contornos_svg(mask):
    cs, hier = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    paths, n_pts = [], 0
    for c in cs:
        if cv2.contourArea(c) < 12:
            continue
        ap = cv2.approxPolyDP(c, EPS, True).reshape(-1, 2)
        if len(ap) < 3:
            continue
        n_pts += len(ap)
        d = 'M ' + ' L '.join(f'{x:.2f},{y:.2f}' for x, y in ap) + ' Z'
        paths.append(d)
    return paths, n_pts


def main():
    S = '/tmp/claude-0/-home-user-neoprene-campaign/2a358ccf-002b-5c2c-9538-4f719f033e34/scratchpad/'
    rgba = cv2.imread('assets/wardrobe/badge_chest_art.png', cv2.IMREAD_UNCHANGED)
    mask = suaviza(rgba[:, :, 3])

    paths, n_pts = contornos_svg(mask)
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CANVAS} {CANVAS}" '
           f'width="{CANVAS}" height="{CANVAS}">',
           '  <title>OH — Use Zero Hora · badge circular do peito</title>',
           '  <desc>Tracado a partir da macro de produto LOGO-VERT.png, '
           'retificada de elipse para circulo pelo anel externo. Nenhuma letra '
           'reconstruida por aproximacao tipografica.</desc>',
           '  <g fill="#ffffff" fill-rule="evenodd">']
    for d in paths:
        svg.append(f'    <path d="{d}"/>')
    svg += ['  </g>', '</svg>', '']
    with open('assets/wardrobe/badge_chest.svg', 'w') as f:
        f.write('\n'.join(svg))

    # confere: rasteriza o vetor de volta e mede divergencia contra a mascara
    # rasteriza com a MESMA regra do SVG (evenodd). Pintar externos de branco e
    # vazados de preto nao serve: o furo interno do anel cobre todo o miolo e
    # apagaria o monograma e o arco. XOR sucessivo implementa evenodd exato.
    conf = np.zeros((CANVAS, CANVAS), bool)
    cs, hier = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    for c in cs:
        if cv2.contourArea(c) < 12:
            continue
        ap = cv2.approxPolyDP(c, EPS, True)
        tmp = np.zeros((CANVAS, CANVAS), np.uint8)
        cv2.drawContours(tmp, [ap], -1, 255, cv2.FILLED)
        conf ^= (tmp > 127)
    conf = conf.astype(np.uint8) * 255
    dif = (conf > 127) ^ (mask > 127)
    print(json.dumps(dict(paths=len(paths), pontos=n_pts,
                          px_arte=int((mask > 127).sum()),
                          divergencia_px=int(dif.sum()),
                          divergencia_pct=round(100 * float(dif.sum()) / max(1, (mask > 127).sum()), 3)),
                     indent=2))
    cv2.imwrite(S + 'vec_check.png', np.hstack([mask, np.full((CANVAS, 12), 128, np.uint8), conf]))
    sys.stdout.flush()


if __name__ == '__main__':
    main()
