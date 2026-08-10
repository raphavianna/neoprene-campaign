# Inventário de assets — neoprene-campaign

> Hierarquia de três camadas conforme `CLAUDE.md` → `<hierarquia_de_assets>`.

**Estado na Fase 0:** o repositório foi clonado contendo **apenas o master prompt**. Nenhum arquivo binário de asset está versionado ainda. A estrutura de pastas está criada e vazia; este inventário registra o que o master prompt declara como esperado, com o slug de destino já reservado. Nada foi descartado — o que existe hoje é ausência de upload, não perda.

**Regra de importação (Fase 0, item 3):** todo arquivo entra primeiro em `assets/_raw/` com o nome original preservado, e só então é copiado/renomeado para o destino de tier. Renomear sobre o original é proibido.

**Como subir:** ver `docs/como_subir_assets.md` para o passo a passo.

---

## TIER 1 — Ancoragem de identidade

Usável como referência de identidade em chamadas Seedance.

| Slug de destino | Caminho | Descrição | O que ancora | Risco de logo | Status |
|---|---|---|---|---|---|
| `face_001` | `assets/identity/face/` | Retrato macro três-quartos, Setup B | Rosto, cabelo molhado, micro-expressão | Baixo (patch fora de quadro) | pendente de upload |
| `body_001` | `assets/identity/body/` | Setup A, plano médio frontal, paisagem | Identidade + Setup A + olhar direto | **Alto** — patch em distância de leitura | pendente de upload |
| `body_002` | `assets/identity/body/` | Setup A, plano médio frontal, retrato | Identidade + Setup A | **Alto** — patch em distância de leitura | pendente de upload |
| `body_003` | `assets/identity/body/` | Setup B, plano aberto lateral, diptique com detalhe de patch/prancha | Setup B, caminhada, tatuagem da canela direita | Médio | pendente de upload |
| `body_004` | `assets/identity/body/` | Setup B, transição na água rasa, luz de contorno forte, diptique com detalhe | Setup B, pico de molhado, backlight | Médio | pendente de upload |

## TIER 2 — Ancoragem de peça

**Nunca como referência de identidade** — o modelo das fotos de produto não é o talent.

| Slug de destino | Caminho | Descrição | O que ancora | Risco de logo | Status |
|---|---|---|---|---|---|
| `patch_chest_macro` | `assets/wardrobe/` | Patch do peito, macro, canônico | Geometria e tipografia do patch | Fonte de verdade do logo | pendente de upload |
| `patch_thigh_macro` | `assets/wardrobe/` | Patch/etiqueta da coxa, macro | Tipografia secundária | Alto | pendente de upload |
| `waist_drawcord` | `assets/wardrobe/` | Cordão interno do cós | Construção do cós | Baixo | pendente de upload |
| `top_back_construction` | `assets/wardrobe/` | Costas do top — corte raglan, gola | Costura e caimento | Baixo | pendente de upload |
| `sleeve_side_panel` | `assets/wardrobe/` | Painel lateral da manga, recorte de poliamida | Recorte em malha nos flancos | Baixo | pendente de upload |
| `material_neoprene_body` | `assets/wardrobe/` | Textura do corpo da bermuda, neoprene fechado 1,5mm | Brilho de borracha molhada | Baixo | pendente de upload |
| `material_open_cell_hem` | `assets/wardrobe/` | Textura da barra, open cell/nylon 1,5mm | Espessura e costura flat-lock | Baixo | pendente de upload |

**Inventário pendente:** o master prompt registra "demais arquivos de detalhe de produto recebidos, catalogar na Fase 0 sem descartar nenhum". Esses arquivos não chegaram ao repositório. Catalogar individualmente assim que forem enviados — a lista acima é o mínimo declarado, não o total.

## FRAME DE PARTIDA — papel de produção, não tier

`assets/start_frames/`

Categoria **adicionada na Fase 0**, não prevista no master prompt v2.0. Pendente de promoção para o `CLAUDE.md` (ver `docs/changelog.md`).

Frame de partida é o **primeiro frame literal do vídeo** — o take nasce dele e se move a partir dali. Diferente de uma referência de identidade, que ancora quem é a pessoa mas deixa o enquadramento por conta do prompt, o frame de partida trava composição, luz e estado físico do segundo 0.

Por que fica em pasta própria e não dentro de `identity/`:

- O papel é outro. A mesma imagem pode ser boa âncora de identidade e péssimo frame de partida (ou o contrário).
- A decisão "este take usa frame de partida" é por take e precisa ficar registrada — vai no `job_metadata.json` do take e no `docs/shot_list.md`.
- **Interação com o risco de logo:** um frame de partida em plano médio ou mais próximo carrega o patch para dentro do frame 0. Se for uma das três fotos do ensaio com o texto adulterado, o erro de tipografia se propaga por todos os frames do take. Frame de partida com patch em distância de leitura exige verificação do patch **antes** de aprovar o take.

| Slug de destino | Take | Origem | Risco de logo | Status |
|---|---|---|---|---|
| `sf_001_<descricao>` | a atribuir | a declarar no upload | a verificar | pendente de upload |

Se o frame de partida vier de um still já aprovado, uma cópia fica aqui mesmo assim: `jobs/stills/` é histórico de produção, `assets/start_frames/` é papel ativo.

## TIER 3 — Suporte de prompt apenas

**Nunca como referência de imagem em geração.** Servem para leitura humana e redação de prompt.

| Slug de destino | Caminho | Descrição | Status |
|---|---|---|---|
| `infografico_etiqueta_emborrachada` | `assets/support_marketing/` | Infográfico de produto com texto/diagramação sobreposta. Fonte de verdade **geométrica e tipográfica** do patch — acima das fotos do ensaio | pendente de upload |
| demais infográficos | `assets/support_marketing/` | Materiais de marketing com texto sobreposto | pendente de upload |

---

## Herança de still

- Job `07b4ffb6` (`nano_banana_pro`) — **aprovado**, sobrepõe `fea50396` (`seedream_v4_5`, descartado).
- `v2_board.png` — prancha corrigida.
- Correção de cabelo: **iniciada e não fechada**. Não usar como padrão de referência para o vídeo.

Arquivos de saída da campanha de still, quando importados, vão para `jobs/stills/`.

## Achado crítico de logo

O patch circular do peito ("OH · USE ZERO HORA®", borracha emborrachada em alto-relevo) sai com texto correto em **apenas uma** das quatro fotos do ensaio; nas outras três o texto está adulterado — alucinação de tipografia clássica. Por isso a fonte de verdade do patch é o infográfico Tier 3, **não** as fotos do ensaio.

Regra por take: patch em distância de leitura (plano médio ou mais próximo) = risco de logo, decidir explicitamente entre travar o patch como referência de imagem adicional ou gerar a área em branco/neutro para composição posterior. Plano geral/distante = risco baixo. A decisão vai declarada no relatório de aprovação do take — nunca assumida em silêncio.
