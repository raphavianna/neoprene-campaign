# Inventário de assets — neoprene-campaign

> Hierarquia de três camadas conforme `CLAUDE.md` → `<hierarquia_de_assets>`.
> **Última atualização:** primeiro lote de upload (6 arquivos) recebido e classificado.

**Regra de importação (Fase 0, item 3):** todo arquivo entra primeiro em `assets/_raw/` com o nome original preservado, e só então é **copiado** (não movido) para o destino de tier. Os originais em `_raw/` permanecem intactos.

**Como subir mais:** ver `docs/como_subir_assets.md`.

---

## TIER 1 — Ancoragem de identidade

| Slug | Caminho | Origem | Descrição | Risco de logo | Status |
|---|---|---|---|---|---|
| `face_001` | `assets/identity/face/face_001.png` | `rosto.png` (1024×1024) | Retrato três-quartos, cabelo molhado com mechas definidas e gotas visíveis, boca levemente entreaberta, olhar fora de quadro. Fundo verde desfocado de mata + céu estourado = **Setup B**. Bate com o dossiê. | Baixo — patch fora de quadro | ✅ importado |
| `body_001` | `assets/identity/body/` | — | Setup A, plano médio frontal, paisagem | Alto | ❌ **não enviado** |
| `body_002` | `assets/identity/body/` | — | Setup A, plano médio frontal, retrato | Alto | ❌ **não enviado** |
| `body_003` | `assets/identity/body/` | — | Setup B, plano aberto lateral, diptique com detalhe | Médio | ❌ **não enviado** |
| `body_004` | `assets/identity/body/` | — | Setup B, transição na água rasa, backlight forte | Médio | ❌ **não enviado** |

**Consequência operacional:** sem nenhum `body_*`, a regra de identity lock (`face_001` + um `body_*` em todo plano médio ou mais próximo) **não pode ser cumprida como escrita**. Os dois frames de partida abaixo podem cobrir o papel de âncora de corpo, mas são **saída gerada**, não foto de ensaio — usar um output como âncora propaga qualquer erro que ele já carregue. Ver os achados críticos no fim deste arquivo.

## FRAME DE PARTIDA

`assets/start_frames/` — primeiro frame literal de um take. Categoria adicionada na Fase 0, pendente de promoção ao `CLAUDE.md`.

| Slug | Caminho | Origem | Formato | Setup / take | Status |
|---|---|---|---|---|---|
| `sf_001` | `assets/start_frames/sf_001_setup_a_encontro_camera_3x4.png` | `frame-start-01.png` | 1792×2390 — **3:4 retrato** | Setup A, corpo inteiro, caminhando de encontro à câmera, olhar direto → composição de **T3** | ⚠️ marca d'água removida; **aspect e patch pendentes** |
| `sf_002` | `assets/start_frames/sf_002_setup_a_plano_medio_16x9.png` | `nedium-frame.png` | 2752×1536 — **16:9 exato** | Setup A, plano médio, olhar direto, gota escorrendo da mão → composição de **T3** | ⚠️ marca d'água removida; **patch pendente** |

Os arquivos em `assets/start_frames/` são as versões **com a marca d'água removida**. Os originais intactos seguem em `assets/_raw/`. O que ainda bloqueia os dois é a tipografia do patch; `sf_001` tem também o problema de aspect.

## TIER 2 — Ancoragem de peça

**Nunca como referência de identidade** — o modelo das fotos de produto não é o talent.

