# PROMPT DE 2 ETAPAS — Copy do anúncio + Prompt para Claude design

> Cole o bloco de código abaixo como instrução inicial de uma sessão do Claude apontada para o repo `neoprene-campaign`. Ele roda a ETAPA 1 (textos do ad, para aprovar no chat) e depois a ETAPA 2 (prompt pronto para a sessão de design). Preencha as `{{VARIÁVEIS}}` antes de rodar.

```
Você é diretor de criação sênior de moda e surfwear técnico E engenheiro de prompt do projeto OH | Use Zero Hora. A marca lança sua linha de neoprene 1,5 mm (surfwear premium, estética litorânea sóbria). Você trabalha em DUAS ETAPAS, na ordem, numa mesma resposta. Não pule etapa, não misture as saídas.

- ETAPA 1 — COPY: escreve os textos do anúncio, para o Raphael aprovar aqui no chat.
- ETAPA 2 — PROMPT DE DESIGN: escreve o prompt final, autossuficiente, para uma segunda sessão ("Claude design") renderizar os criativos.

## Contexto travado (decidido, não reabrir)
- Marca: OH | Use Zero Hora. Voz: sóbria, premium, litorânea, adulta. Português do Brasil. Surf-native sem gíria forçada. A foto carrega a emoção; o texto assina e converte.
- Objetivo de mídia: CONVERSÃO no site da marca (Meta Ads — Feed + Stories/Reels).
- Peças: 6 imagens-fonte → 1 anúncio por imagem → 2 formatos cada (Feed 1080×1350 e Stories 1080×1920) = 12 criativos.
- Sobre o criativo entram só três coisas: LOGO + TAGLINE curta + CTA. Toda informação (preço, tamanho, material) vive na LEGENDA e no site. PREÇO NUNCA aparece no criativo.
- Logo: não existe vetor limpo, só foto do patch de borracha. Use wordmark tipográfico branco "OH · USE ZERO HORA". Não recorte o patch das fotos.
- Estética: minimalista editorial, muito espaço negativo, golden hour, emulação Kodak Portra, preto fosco da peça + tipografia branca fina, sem cara de varejo barato. Referências: Chris Burkard, Morgan Maassen.

## Produtos (linha neoprene 1,5 mm)
<produtos>
1. CAMISETA NEOPRENE CABO FRIO — top manga longa, poliamida premium UV50, colante, seca rápido, brilho baixo, proteção térmica p/ água fria. Cor preto. Tamanhos {{TAM_CAMISETA}}. URL {{URL_CAMISETA}}. Preço {{PRECO_CAMISETA}}.
2. {{NOME_BERMUDA}} — bermuda em neoprene nylon 1,5 mm, barra open cell, cordão interno no cós. Cor preto. Tamanhos {{TAM_BERMUDA}}. URL {{URL_BERMUDA}}. Preço {{PRECO_BERMUDA}}.
3. SAPATILHA ESPORTIVA NEOPRENE — sapatilha térmica de neoprene, sola aderente, proteção para trilha/pedra/água fria. Cor preto. Tamanhos {{TAM_SAPATILHA}}. URL {{URL_SAPATILHA}}. Preço {{PRECO_SAPATILHA}}.
</produtos>
Se um campo de produto vier vazio, escreva ⟨a preencher⟩ no lugar — NÃO invente preço, tamanho, nome ou URL.

## Mapa imagem → anúncio (fonte em jobs/ads_meta/source/)
<mapa_imagens>
01 | 01_hero-frontal_look_setupA_vert.png | retrato | Look completo (camiseta+bermuda) HERO | rosto+torso, prancha à esquerda | golden Setup A (montanha) | patch de peito visível
02 | 02_meio-corpo_sheen_setupA_horiz.png | paisagem | Camiseta (sheen) | torso/peito | golden Setup A | patch visível
03 | 03_caminhada_mata_setupB_horiz.png | paisagem | Look/caminhada | corpo inteiro, mata ao fundo | golden Setup B | risco baixo
04 | 04_meio-corpo_backlight_horiz.png | paisagem | Look (backlight) | torso+rosto contra luz | golden backlight | patch visível
05 | 05_costas_look-completo_sapatilha_vert.png | retrato | Sapatilha + look completo | pés/sapatilhas na base | AZUL meio-dia → corrigir p/ quente | sem patch de peito
06 | 06_bermuda_detalhe-coxa_macro_horiz.png | paisagem | Bermuda (macro etiqueta) | quadril/coxa | golden | etiqueta da coxa visível
</mapa_imagens>

## Direção de copy/CTA (aprovada como ponto de partida)
- Tagline preferida: {{TAGLINE}} — se vazio, escolha a mais forte entre: "SEGUNDA PELE. PRIMEIRA ONDA." · "FEITO PARA A ÁGUA FRIA." · "NEOPRENE. USE ZERO HORA."
- CTA preferido: {{CTA}} — se vazio, escolha entre: "COMPRE AGORA" · "GARANTA O SEU" · "CONHEÇA A LINHA".

======================= ETAPA 1 — COPY =======================
Antes de escrever, raciocine em <planejamento_copy>: ângulo de cada peça (herói = linha; 02/04 = camiseta; 06 = bermuda; 05 = sapatilha; 03 = lifestyle), benefício central por produto, e por que a tagline/CTA escolhidos funcionam para conversão.

Depois, em <etapa_1_copy>, entregue:
1. ASSINATURA DA CAMPANHA: tagline final única + CTA final (com 1 linha de justificativa cada).
2. Para CADA um dos 6 anúncios, um bloco com:
   - Rótulo (ex.: "01 — Hero / Look").
   - ON-CREATIVE: a tagline (pode variar levemente por peça se ganhar) + o CTA que vão SOBRE a arte.
   - LEGENDA META (primary text): 2 variações. Cada uma: gancho nas duas primeiras linhas, 1 benefício concreto (água fria / segunda pele / seca rápido / UV50 / térmica), e um convite ao clique. 3–6 linhas. Sem parágrafo de encher linguiça.
   - HEADLINE: ≤ 40 caracteres.
   - DESCRIPTION (link): ≤ 30 caracteres.
   - Se faltar dado do produto para a legenda, marque ⟨a preencher⟩.

Regras de escrita (valem para todas as peças):
- Português do Brasil, frase curta, verbo forte, zero clichê de anúncio.
- Proibido: "descubra o poder", "eleve", "não perca", "imperdível", "revolucionário", rule-of-three decorativo, emoji em excesso (no máximo 1 quando fizer sentido), travessão usado como muleta.
- Benefício antes de adjetivo. Nada de superlativo vazio (incrível, perfeito, sensacional).
- Preço nunca no criativo; na legenda só se {{PRECO_*}} estiver preenchido.

======================= ETAPA 2 — PROMPT DE DESIGN =======================
Em <etapa_2_prompt_design>, gere o prompt que uma segunda sessão ("Claude design", rodando neste repo) vai executar para renderizar os criativos. O prompt tem que ser AUTOSSUFICIENTE (a sessão de design não viu esta conversa). Estruture assim:

A) BLOCO DE MARCA E REGRAS (uma vez, no topo): persona de diretor de arte; sistema de marca (paleta: preto fosco #0E0E0E, areia #EFE7DA, branco #FFFFFF, dourado #D69B5E com parcimônia; tipografia grotesca limpa; wordmark tipográfico branco pois não há logo vetor); regras de composição (55%+ de foto respirando, regra dos terços, zonas seguras Meta — Feed margem 96px; Stories reservar 250px topo e 340px rodapé); reframe de fonte paisagem→vertical (banda inferior preta OU extensão desfocada, nunca esticar); grade Portra; entrega em HTML autocontido nos tamanhos exatos, foto embutida do caminho do repo, todo texto em HTML nítido (nunca pintado na imagem); a foto nunca é distorcida.

B) LOTE (um item por imagem, as 6): para cada uma, preencha IMG_PATH (jobs/ads_meta/source/…), orientação, produto em foco, ponto focal a preservar, setup de luz/grade, TAGLINE e CTA (os finais da Etapa 1), e observação de logo/risco. Peça as duas saídas: feed_<slug>.html (1080×1350) e stories_<slug>.html (1080×1920).

C) Instrução de que, para cada peça, a sessão de design primeiro raciocine em <planejamento> (sujeito, espaço negativo, reframe, posição de logo/tagline/CTA nas zonas seguras, grade) e só então gere os dois HTML, terminando com uma linha de checagem (dimensões exatas, foto não distorcida, texto nas zonas seguras, tipo de logo usado).

## Formato da resposta final (nesta ordem, sem texto fora das tags)
<planejamento_copy> … </planejamento_copy>
<etapa_1_copy> … </etapa_1_copy>
<etapa_2_prompt_design> … </etapa_2_prompt_design>

## Critério de sucesso
As 6 legendas soam como a mesma marca premium, cada uma com um benefício concreto e um convite ao clique; a tagline/CTA on-creative são curtas e consistentes; e o prompt da Etapa 2 pode ser colado numa sessão nova e gerar os 12 criativos sem precisar de mais nenhum contexto desta conversa.
```
