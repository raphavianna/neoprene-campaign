# Como subir os assets — guia prático

Este arquivo responde uma pergunta só: **onde eu coloco cada imagem que já tenho.**

---

## O caminho curto (recomendado)

**Joga tudo em `assets/_raw/` de uma vez. Sem renomear nada. Eu classifico depois.**

Isso não é preguiça, é a regra da Fase 0 item 3: *"Original preservado em `assets/_raw/` antes de renomear."* O `_raw/` é o depósito de entrada — nome de arquivo do celular, do WhatsApp, do Drive, tanto faz. Depois que estiverem lá, eu abro cada imagem, identifico o que é, e copio para o tier certo com o slug canônico.

### Passo a passo

1. Abrir: **https://github.com/raphavianna/neoprene-campaign/tree/claude/ativar-workflow-projeto-axprrl/assets/_raw**
2. Botão **Add file** → **Upload files**.
3. Arrastar todos os arquivos de uma vez.
4. Na caixa de commit embaixo, conferir que está marcado **"Commit directly to the `claude/ativar-workflow-projeto-axprrl` branch"**.
   ⚠️ **Não** marcar "Create a new branch" e **não** subir para a `main`.
5. **Commit changes**.

### Limites do upload pelo navegador

| Limite | Valor |
|---|---|
| Tamanho por arquivo | 25 MB |
| Arquivos por lote de arrastar | 100 |

Arquivo acima de 25 MB ou vídeo de referência: não sobe por aí. Manda por Google Drive numa pasta compartilhada que eu puxo de lá (o conector do Drive está ativo nesta sessão).

### Formato

Sobe o **original**, na resolução máxima que você tiver. PNG ou JPG. Não redimensiona, não comprime, não passa por app de edição antes. A qualidade da referência entra direto na qualidade do identity lock — imagem recomprimida degrada o ancoramento de rosto.

---

## O caminho longo (se você preferir já organizar na mão)

Cada arquivo vai para a pasta do seu papel. Os slugs abaixo são os que `docs/asset_inventory.md` já reservou — usar exatamente esses nomes (a extensão pode ser `.png` ou `.jpg`).

### `assets/identity/` — Tier 1, quem é o personagem

Serve para travar identidade em toda chamada Seedance. É o único tier que pode ancorar rosto e corpo.

| Arquivo | Onde vai |
|---|---|
| Retrato macro três-quartos (Setup B, fundo verde desfocado) | `assets/identity/face/face_001.png` |
| Setup A, plano médio frontal, paisagem — montanha ao fundo, olhar direto | `assets/identity/body/body_001.png` |
| Setup A, plano médio frontal, retrato | `assets/identity/body/body_002.png` |
| Setup B, plano aberto lateral, diptique com detalhe de patch/prancha | `assets/identity/body/body_003.png` |
| Setup B, transição na água rasa, luz de contorno forte | `assets/identity/body/body_004.png` |

### `assets/wardrobe/` — Tier 2, como a peça é

**Nunca como referência de identidade** — o modelo das fotos de produto não é o talent. Se uma foto de produto entrar como referência de rosto, o personagem vira outra pessoa.

`patch_chest_macro` · `patch_thigh_macro` · `waist_drawcord` · `top_back_construction` · `sleeve_side_panel` · `material_neoprene_body` · `material_open_cell_hem`

Tem mais detalhe de produto além desses? Sobe todos assim mesmo, em `_raw/`. O master prompt manda catalogar sem descartar nenhum.

### `assets/scenario/` — praia sem personagem

Plates de locação, referência de luz, de arrebentação, de linha de mata. Se você tem foto do lugar sem o modelo, é aqui.

### `assets/support_marketing/` — Tier 3, só leitura humana

Infográficos com texto e diagramação sobrepostos. **Nunca entram como referência de imagem numa geração** — o modelo copiaria a diagramação para dentro do frame. Servem para eu ler e escrever o prompt certo.

O infográfico **"ETIQUETA EMBORRACHADA"** é o mais importante do repo inteiro: é a fonte de verdade geométrica e tipográfica do patch, acima das fotos do ensaio. Vai em `assets/support_marketing/infografico_etiqueta_emborrachada.png`.

### `assets/start_frames/` — frame de partida

Ver a seção abaixo. Nome: `sf_001_<descricao_curta>.png`, `sf_002_...` e assim por diante.

### `jobs/stills/` — saídas da campanha de still

Resultado dos jobs de imagem já rodados (`07b4ffb6` aprovado, `v2_board.png` com a prancha corrigida). É arquivo de produção, não referência ativa.

---

## Frame de partida ≠ imagem de referência

Isso é a parte que o master prompt v2.0 não cobre, e a distinção muda o resultado.

**Imagem de referência** (`assets/identity/`, `assets/wardrobe/`) — entra na chamada como âncora. O modelo lê dela quem é a pessoa e como a roupa se comporta, mas **inventa o enquadramento**. Composição, distância de câmera e luz do segundo 0 saem do texto do prompt.

**Frame de partida** (`assets/start_frames/`) — é o **primeiro frame literal do vídeo**. O take nasce exatamente daquela imagem e se move a partir dela. Composição, enquadramento, luz, estado de molhado, posição da prancha: tudo já está decidido, o prompt só descreve o que acontece **depois**.

Consequência prática:

- Com frame de partida, o risco de deriva de identidade despenca — o rosto do segundo 0 é literalmente o rosto da foto, não uma reconstrução.
- Em compensação, o take fica preso àquela composição. Não dá para pedir um enquadramento diferente do que a imagem já tem.
- **No risco de logo isso pesa:** se o frame de partida for uma das três fotos do ensaio com o texto do patch adulterado, o take começa com o logo errado e o erro se propaga por todos os frames seguintes. Frame de partida em plano médio ou mais próximo exige checar o patch **antes** de aprovar o take, não depois.

Por isso `start_frames/` é pasta separada e não um arquivo solto dentro de `identity/`: o papel é outro, e a decisão "T1 usa frame de partida ou não" precisa ficar registrada por take.

### Quando você subir o seu

Sobe em `assets/start_frames/` e me diz **de qual take ele é** (T1, T2 ou T3 — ver `docs/shot_list.md`). Eu registro no inventário, no shot list e depois no `job_metadata.json` do take. Se ele veio de um still já aprovado, fica uma cópia aqui mesmo assim — `jobs/stills/` é histórico de produção, `start_frames/` é papel ativo de produção.

---

## Depois que você subir

Me avisa. Eu:

1. Abro cada imagem e identifico o que é.
2. Copio de `_raw/` para o tier certo com o slug canônico — o original em `_raw/` fica intacto.
3. Atualizo `docs/asset_inventory.md` trocando "pendente de upload" pelo caminho real, com risco de logo confirmado arquivo a arquivo (aviso se achar mais fotos com o texto do patch adulterado).
4. Comito e reporto o que entrou, o que faltou e o que não bateu com o esperado.
