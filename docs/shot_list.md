# Shot list — neoprene-campaign

> **Status:** Onda 1 **revisada** após o inventário real de assets. A versão original do master prompt está preservada mais abaixo, em "Onda 1 — proposta original".

---

# ONDA 1 REVISADA — o que o material sustenta

## Por que revisar

O shot list original pede uma progressão de três takes atravessando dois pontos da praia, e depende de quatro referências de corpo: `body_001`–`body_002` (Setup A) e `body_003`–`body_004` (Setup B).

O inventário real tem **duas** referências de corpo, ambas de **Setup A**, mais um retrato de **Setup B** (`face_001`). Não existe nenhuma referência de corpo em Setup B — logo T1 e T2, como escritos, não têm âncora. Forçá-los significaria o modelo inventar a locação inteira do Setup B a partir de descrição verbal, que é exatamente o risco que este projeto existe para eliminar.

A revisão abaixo usa **só o que existe**, e mantém a direção narrativa que o master prompt estabeleceu: o personagem vem do Setup B em direção ao Setup A, secando progressivamente.

## Os três takes

### R1 — Respiro · close · Setup B

- **Papel:** abertura. Estabelece o personagem e o Setup B sem precisar de plano de corpo.
- **Âncora e frame de partida:** `face_001` (1024×1024).
- **Estado físico:** pico de molhado — mechas agrupadas, gotas escorrendo do cabelo e do rosto.
- **Ação:** o personagem respira, gotas escorrem, olhar fora de quadro com micro-deriva. Sem deslocamento de corpo.
- **Luz:** Setup B, contraluz quente, mata desfocada ao fundo.
- **Câmera:** estática ou micro-deriva de respiração. Nada de trajetória, porque não há referência de corpo para sustentar movimento.
- **Duração:** 4s.
- **Risco de logo:** NULO — patch fora de quadro.
- **Áudio:** arrebentação próxima, vento.

### R2 — Encontro com a câmera · plano médio · Setup A

- **Papel:** o take principal. É o T3 do shot list original, sem alteração de intenção.
- **Âncora:** `body_001` + `body_002` + `face_001`. **Frame de partida:** `sf_002` (16:9 nativo).
- **Estado físico:** molhado, sheen mais discreto que R1 — coerente com estar mais longe da água.
- **Ação:** caminha de encontro à câmera, olhar direto, expressão neutra-séria, gota escorrendo da mão.
- **Luz:** Setup A, mais rasante e fria, montanha ao fundo.
- **Câmera:** 85mm equiv., f/2.8, handheld micro-estabilizado.
- **Duração:** 8s.
- **Risco de logo:** RESOLVIDO no frame de partida — badge e etiqueta já compostos com a arte canônica.
- **Áudio:** arrebentação de fundo mais suave, vento.

### R3 — Insert de produto · macro

- **Papel:** cutaway de edição.
- **Âncora e frame de partida:** `_raw/LOGO-VERT.png`, a macro real do badge sobre a peça.
- **Ação:** respiração mínima de câmera sobre o relevo de borracha, com brilho deslizando.
- **Câmera:** 100mm macro equiv., f/2.8, estática.
- **Duração:** 3s.
- **Risco de logo:** alto por definição, mas a âncora **é** o logo real fotografado — o risco se inverte a favor.

**Ordem de exibição:** R1 → R2, com R3 como cutaway. A direção Setup B → Setup A e o gotejamento decrescente do tracker de continuidade seguem válidos.

## Entrega de formato — o papel do `sf_001`

O `sf_001` não é um segundo momento narrativo: é o **mesmo take em enquadramento retrato**. Medido:

| Origem | 16:9 | 9:16 | 4:5 |
|---|---|---|---|
| `sf_002` (2752×1536) | **nativo** | perde 69% | perde 55% |
| `sf_001` (1792×2390) | perde 58% | **perde 25%** | **perde 6%** |

Ou seja: `sf_002` é o master horizontal, `sf_001` é o master vertical. O "problema de aspect" do `sf_001` deixa de ser defeito e vira função — ele atende Reels e TikTok sem crop destrutivo.

## O que sai de escopo nesta revisão

- **T1 e T2 originais** (Setup B, arrebentação e caminhada observacional): sem âncora de corpo. Ficam fora até existir material de Setup B.
- **Onda 2** (bloco de ação): já estava fora, e segue.

## Caminho para recuperar o arco completo

Se o arco de três takes atravessando os dois setups for desejado, o passo é gerar **dois stills novos de Setup B** — identidade ancorada em `face_001` + `body_001/002`, locação descrita pela bíblia —, aprová-los como `body_003` e `body_004`, e só então produzir T1 e T2.

Isso consome crédito de **imagem** antes de qualquer vídeo, e é ciclo de aprovação próprio. Não iniciado.

---

# Onda 1 — proposta original (preservada)


> Extrato de consulta. Fonte de verdade: `CLAUDE.md` → `<fase_1_shot_list_detalhado>`.

## Correção estrutural do arco (v2)

