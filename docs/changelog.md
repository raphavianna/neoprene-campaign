# Changelog — neoprene-campaign

## [Fase 0] Primeiro lote de assets — 6 arquivos classificados

Upload recebido em `assets/_raw/` e copiado para os tiers (originais preservados):

- `rosto.png` → `assets/identity/face/face_001.png` (Tier 1, Setup B)
- `frame-start-01.png` → `assets/start_frames/sf_001_setup_a_encontro_camera_3x4.png`
- `nedium-frame.png` → `assets/start_frames/sf_002_setup_a_plano_medio_16x9.png`
- `front.webp` → `assets/wardrobe/top_front_product.webp` (Tier 2)
- `006ebe…webp` → `assets/wardrobe/patch_thigh_macro.webp` (Tier 2)
- `64f99…webp` → `assets/wardrobe/bootie_sole_product.webp` (Tier 2, produto fora do escopo)

**Oito achados críticos registrados em `docs/asset_inventory.md`.** Os que bloqueiam produção:

1. Tipografia do patch adulterada nos dois frames gerados — o `achado_critico_logo` confirmado no material real.
2. Marca d'água do gerador nos dois frames — inaceitável em frame de partida, tende a se propagar pelo take.
3. `sf_001` é 3:4; o shot list exige 16:9. Só `sf_002` tem aspect correto.
4. Os dois frames são Setup A (composição de T3) — T1 e T2 seguem sem frame de partida e sem âncora de corpo.
5. Prancha dos frames (deck pad preto, leash na rabeta) contradiz o tracker (single-fin 9', leash no pulso).
6. Barra da bermuda não lê como open cell nos frames.
7. A tatuagem atribuída ao personagem provavelmente é do modelo de produto — revisão do dossiê pendente.
8. Sapatilha de neoprene é produto novo, fora do conjunto de duas peças declarado.

Nenhum `body_001`–`body_004` foi enviado, então a regra de identity lock não pode ser cumprida como escrita. Nenhum crédito consumido.

## [Fase 0] Frame de partida e guia de upload

- `docs/como_subir_assets.md` criado: passo a passo de upload, limites do navegador, destino por tipo de arquivo e a distinção entre frame de partida e imagem de referência.
- **`assets/start_frames/` criada** — categoria não prevista no master prompt v2.0.

**Decisão pendente de aprovação:** o master prompt v2.0 trata toda imagem enviada ao Seedance como "referência", sem separar o caso do **frame de partida** — a imagem que é o primeiro frame literal do vídeo e trava composição, luz e estado físico do segundo 0. São papéis com consequências diferentes, e a diferença é material no risco de logo: frame de partida em plano médio ou mais próximo carrega o patch para dentro do frame 0, e se for uma das três fotos do ensaio com o texto adulterado, o erro se propaga por todos os frames do take.

A pasta e a documentação já existem para destravar o upload. **Promover isso para dentro do `CLAUDE.md` (árvore de pastas + papel declarado por take na Fase 2/3) depende de aprovação** — o master prompt é a fonte de verdade e não foi editado por conta própria.

## [Fase 0] Bootstrap da estrutura — v2

- Master prompt renomeado de `claude.md` para `CLAUDE.md` na raiz, ativando-o como instrução persistente do repositório (item 2 da árvore de pastas da Fase 0).
- Árvore de pastas criada conforme a Fase 0: `assets/` (com `_raw/`, `identity/{face,body}/`, `wardrobe/`, `scenario/`, `support_marketing/`), `jobs/{stills,video}/`, `docs/` e `docs/history/`.
- Bíblias extraídas do master prompt para arquivos próprios de consulta: `character_bible.md`, `cinematography_bible.md`, `location_bible.md`, `continuity_tracker.md`, `shot_list.md`.
- `asset_inventory.md` criado com a hierarquia de três tiers, slugs de destino reservados e risco de logo por asset.
- `anti_ai_checklist_log.md` e este changelog abertos, vazios por ora.
- `README.md` com visão geral, estado atual e como retomar.
- **Zero créditos consumidos.** Nenhuma chamada ao Higgsfield.

**Pendências que saem da Fase 0:**

- Nenhum arquivo de asset está no repositório — as pastas de `assets/` estão vazias. Tier 1 e Tier 2 precisam ser enviados antes de qualquer geração, porque a identidade depende de referência de imagem direta em cada chamada.
- `docs/history/` está vazia: a v1 do master prompt não existe no histórico deste repositório (commit único de origem), então não havia o que arquivar.
- Demais arquivos de detalhe de produto citados no master prompt ainda não catalogados individualmente — dependem do upload.

## [Origem]

- `Add files via upload` (`ef93043`) — master prompt v2.0 adicionado ao repositório.

---

### Changelog do master prompt v1 → v2

Preservado aqui porque o cabeçalho do master prompt registra a transição:

- Correção estrutural do arco: as quatro fotos de corpo mostram exclusivamente o estado pós-surf molhado. Não existe referência do personagem seco. O shot list deixa de simular um bookend espelhado e passa a tratar a sequência ancorada como progressão dentro da própria saída, isolando remada, manobra em onda e entrada seca como bloco separado e não ancorado.
- Adicionados dossiê de personagem, bíblia de cinematografia e bíblia de locação — travam identidade, óptica e luz como decisão explícita, não como categoria vazia.
- Adicionado tracker de continuidade de props e estado físico (seco → molhado → escorrendo) por take.
- Tatuagem na canela direita removida da descrição verbal do prompt por decisão do usuário — a referência de imagem carrega isso sozinha. Não há instrução de removê-la do resultado.
- Cada take do shot list deixa de ser linha de tabela e vira mini-brief com ação segundo a segundo, estado físico, luz e câmera específicas.
