# Tracker de continuidade — neoprene-campaign

> Extrato de consulta. Fonte de verdade: `CLAUDE.md` → `<tracker_de_continuidade>`.
> Aplica-se a todo take do **Bloco de Retorno (Onda 1)**. Cada linha é um estado que não pode contradizer o take anterior nem o seguinte na sequência aprovada.

## Regras travadas

**Prancha**
Single-fin, ~9'0"–9'2", **mesmo exemplar físico em todos os takes**: cera bege/marrom desgastada no deck, amarelamento leve nos rails. Não trocar o padrão de desgaste entre takes. Leash escura, presa ao pulso/mão quando ele caminha (não ao tornozelo nestes planos, conforme referência) — nunca duplicar o ponto de fixação de forma inconsistente.

**Cabelo**
Molhado em todos os takes da Onda 1, mechas agrupadas e definidas. A intensidade de gotejamento pode **reduzir** progressivamente do take mais próximo da água para o mais afastado — nunca aumentar nessa direção.

**Tecido**
Sheen de água máximo próximo da arrebentação, secando visualmente de forma sutil e progressiva conforme o personagem se afasta da água. Nunca abrupto entre um take e o seguinte. Lembrar que são dois materiais com física distinta: poliamida UV50 (brilho baixo) no top, neoprene 1,5mm (brilho de borracha molhada) na bermuda.

**Pele**
Gotas visíveis em braços e rosto próximo da água, reduzindo de forma consistente com o tecido.

**Pés — descalço**
Personagem **descalço em todos os takes**. A sapatilha de neoprene existe como produto e está catalogada em `assets/wardrobe/bootie_sole_product.webp`, mas por decisão do usuário entra **apenas como catálogo de produto** nesta fase e não como figurino. Calçar o personagem em qualquer take da Onda 1 é quebra de continuidade, não variação. A sapatilha também não entra como referência de imagem em chamada de vídeo.

## Estado por take

Preencher na aprovação de cada take (Fase 4). Sem take produzido até aqui.

| Take | Setup | Estado do cabelo | Sheen de tecido | Gotas na pele | Prancha / leash | Job ID | Status |
|---|---|---|---|---|---|---|---|
| T1 — Transição na arrebentação | B | pico de molhado, gotejamento visível | máximo | máximo | braço esquerdo, leash no pulso | — | não produzido |
| T2 — Caminhada observacional | B | molhado, gotejamento < T1 | alto | reduzindo | braço esquerdo, leash balançando | — | não produzido |
| T3 — Encontro com a câmera | A | molhado, mechas definidas, mais assentado | discreto | gota escorrendo da mão | braço direito | — | não produzido |
| T4 — Insert de detalhe (opcional) | — | n/a | molhado (macro) | n/a | prancha molhada em macro | — | não produzido |

---

# Contrato de continuidade da Onda 1 revisada

A cadeia R1 → R2 é um **corte entre dois setups**, não uma continuação de frame. Não existe continuidade de pixel a atravessar: existe continuidade de **estado**. As condições abaixo são o que faz o corte fechar.

## O que muda de R1 para R2, e em que direção

| Eixo | R1 (Setup B, close) | R2 (Setup A, plano médio) | Direção obrigatória |
|---|---|---|---|
| Molhado | pico da sequência — gotas correndo pelo maxilar e pescoço, uma pendurada na ponta de mecha | ainda molhado, sheen mais discreto | **só pode diminuir** |
| Luz | contraluz quente por trás e à esquerda, halação forte na água | rasante e mais fria, sombras longas | de quente para frio |
| Fundo | mata atlântica desfocada, sem linha de horizonte | mar aberto, montanha enevoada | B fica mais perto da água |
| Olhar | fora de quadro, à direita | direto na lente | R1 desvia, R2 encara |
| Movimento | parado; giro de cabeça iniciado e **cortado em 3,12s antes de completar** | caminhando de encontro à câmera | o giro de R1 **motiva** o corte |
| Figurino | idêntico | idêntico | sem variação |
| Boca | **entreaberta**, coerente com o `face_001` que ancora o take | fechada | corrigido após a auditoria do R1 |

## Por que o corte funciona

R1 termina com ele começando a virar em direção à lente e o peso indo para a frente. O movimento **não se completa em quadro** — completa-se no corte. R2 entra com ele já caminhando e já olhando. É corte por ação iniciada, não por posição igual, e é isso que dispensa continuidade de pixel entre dois pontos diferentes da praia.

## O que invalida a cadeia

- R1 sair menos molhado que R2.
- R1 com luz rasante fria em vez de contraluz quente.
- Horizonte ou mar visível em R1 — o fundo de R1 é mata, e mar em quadro colocaria os dois takes no mesmo ponto.
- Qualquer deslocamento de corpo em R1 além da transferência de peso final.
- Boca aberta no R2. No R1 a boca entreaberta é a referência, não um defeito.

## Medição do estado final do R2

Último frame do job `b88358a2`, 8,00s: close de peito para cima, olhar direto, boca fechada, Setup A com montanha à direita e arrebentação atrás. Prancha no canto inferior esquerdo. É esse o estado que qualquer take posterior a R2 tem de herdar.
