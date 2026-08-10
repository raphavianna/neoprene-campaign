#!/usr/bin/env python3
"""Remove a marca d'agua do gerador (sparkle astroide de 4 pontas) dos frames.

MODELO
    A marca e' uma sobreposicao de branco com transparencia constante:
        observed = (1 - a*m)*bg + a*m*255
    logo ela e' INVERTIVEL:
        bg = (observed - a*m*255) / (1 - a*m)
    Isso RECUPERA a textura real do fundo. Nao e' inpaint: nenhum pixel e'
    inventado dentro da area da marca.

PARAMETROS — medidos, nao arbitrados
    forma  astroide  |u|^p + |v|^p <= 1  com p = 2/3.
           O expoente foi medido em sf_001 pela extensao diagonal da marca
           (resultado 0.667) e nao assumido.
    alpha  medido por dois metodos independentes que concordaram em sf_001:
           (1) perfil de alpha por conchas de raio, com fundo estimado por
               inpaint a partir de fora -> plato em 0.28;
           (2) degrau local em pares de pixels cruzando a borda pela normal,
               imune a variacao global de fundo -> mediana 0.289.
           Em sf_002 o fundo e' espuma clara: (255-bg) fica pequeno, o
           estimador perde precisao e a dispersao explode, entao o alpha de
           cada marca foi fechado por inspecao visual em torno do valor de
           sf_001 (0.30 e 0.28).
    centro e tamanho  lidos em crop ampliado com grade de coordenadas, com
           realce local de contraste onde a marca cai sobre espuma.

BORDA
    Depois da inversao sobra um fio de 1-2 px no contorno, porque o antialias
    original nao e' exatamente reproduzivel. So essa faixa recebe inpaint —
    3 px de largura, vizinhos imediatos, nada a inventar. O interior nunca.

O QUE FOI TENTADO E DESCARTADO (para nao repetir)
    - Ajuste automatico de (centro, tamanho, alpha) minimizando energia de
      borda com a banda de avaliacao derivada do proprio candidato: o
      otimizador encolhe a mascara e zera o alpha, porque assim a banda cai no
      interior liso da marca e o custo despenca. Objetivo explorado.
    - Subtracao do residuo por mediana de concha ("de-ring"): realca o
      contorno em vez de apaga-lo.
    - Inpaint TELEA da area inteira da marca (~100 px): vira borrao radial,
      visualmente pior que a propria marca.
"""
import numpy as np, cv2, json, sys

EXPO = 2 / 3

JOBS = [
    dict(src='assets/_raw/frame-start-01.png',
         dst='assets/start_frames/sf_001_setup_a_encontro_camera_3x4.png',
         marks=[dict(cx=1552, cy=2150, size=104, alpha=0.289)]),
    dict(src='assets/_raw/nedium-frame.png',
         dst='assets/start_frames/sf_002_setup_a_plano_medio_16x9.png',
         marks=[dict(cx=2509, cy=1296, size=100, alpha=0.30),
                dict(cx=2640, cy=1426, size=88, alpha=0.28)]),
]


def coverage(shape, ox, oy, s, ss=6):
    """Cobertura antialiasada por supersampling espacial da forma nitida."""
    h, w = shape
    ny, nx = h * ss, w * ss
    yy, xx = np.mgrid[0:ny, 0:nx].astype(np.float32)
    xx = (xx + 0.5) / ss - 0.5
    yy = (yy + 0.5) / ss - 0.5
    u = (xx - ox) * (2.0 / s)
    v = (yy - oy) * (2.0 / s)
    hard = ((np.abs(u) ** EXPO + np.abs(v) ** EXPO) <= 1.0).astype(np.float32)
    return cv2.resize(hard, (w, h), interpolation=cv2.INTER_AREA)


def remove_mark(img, cx, cy, size, alpha, band=2):
    P = int(size * 1.25)
    x0, y0 = max(0, cx - P), max(0, cy - P)
    x1, y1 = min(img.shape[1], cx + P), min(img.shape[0], cy + P)
    win = img[y0:y1, x0:x1]
    m = coverage(win.shape[:2], cx - x0, cy - y0, size)

    a = np.clip(m * alpha, 0, 0.95)[:, :, None]
    rec = np.clip((win - a * 255.0) / (1.0 - a), 0, 255).round().astype(np.uint8)

    edge = ((m > 0.01) & (m < 0.99)).astype(np.uint8)
    bm = cv2.dilate(edge, np.ones((2 * band + 1, 2 * band + 1), np.uint8))
    fixed = cv2.inpaint(rec, bm, 3, cv2.INPAINT_TELEA)
    sel = bm.astype(bool)
    rec[sel] = fixed[sel]

    img[y0:y1, x0:x1] = rec.astype(np.float32)
    return img


def main():
    report = []
    for job in JOBS:
        src = cv2.imread(job['src'], cv2.IMREAD_UNCHANGED)
        if src is None:
            raise SystemExit(f"nao consegui ler {job['src']}")
        img0 = src[:, :, :3].astype(np.float32)
        cur = img0.copy()
        for mk in job['marks']:
            cur = remove_mark(cur, **mk)
        out = cur.round().astype(np.uint8)
        if src.shape[2] == 4:
            out = np.dstack([out, src[:, :, 3]])
        cv2.imwrite(job['dst'], out, [cv2.IMWRITE_PNG_COMPRESSION, 6])
        d = np.abs(cur - img0).max(axis=2)
        report.append(dict(src=job['src'], dst=job['dst'], marks=job['marks'],
                           changed_px=int((d > 1).sum()),
                           changed_pct=round(100 * float((d > 1).sum()) / d.size, 4),
                           resolucao=[int(out.shape[1]), int(out.shape[0])]))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    sys.stdout.flush()


if __name__ == '__main__':
    main()
