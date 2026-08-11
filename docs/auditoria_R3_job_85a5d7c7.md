# Auditoria técnica — R3, job `85a5d7c7`

1280×720, 24.000 fps, 97 frames, 4.04s, 16:9, com trilha de áudio. Custo 26 créditos. Uma imagem anexada (`sf_004`), nenhuma referência adicional.

## Veredito

**APROVADO COM RESSALVA E CORTE EM 3s.** O take cumpre a única coisa que tinha de cumprir — a tipografia se mantém correta e legível nos 97 frames — e é exatamente onde o R2 falhou. Um defeito real de realismo (grão congelado), corrigível na montagem, não justifica re-roll.

---

## 1. O item que definia o take: a tipografia

Medida por **correlação de magnitude de gradiente**, que responde a forma e não a nível de luz — necessário porque este take tem um brilho varrendo as letras, e uma correlação de luminância crua confundiria especular com deformação.

| Região | mín | média | fim |
|---|---|---|---|
| Wordmark `USEZEROHORA` | 0,895 | **0,943** | 0,958 |
| Glifo de onda | 0,863 | **0,956** | 0,863 |
| Monograma `OH` | 0,528 | 0,815 | 0,868 |

Correlação do frame inicial contra o final na região da etiqueta: **0,9408**. Variação tipográfica entre frames: **média 0,50, pico 0,94** — contra o badge do R2, que alucinou a **5,31 de média e 11,28 de pico**. Uma ordem de grandeza de diferença.

**O mínimo de 0,528 no monograma não é deformação.** Ocorre num único frame (f18, 0,75s) em que o brilho médio da região sobe de 121 para 168 — estouro especular que satura o topo dos traços e mata o gradiente ali. Inspeção lado a lado de f0 / f18 / f96: geometria idêntica, mesma espessura, mesmo kerning, mesmo entrelaçamento do `O` com o `H`. É luz, não morfologia.

O wordmark lê `USEZEROHORA` corretamente do primeiro ao último frame, sem re-kerning, sem letra trocada, sem caractere inventado.

## 2. Frame de partida: composição honrada, luz reescrita

A medição crua assusta e é enganosa:

| | crua | após alinhamento |
|---|---|---|
| Pixels com diferença > 8 | 98,6% | — |
| Correlação | **0,216** | **0,603** |

O ECC afim que leva `sf_004` ao frame 0 é **escala 1,107 × 1,079, rotação 0,06°, translação −89 px**. Ou seja: o modelo **não recompôs** — manteve o enquadramento, o ângulo diagonal da etiqueta e a posição de cada elemento, com um leve *push-in* de 10%. O que ele reescreveu foi a **luz**: `sf_004` é uma macro de produto cinza e neutra; o frame 0 é dourado, com fonte quente no canto superior esquerdo.

**A causa é meu próprio prompt.** O bloco de abertura manda "the first frame of the video must match the provided image exactly" e o bloco LOOK manda "a single low warm source at the upper left, the same golden hour light as the rest of the sequence, Kodak Portra 400 emulation". As duas instruções são incompatíveis com uma referência cinza. O modelo obedeceu o LOOK.

**E fez a escolha certa editorialmente.** O R1 e o R2 são golden hour. Um insert cinza de catálogo não cortaria com eles. A relight é o que torna o take montável.

*Lição para os próximos prompts:* quando o frame de partida não estiver na luz da sequência, dizer isso explicitamente — "match the composition of the start frame; relight it to golden hour" — em vez de pedir correspondência exata e mudança de luz na mesma peça.

## 3. Câmera

Deriva de fundo em 4,04s: **+0,2 px em x, +0,2 px em y**. Travada, como pedido. Sem push-in, sem rack focus, sem reenquadramento.

A nitidez global oscila 97 → 158 (42% de amplitude), o que isolado sugeriria respiração de foco. Não é: a correlação entre nitidez global e brilho global é **0,968** — a oscilação é o especular entrando e saindo de quadro, não o foco se movendo. Numa região de borda dura fora do caminho do brilho a variação absoluta é de 3,6 a 7,4, nível de ruído.

## 4. O brilho percorre, ou a imagem pulsa?

**Percorre.** Centroide do brilho dentro da faixa de 550 px do wordmark: `209 → 100 → 445 → 245`. Amplitude de **361 px**, maior salto entre frames de 25,4 px — travessia contínua, sem teletransporte.

Ressalva de briefing: pedi uma varredura única da esquerda para a direita. O que veio foi esquerda → direita → volta parcial, duas inversões de direção. Não é defeito de realismo (uma fonte quente baixa com a peça se movendo produziria isso), é desvio de brief.

## 5. Grão — o defeito real

| Medida | Valor | Veredito |
|---|---|---|
| Desvio do grão no neoprene | 5,32 | amplitude plausível |
| **Correlação do padrão entre frames** | **+0,995** | ❌ **congelado** |

O grão existe espacialmente e está no lugar certo, mas é **o mesmo padrão em todos os 97 frames**. Grão de filme e ruído de sensor decorrelacionam quadro a quadro; um padrão estático por cima de um brilho que se move é assinatura de render, não de captura. É o item que mais entrega o take num monitor grande.

**Correção:** grão temporal na montagem. Não vale re-roll — o prompt já pede "subtle film grain that is irregular and clumpy rather than uniform digital noise" e o modelo entregou a distribuição espacial certa; o que falta é a dimensão de tempo, que se adiciona em pós com precisão maior do que se pede em prompt.

## 6. Demais itens anti-AI

| Item | Medida | Veredito |
|---|---|---|
| Flicker | 0,246 | ✅ desprezível |
| Motion blur | coerente com o obturador 180° | ✅ |
| Textura pontilhada do neoprene | preservada, não suavizada | ✅ |
| Bevel do relevo | lê em todos os frames, sem achatar | ✅ |
| Áudio | trilha `mp4a` presente | ✅ gerado |

## 7. Elemento inventado

Há uma **gota d'água grande sobre a face da etiqueta**, entre o divisor do monograma e o `USEZEROHORA`, que não está na referência. O prompt pedia uma gota no neoprene junto à borda inferior; o modelo pôs uma maior e em cima da peça.

Não é quebra: o estado molhado é o do arco inteiro, e a gota lê como física correta sobre borracha (menisco, especular no topo, sombra de contato). Fica registrada como invenção porque o take é um insert de produto e qualquer elemento não previsto sobre a marca é decisão, não acaso.

## 8. Continuidade

Insert macro, sem rosto, sem horizonte, sem pele. Não entra na cadeia de estado do tracker — não há gotejamento de personagem a herdar nem luz de setup a casar além da temperatura, que a relight já resolveu para o lado certo.

O que ele **precisava** herdar e herdou: a tipografia canônica. É a mesma arte que foi composta nos frames de partida do R2, agora fotografada em movimento sem se degradar.

## 9. Pendências

1. **Cortar para 3s** na montagem (shot list pede 3s; o mínimo do `seedance_2_5` é 4s).
2. **Grão temporal** em pós.
3. Ponto de entrada sugerido: a partir de ~0,9s, depois do estouro especular de f18, para abrir no meio da travessia do brilho e não na parte estática do primeiro segundo.
