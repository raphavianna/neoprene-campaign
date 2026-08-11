# Auditoria técnica — R1, job `8aa3bdbd`

1280×720, 24.000 fps, 97 frames, 4.04s, 16:9. Custo 26 créditos.

## Veredito

**APROVADO COM CORTE EM 3,12s.** Duas notas de especificação, nenhuma delas defeito de realismo.

---

## O teste que importava: o frame de partida foi honrado

| | R2 (`b88358a2`) | **R1 (`8aa3bdbd`)** |
|---|---|---|
| Imagens anexadas | 3 | **1** |
| Pixels com diferença > 8 | 90,4% | **47,9%** |
| Correlação global | 0,45 | **0,88** |
| Recompôs o plano? | sim | **não** |

**A hipótese estava certa.** Com uma imagem só, o modelo mantém enquadramento, posição da cabeça e fundo. A diferença de 47,9% que resta é re-renderização de detalhe, não recomposição — a correlação de 0,88 e a inspeção visual confirmam.

Isso valida a correção de método para todos os takes seguintes: **uma imagem por chamada**.

## Continuidade com o R2 — os critérios invalidantes

| Critério do contrato | Resultado |
|---|---|
| Sem linha de horizonte, sem mar no fundo | ✅ mata desfocada em todo o take |
| R1 mais molhado que R2 | ✅ **405 especulares** no rosto contra **118** do R2 — cerca de 3,4× |
| Sem deslocamento de corpo | ✅ só o giro de cabeça e a transferência de peso |
| Câmera travada | ✅ ver abaixo |

**Câmera — a primeira medição estava errada e foi corrigida.** Rastreando pontos em todo o quadro dava 86,7px de deslocamento, o que sugeriria uma câmera que viaja. Rastreando **só o fundo**, o deslocamento é de **−0,7px em x e −3,9px em y em 4 segundos**. Os 86,7px eram o movimento do sujeito, não da câmera. A câmera está travada, como pedido.

## Medições anti-AI

| Item | Medida | Veredito |
|---|---|---|
| Flicker | desvio 0,203 sobre luminância 115,1 | ✅ praticamente nulo |
| Motion blur | laplaciano 65–186, amplitude 82% | ✅ varia com o movimento |
| Identidade | estável, consistente com `face_001` | ✅ |
| Pele | poros, barba rala, gotas com trajetória e velocidade desiguais | ✅ |
| **Grão** | **inconclusivo neste enquadramento** | ⚠️ ver abaixo |

**Grão: a medição não conclui, e é honesto dizer isso.** Na região lisa disponível — o céu estourado do canto superior esquerdo — o desvio é 0,33 com correlação de 0,502 entre frames. Mas céu estourado satura e perde grão por definição, então o número não prova ausência. A medição global dá 4,85 com correlação +0,32, contaminada pela textura estática da mata desfocada, que persiste entre frames por ser cenário parado, não por ser padrão fixo de ruído.

No R2 a medição concluiu (2,79, correlação −0,007) porque havia água e areia em movimento oferecendo região de teste limpa. Aqui não há. **Fica registrado como não verificado, não como aprovado.**

---

## Nota 1 — o giro de cabeça completou em quadro

Pedi que ele **começasse** a virar e que o movimento se completasse no corte. Ele completou dentro do take:

| Frame | Tempo | Estado |
|---|---|---|
| 54 | 2,25s | olhar fora de quadro, à direita |
| 63 | 2,62s | ainda fora de quadro |
| **72** | **3,00s** | **meio giro, olhar ainda não travado, boca já fechada** |
| 81 | 3,38s | quase frontal |
| 90 | 3,75s | frontal, olhar na lente |
| 96 | 4,00s | frontal pleno |

Se o take inteiro entrar na montagem, **o encontro com a câmera acontece duas vezes** — uma no fim do R1 e outra no R2 — e a virada do R2 perde a revelação. É exatamente o que o contrato de continuidade proíbe.

**Solução sem gerar nada: cortar o R1 em 3,12s (frame 75).** Ali a cabeça está a meio giro, o olhar ainda não travou na lente e a boca já fechou. O movimento passa a se completar no corte, como especificado. O take entrega 3,1s dos 4s gerados.

## Nota 2 — a boca aberta é erro meu de especificação, não do modelo

De 0 a ~2,6s ele está com a boca entreaberta. Meu prompt pedia "mouth closed and relaxed".

Mas o `face_001` — o frame de partida — **já tem a boca levemente entreaberta**, e isso está registrado no dossiê de personagem como característica da referência. Eu especifiquei contra a própria âncora, e o modelo seguiu a âncora.

Boca entreaberta em quem acabou de sair do mar depois de esforço é plausível e não é defeito de realismo. **O que precisa ser corrigido é o contrato de continuidade, não o take.**

---

## Ações

1. **Cortar o R1 em 3,12s na montagem.** Não requer nova geração.
2. **Corrigir o contrato de continuidade:** trocar "boca fechada nos dois takes" por "boca entreaberta em R1, coerente com `face_001`; fechada em R2".
3. **Método travado para os próximos takes:** uma imagem por chamada.