| Slug | Caminho | Origem | Descrição | Status |
|---|---|---|---|---|
| `top_front_product` | `assets/wardrobe/top_front_product.webp` | `front.webp` (1024×1366) | Top manga longa, frente, em modelo de estúdio. Mostra corte raglan, gola, costura vertical central e o **patch do peito com tipografia legível**: `OH` sobre `USE ZERO HORA®` | ✅ importado |
| `patch_thigh_macro` | `assets/wardrobe/patch_thigh_macro.webp` | `006ebe…webp` (1024×1280) | Bermuda de neoprene, três-quartos lateral. Mostra a **etiqueta da coxa legível** (`OH \| USE ZERO HORA \| ≋`), a costura da barra e o volume do neoprene | ✅ importado |
| `bootie_sole_product` | `assets/wardrobe/bootie_sole_product.webp` | `64f99…webp` (1024×682) | **Sapatilha de neoprene**, vista da sola, solado texturizado, logo `OH` no cano | ⚠️ importado — **produto fora do escopo declarado**, ver achados |
| `patch_chest_macro` | `assets/wardrobe/` | — | Patch do peito, macro isolado | ❌ não enviado (parcialmente coberto por `top_front_product`) |
| `waist_drawcord` | `assets/wardrobe/` | — | Cordão interno do cós | ❌ não enviado |
| `top_back_construction` | `assets/wardrobe/` | — | Costas do top, raglan e gola | ❌ não enviado |
| `sleeve_side_panel` | `assets/wardrobe/` | — | Painel lateral da manga, recorte de poliamida | ❌ não enviado |
| `material_neoprene_body` | `assets/wardrobe/` | — | Textura do corpo da bermuda | ❌ não enviado (parcialmente coberto por `patch_thigh_macro`) |
| `material_open_cell_hem` | `assets/wardrobe/` | — | Textura da barra, open cell | ❌ não enviado (parcialmente coberto por `patch_thigh_macro`) |

## ARTE DE LOGO — derivada, canônica

Extraída das macros de produto por `tools/extract_logo_art.py` e vetorizada por `tools/vectorize_logo.py`.

| Arquivo | O que é | Origem |
|---|---|---|
| `assets/wardrobe/badge_chest_art.png` | Arte do badge do peito, 1000×1000 RGBA, branco sobre transparente, retificada e de pé | `_raw/LOGO-VERT.png` |
| `assets/wardrobe/badge_chest.svg` | Mesma arte em vetor, 24 paths, viewBox 1000×1000, `fill-rule="evenodd"` | idem |

**O que foi feito:** isolado o relevo branco por limiar, ajustada a elipse do anel externo — que é círculo perfeito no plano da peça e tem contraste muito melhor que a borda do disco —, mapeada para círculo, e corrigido o "de pé" pela posição angular das letras do arco.

**Símbolo ® redesenhado — única exceção, declarada.** Na macro o ® tem 42 px e a foto não resolve os traços do R: o limiar global quebrava o anel do lado escuro e deixava dois respingos soltos; limiar local fecha o anel, mas o miolo continua ruído e não ganha legibilidade. O ® é **símbolo universal padronizado** (círculo com R), não tipografia da marca — redesenhá-lo não é o mesmo que redesenhar `USE ZERO HORA`, que continua vindo integralmente da geometria medida. Diâmetro, espessura de traço, posição e inclinação ao longo do arco saem do próprio símbolo extraído; só a forma interna do R é desenhada.

**O que deliberadamente não foi feito:** nenhuma letra do wordmark foi reconstruída por aproximação tipográfica, e o anel traçado não foi substituído por círculo ideal. Fora o ®, tudo no SVG veio da geometria medida na macro.

**Limitação registrada:** o anel sai ~5% ovalado. A retificação é afim e o badge tem distorção projetiva real na foto; um único cônico não determina a homografia sem as intrínsecas da câmera. Não afeta o compositing, onde a elipse vem da geometria medida no próprio frame — afeta só o uso do SVG isolado em escala grande.

**Duas grafias, as duas corretas:** badge do peito = `USE ZERO HORA®`, com espaços e ®. Etiqueta da coxa = `USEZEROHORA`, tudo junto, sem ®, com o glifo de ondas `≋`. São lockups diferentes; não uniformizar um pelo outro.

## TIER 3 — Suporte de prompt apenas

**Nunca como referência de imagem em geração.**