As quatro imagens de corpo registram **exclusivamente** o momento de saída da água — nenhuma mostra o personagem seco. Um bookend "entrada seca, mesma composição, direção invertida" forçaria um estado físico sem âncora fotográfica, exatamente o risco que este projeto existe para eliminar.

O material totalmente ancorado forma uma progressão de **um só momento**: o retorno à areia após a última onda, caminhando do **Setup B em direção ao Setup A**. Fecha com intenção (o personagem se aproxima e finalmente encara a câmera) em vez de repetir composição.

---

## ONDA 1 — BLOCO DE RETORNO

Totalmente ancorado, pronto para produção após aprovação. **Ordem de produção = ordem de exibição.**

### T1 — Transição na arrebentação

- **Papel:** primeiro momento da progressão, mais próximo da água.
- **Ancoragem:** `body_004` (Setup B).
- **Estado físico:** pico de molhado — sheen máximo, gotejamento visível, tecido colado ao corpo.
- **Ação segundo a segundo:** personagem emerge da espuma branca da arrebentação, prancha sob o braço esquerdo, dois a três passos atravessando água rasa em direção à areia, olhar para fora de quadro, luz de contorno forte por trás.
- **Locação / luz:** Setup B, backlight quente intenso, reflexo dourado na água rasa.
- **Câmera:** família "planos de caminhada" — 85mm equiv., f/2.8, handheld micro-estabilizado, altura dos olhos.
- **Duração / aspect:** 6s, 16:9.
- **Risco de logo:** MÉDIO — patch de peito parcialmente visível, plano não é close. *Decisão a confirmar antes da execução.*
- **Áudio:** arrebentação de fundo, vento leve, passos na água.

### T2 — Caminhada observacional

- **Papel:** meio da progressão, afastando-se da água.
- **Ancoragem:** `body_003` (Setup B) + detalhe de patch/prancha do mesmo diptique como referência auxiliar de wardrobe.
- **Estado físico:** molhado, gotejamento reduzindo em relação a T1.
- **Ação:** caminhada continua na faixa de areia molhada, prancha sob o braço esquerdo, leash balançando levemente, olhar ainda para fora de quadro, passo relaxado.
- **Locação / luz:** Setup B, mesma qualidade de luz de T1, levemente menos intensa se o plano for mais amplo.
- **Câmera:** família "planos observacionais" — 50mm equiv., f/4, estática com push-in muito lento.
- **Duração / aspect:** 8s, 16:9.
- **Risco de logo:** BAIXO — plano aberto.
- **Áudio:** arrebentação mais distante, vento.

### T3 — Encontro com a câmera

- **Papel:** fechamento da progressão, plano mais próximo e mais composto.
- **Ancoragem:** `body_001`, `body_002` (Setup A) + `face_001` para o rosto.
- **Estado físico:** ainda molhado mas sheen mais discreto, cabelo já mais assentado embora ainda com mechas definidas.
- **Ação:** personagem caminha diretamente em direção à câmera, olhar direto, expressão neutra-séria, prancha sob o braço direito, uma gota escorrendo visivelmente da mão em determinado momento (elemento já presente na referência).
- **Locação / luz:** Setup A, luz mais fria e mais rasante, montanha ao fundo.
- **Câmera:** família "planos de caminhada" — 85mm equiv., f/2.8, handheld micro-estabilizado.
- **Duração / aspect:** 8s, 16:9.
- **Risco de logo:** ALTO — plano médio frontal, patch em distância de leitura. *Decisão obrigatória antes da execução: travar referência de patch ou neutralizar para pós-produção.*
- **Áudio:** arrebentação de fundo mais suave (mais afastado da água), vento.

### T4 (opcional) — Insert de detalhe

- **Papel:** cutaway de edição, não narrativo.
- **Ancoragem:** crop de patch do peito (Tier 2, canônico) e crop de prancha das próprias referências de still.
- **Ação:** plano macro estático ou com respiração mínima de câmera sobre patch e textura da prancha molhada.
- **Câmera:** família "inserts" — 100mm macro, f/2.8, estática.
- **Duração / aspect:** 3–4s, 16:9.
- **Risco de logo:** ALTO por definição — é um close do patch. *Só produzir depois de T1–T3 aprovados e com a decisão de logo já validada num take anterior.*

---

## ONDA 2 — BLOCO DE AÇÃO

**Sem ancoragem fotográfica.** Não iniciar sem decisão explícita separada de Raphael — anexar referência adicional (foto ou vídeo do personagem surfando, mesmo de outra sessão) ou aceitar formalmente o risco maior de artefato de IA antes de qualquer prompt ser escrito.

- Remada e duck dive até o line-up.
- Manobra em onda (bottom turn / cutback).
- Retorno da última onda até o ponto onde T1 começa — esta é a **costura** entre as duas ondas, precisa fechar fisicamente com o estado de T1.
- Entrada seca no início da sessão, se este bookend for mesmo desejado — sem nenhuma referência de estado seco disponível hoje.

---

## Critério de saída da Fase 1

1. Onda 1 aprovada como shot list final.
2. Decisões de risco de logo tomadas **por take**.
3. Onda 2 formalmente decidida: seguir sem referência / aguardar material / cortar do escopo por ora.
