# ads_meta — Campanha Meta Ads · Linha Neoprene OH | Use Zero Hora

Workstream de **anúncios estáticos para Meta (Feed + Stories)**, objetivo **conversão** no site da marca.
Separado do pipeline de vídeo (`jobs/video/`) e dos stills (`jobs/stills/`).

## Decisões travadas (sessão 12-Ago-2026)
- **Motor de design:** Claude design lendo as imagens direto deste repositório (embute a foto; sem upload externo).
- **Mapa:** 1 anúncio por imagem → **6 anúncios × 2 formatos** = 12 peças.
- **Sobre o criativo:** Logo OH + **tagline curta** + **CTA**. Toda informação de produto/preço vai na **legenda**.
- **Formatos:** Feed **4:5 (1080×1350)** · Stories/Reels **9:16 (1080×1920)**.
- **Estética:** minimalista, editorial, foto manda; golden hour / Portra; preto fosco da peça + tipografia branca fina.

## Mapa imagem → anúncio

| # | Arquivo (source/) | Orientação | Produto foco | Setup/Luz | Tratamento p/ 4:5 e 9:16 | Obs |
|---|---|---|---|---|---|---|
| 01 | `01_hero-frontal_look_setupA_vert.png` | Retrato 3:4 | Look (camiseta+bermuda) — **HERO** | A (montanha), golden | Crop direto, sobra p/ tipografia embaixo | patch de peito legível → cuidar do logo |
| 02 | `02_meio-corpo_sheen_setupA_horiz.png` | Paisagem 1.8 | Camiseta (sheen) | A, golden | Reframe: foto no topo, faixa/negativo p/ type | landscape largo, precisa banda |
| 03 | `03_caminhada_mata_setupB_horiz.png` | Paisagem 1.5 | Look / caminhada | B (mata), golden | Reframe editorial vertical | |
| 04 | `04_meio-corpo_backlight_horiz.png` | Paisagem 1.5 | Look (backlight) | A/B, golden | Reframe editorial vertical | |
| 05 | `05_costas_look-completo_sapatilha_vert.png` | Retrato 3:4 | **Sapatilha** + look completo | **Azul meio-dia (destoa)** | Crop direto | única foto com sapatilha; luz fria fora do set → tratar no grade |
| 06 | `06_bermuda_detalhe-coxa_macro_horiz.png` | Paisagem 1.5 | **Bermuda** (macro etiqueta) | Golden | Crop macro, type sobre negativo | ótimo p/ detalhe de material |

## Variáveis pendentes (preencher antes de finalizar criativos + legendas)
- [ ] `PRODUTO_NOME` (camiseta / bermuda / sapatilha) — via sync Nuvemshop
- [ ] `PRECO` por produto — via sync Nuvemshop
- [ ] `TAMANHOS` / SKU — via sync Nuvemshop
- [ ] `URL_DESTINO` por produto (conversão) — via sync Nuvemshop
- [ ] `TAGLINE` da linha — a confirmar com Raphael
- [ ] `CTA` (ex.: "Compre agora", "Conheça a linha") — a confirmar
- [ ] Logo vetor/mono branco em PNG transparente — **falta** (hoje só há foto do patch de borracha)

## Estrutura
- `source/` — fotos originais renomeadas (fonte de verdade visual)
- `briefs/` — prompt(s) de diretor de arte por peça
- `feed/` — saída 4:5
- `stories/` — saída 9:16
- `captions/` — legendas (carregam a informação)