| Slug | Descrição | Status |
|---|---|---|
| `infografico_etiqueta_emborrachada` | Fonte de verdade declarada pelo master prompt | ❌ não enviado — **substituído pelas macros `LOGO-VERT.png` e `LOGOS-HORI.png`, que são melhores: são o produto real, não diagrama** |

## `assets/scenario/`

Vazia. Nenhum plate de locação sem personagem enviado.

---

# Achados críticos do primeiro lote

## 1. Tipografia do patch — CORRIGIDA por compositing determinístico

O `achado_critico_logo` se materializou nos dois frames: o arco do peito saía como ruído (`9GEEN RACCB`), a etiqueta da coxa idem, e — achado que só apareceu com as macros em mãos — **o próprio `OH` do frame não era o monograma da marca**, eram duas letras soltas de uma sans qualquer. Não havia nada de aproveitável na marcação.

**Corrigido.** `tools/composite_logo.py`, zero crédito. Medições em `sf_002`, peito:

| | Original | Composto |
|---|---|---|
| Tinta, pico (p95) | 221,1 | 221,0 |
| Tinta, média | 148,4 | 163,6 |
| Fundo do disco | 54,5 | 61,3 |

Pixels alterados na imagem inteira: **0,26%** em `sf_002`, **0,21%** em `sf_001`.

