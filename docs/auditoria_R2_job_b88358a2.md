# Auditoria técnica — R2, job `b88358a2`

Vídeo: 1280×720, 24.000 fps, 193 frames, 8.04s, 16:9. Custo 52 créditos.

---

## Veredito

**REPROVADO.** Não por qualidade de imagem — que é alta — mas porque **o frame de partida foi ignorado pelo modelo**, e com ele todo o trabalho de correção do logo.

---

## O achado que domina tudo

**O frame 0 do vídeo não é o frame de partida enviado.**

| Medida | Valor |
|---|---|
| Pixels com diferença > 8 níveis | **90,4%** |
| Diferença média por pixel | 38,6 |
| Correlação global | **0,45** |

Não é reamostragem nem recompressão: é outra imagem. Mesmo personagem, mesmo figurino, mesma praia — mas enquadramento, posição do corpo, padrão das ondas e distribuição de luz recompostos do zero.

**Causa provável:** no modo `omni_reference` do Seedance 2.5, o papel `start_image` foi colapsado junto com as demais referências. O eco dos parâmetros do job confirma: as três imagens voltaram agrupadas em `reference_images`, sem distinção de papel.

**Consequência:** o badge e a etiqueta compostos deterministicamente no frame de partida **não propagam**. O modelo redesenhou as marcas por conta própria — e o erro de tipografia voltou.

## Marca do peito — alucinada de novo

O monograma `OH` sai aproximado, não correto. O arco que deveria ler `USE ZERO HORA®` volta a ser ruído tipográfico, e **muda de forma frame a frame** — variação média de 5,31 níveis na região entre frames consecutivos, pico de 11,28.

## Etiqueta da coxa — pior que o peito

Em 1,0s e 2,0s a estrutura aparece (monograma, divisória, texto, divisória, ondas) mas o texto é ilegível. **A partir de 3,0s a etiqueta desaparece por completo.** Isso não é só erro de tipografia: é quebra de continuidade dentro do mesmo take.

---

## O que passou — e passou bem

| Item | Medida | Veredito |
|---|---|---|
| Formato | 1280×720, 16:9, 24.000 fps, 8,04s | ✅ bate com o brief |
| **Grão** | correlação do padrão entre frames: **−0,007** | ✅ muda a cada frame, como filme. Não é padrão fixo nem ruído digital estático |
| **Flicker temporal** | desvio 0,29 sobre luminância média 142,6 | ✅ praticamente nulo |
| **Motion blur** | variância do laplaciano oscila **95%** com o movimento | ✅ obturador coerente, blur acompanha a ação |
| **Mãos** | cinco dedos, anatomia correta, sem fusão nem dedo extra | ✅ |
| **Identidade** | estável nos 8s, consistente com `face_001` | ✅ |
| **Pele** | poros e barba rala visíveis no close final | ✅ |
| **Peça de duas partes** | top e bermuda distinguíveis, barra visível | ✅ |
| **Pés descalços** | sim | ✅ conforme decisão de escopo |
| **Prancha** | sob o braço direito, leash presente | ✅ |
| **Água** | sem respingo acima da canela | ✅ |
| **Céu e locação** | montanha enevoada, sem nuvem dramática | ✅ Setup A mantido |

Ressalva menor: aos 7,0s ele abre a boca num respiro. O brief pedia expressão neutra-séria e uma piscada — a boca aberta não foi pedida e destoa. Aos 8,0s volta ao neutro correto.

---

## Como resolver

O problema não é o prompt. É o **modo de geração**.

**1 — Testar `omni_reference` com o start frame sozinho.** A hipótese é que múltiplas referências colapsam os papéis. Enviar só o frame de partida, sem `face_001` nem `body_002`, custa 52 créditos e responde a pergunta de forma definitiva. O identity lock não se perde: o próprio frame de partida já carrega rosto e corpo do personagem.

**2 — Trocar por um modelo com image-to-video literal.** `minimax_h3` trabalha com keyframes, `kling3_0` com transferência de movimento. Se algum honrar o primeiro frame, o composite passa a valer.

**3 — Aceitar a re-renderização e neutralizar.** Gerar com a área do logo limpa e compor a marca em pós, frame a frame, com rastreamento. Determinístico e à prova de alucinação, mas é trabalho de composição por quadro.

**Recomendação:** o teste 1 primeiro. É barato, e se confirmar a hipótese resolve o problema inteiro sem trocar de modelo nem entrar em composição por quadro.

---

## Para rodar direto na interface do Higgsfield

Mesmo prompt e mesmas configurações do `briefing_manual.md`, com **uma mudança**: anexar **somente o frame de partida** no papel de start image, sem as duas referências de identidade. Se a interface separar explicitamente "start frame" de "reference images", usar essa separação e conferir no resultado se o primeiro frame do vídeo é idêntico ao anexado.