**Como:** supressão da tinta velha por abertura morfológica (inpaint deixa borrão), reposição de textura com corte de outliers (sem o corte, gotas d'água do trecho de origem são carimbadas dentro do patch), e arte canônica entrando só como máscara de relevo — o brilho não é arbitrado, é medido no próprio frame pelo percentil 90 do excesso da tinta original, **por canal**, porque a tinta da peça é creme quente e ganho neutro devolve cinza.

**Defeito residual:** o fundo do disco fica ~7 níveis mais claro que o tecido vizinho, resquício da supressão. Tentativa de corrigir por viés medido foi reprovada — o anel de tecido limpo disponível dentro do disco cai no lado escuro do gradiente e a correção inverte de sinal, clareando em vez de escurecer.

## 1b. Registro do estado anterior

É o `achado_critico_logo` se materializando. Nos dois frames:

- **Patch do peito:** o `OH` sai legível, mas a linha de texto abaixo dele é ruído tipográfico, não `USE ZERO HORA®`.
- **Etiqueta da coxa:** ruído em ambos (`TS&S ENCLOSESHTA` e `UZS ZOOASDXZ` são leituras aproximadas do que aparece).

Se qualquer um desses frames virar frame de partida sem correção, o logo errado entra no frame 0 e se propaga por **todos** os frames do take. Não é corrigível em pós sem repintar quadro a quadro.

**Boa notícia:** o lote trouxe a fonte de verdade que faltava. `top_front_product.webp` e `patch_thigh_macro.webp` mostram as duas marcas com tipografia legível, e podem ser travadas como referência adicional ou usadas para recompor a área em pós.

## 2. Marca d'água do gerador — RESOLVIDO

Os PNGs traziam o ícone de brilho (sparkle) do gerador: **uma** marca em `sf_001`, **duas** em `sf_002` (a segunda passou despercebida na primeira leitura). Num frame de partida isso é pior que numa still — a marca entra no frame 0 e o modelo de vídeo tende a preservá-la e às vezes animá-la ao longo do take.

**Removidas.** Script versionado em `tools/remove_generator_watermark.py`, com os parâmetros e o racional no cabeçalho.

Método: a marca é uma sobreposição de branco com transparência constante, então é **invertível** — `bg = (obs − a·m·255)/(1 − a·m)`. Isso recupera a textura real do fundo em vez de inventar pixel. Os parâmetros foram medidos, não arbitrados: o expoente do astroide saiu 0,667 pela extensão diagonal, e o alpha 0,289 por dois estimadores independentes que concordaram (perfil por conchas de raio e degrau local cruzando a borda). Só a faixa de 3 px do contorno recebe inpaint, onde o antialias original não é reproduzível exatamente.

Área alterada: 0,10% dos pixels em `sf_001`, 0,16% em `sf_002`. Verificado em 1:1 — sem traço em `sf_001`, contorno residual imperceptível em `sf_002`.

Ressalva honesta: sobre a espuma clara de `sf_002` o estimador de alpha perde precisão, porque `255 − fundo` fica pequeno. O alpha das duas marcas dessa imagem foi fechado por inspeção visual em torno do valor medido em `sf_001` (0,30 e 0,28), não por medição direta.

## 3. Aspect ratio

`sf_001` é **3:4 retrato**. O shot list especifica **16:9 em todos os takes**. Usar 3:4 como frame de partida de um take 16:9 força crop ou outpaint, e nos dois casos a composição muda.

`sf_002` é **16:9 exato** (2752×1536). Aspect-wise, é o único pronto.

## 4. Os dois frames são do Setup A — T1 e T2 seguem sem material

Montanha enevoada no horizonte, mar aberto, luz rasante, personagem de frente para a câmera com olhar direto: é **Setup A**, composição de **T3**.

Não veio nada de **Setup B** (mata atlântica fechada ao fundo, backlight quente forte, personagem de perfil olhando fora de quadro) além do `face_001`. **T1 e T2 continuam sem frame de partida e sem âncora de corpo.**

## 5. Prancha contradiz o tracker de continuidade

O `docs/continuity_tracker.md` trava: single-fin de ~9'0"–9'2", cera bege/marrom desgastada no deck, **leash presa ao pulso/mão**.

Os dois frames mostram: prancha branca com **deck pad preto de tração na rabeta** (elemento de shortboard/mid-length, não de longboard single-fin clássico), e **leash saindo da rabeta e arrastando na água**, não presa ao pulso.

Isso é contradição direta, não variação. Precisa de decisão: ou o tracker é corrigido para descrever a prancha que aparece no material aprovado, ou o material precisa ser regerado. Manter os dois como estão garante quebra de continuidade em produção.

## 6. Barra da bermuda não lê como open cell nos frames

`patch_thigh_macro.webp` mostra a barra como banda distinta, mais espessa, com costura própria. Nos dois frames gerados a bermuda lê como peça lisa de compressão, sem a barra diferenciada. É exatamente a confusão entre os dois materiais que o master prompt marca como "erro de continuidade visível a olho treinado".

## 7. A tatuagem provavelmente é do modelo de produto, não do personagem

O dossiê registra "tatuagem escura na canela direita, visível abaixo da barra da bermuda em `body_003`" como marca de continuidade **do personagem**.

`patch_thigh_macro.webp` — que é foto de **produto**, cujo modelo o master prompt afirma explicitamente **não ser o talent** — mostra uma tatuagem na perna, abaixo da barra da bermuda. E `body_003` é descrito no próprio master prompt como um **diptique com detalhe de produto**.

Os dois frames gerados do personagem **não têm tatuagem nenhuma**.

Leitura mais provável: a tatuagem foi observada no lado de produto do diptique e atribuída ao personagem por engano. Se confirmado, sai do dossiê como marca de continuidade — o que também torna irrelevante a decisão de não descrevê-la no prompt.

## 8. Sapatilha de neoprene — DECIDIDO: catálogo de produto apenas

O `<contexto_da_campanha>` define a peça como **conjunto de duas partes**: top + bermuda. A sapatilha não aparece no master prompt, nem no shot list, nem no tracker.

**Decisão do usuário:** a sapatilha entra **apenas como catálogo de produto** neste momento. O personagem aparece **descalço em todos os takes**, como já está nos dois frames.

Consequências aplicadas:

- `bootie_sole_product.webp` permanece em `assets/wardrobe/` como Tier 2, para referência de produto e uso em material de catálogo.
- **Nunca entra como referência de figurino** em chamada de vídeo da Onda 1.
- "Pés descalços" vira item travado no `docs/continuity_tracker.md` — calçar o personagem em qualquer take passa a ser quebra de continuidade, não variação.
