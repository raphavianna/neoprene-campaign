# R2 — Encontro com a câmera · para colar direto no Higgsfield

## Configuração

| Campo | Valor |
|---|---|
| Modelo | **Seedance 2.5** — o 2.0 não existe mais no catálogo |
| Modo | **Omni reference** |
| Duração | **8s** |
| Resolução | **720p** |
| Aspect | **16:9** |
| Áudio | **ligado** |
| Variantes | 1 |

Se aparecer sugestão do preset **"IN THE DARK", recuse** — ele sobrescreve a bíblia de câmera e luz.

## Imagens a anexar

**Uma só: o frame de partida.**

`assets/start_frames/sf_002_setup_a_plano_medio_16x9.png` — 2752×1536

Na primeira geração eu anexei três imagens (frame de partida + rosto + corpo) e o modelo colapsou os papéis: tratou tudo como referência genérica, recompôs o plano do zero e redesenhou o logo. Com uma imagem só, a ambiguidade de papel desaparece.

**Não anexe** `face_001` nem `body_002` — o próprio frame de partida já carrega rosto e corpo do personagem, então o identity lock não se perde.

**Não anexe** as fotos de produto. O modelo delas não é o talent; entrariam como referência de identidade e trocariam o personagem.

## Prompt

```
Continue forward from the provided start frame. Do not recompose the shot: the first frame of the video must match the provided image exactly, including framing, subject position, wave pattern and the printed marks on the garment.

MODEL / CAMERA
85mm full-frame equivalent, f/2.8, eye level, handheld with micro-stabilisation that breathes with the operator's step. 24fps, 180-degree shutter.

SUBJECT
Man in his early thirties, tanned olive skin, lean athletic swimmer's build, defined jaw, short few-day stubble, brown eyes, short brown hair soaked into separated clumped strands stuck to forehead and nape, never a smooth uniform mass. Natural skin texture, visible pores in close-up, realistic micro-expressions. Gaze locked to the lens, expression neutral and serious, no smile, mouth closed throughout.

WARDROBE
Black long-sleeve UV50 polyamide top, thin, matte, clinging. Black neoprene shorts with thicker cuffs at the leg hems reading as wet rubber. The circular chest badge and the rectangular thigh label are already printed correctly in the start frame: keep them identical in shape, size, position and lettering for the whole shot, and keep the thigh label visible and unchanged, never fading out.

ACTION
0-2s: two unhurried steps directly toward camera through ankle-deep wash, board under his right arm, torso steady.
2-4s: a droplet gathers and runs off his lowered left hand and falls; foam slides back around his feet.
4-6s: two more steps, closer; the wet polyamide shifts across his chest with the stride, hair strands move as a group.
6-8s: pace continues, direct gaze held, one slow blink, shoulders settling on the exhale.
Shallow wash around the ankles, no splash above mid-shin, droplets falling with real weight.

SCENE
Maresias beach, north coast of Sao Paulo, golden hour. Distant hazy mountain silhouette, open sea, medium shorebreak with continuous white foam, moderate ebbing tide, clear to slightly hazy sky, beach empty of other people.

LOOK
Motivated lighting from the low sun only, raking and cool within the golden hour window. Kodak Portra 400 emulation, moderate contrast, blacks lifted rather than crushed, skin tones protected.

LENS
Photorealistic, shot on 85mm. Slight halation on wet shoulders, lens artifacts, subtle film grain that is irregular and clumpy rather than uniform digital noise. Shallow depth of field, mountain and sea softly out of focus.

CAMERA CONSTRAINTS
The camera holds one handheld take at eye level, keeps the subject centred, holds its distance so he grows in frame by his own movement, and keeps the same shutter and focal length throughout.

AUDIO
Distant shorebreak, steady light wind, wet footsteps in shallow water. No music, no voices.
```

## O que mudou em relação ao prompt da primeira geração

1. **Abre travando o frame 0.** A primeira linha manda não recompor e casar o primeiro frame com a imagem anexada. Antes essa instrução estava enterrada no bloco de estrutura.
2. **"mouth closed throughout"** — na primeira geração ele abriu a boca aos 7s sem ter sido pedido.
3. **"keep the thigh label visible and unchanged, never fading out"** — a etiqueta da coxa sumia a partir dos 3s.
4. Menos redundância nos blocos de identidade, já que agora só existe uma referência.

## O primeiro item a conferir no resultado

**O frame 0 do vídeo é idêntico à imagem que você anexou?**

Se não for, o modelo ignorou o frame de partida de novo, e nenhum ajuste de prompt resolve — o caminho passa a ser um modelo cujo único papel de mídia é `start_image`, que estruturalmente não tem como colapsar papéis: `kling3_0_turbo`, `veo3` ou `happy_horse_video`.

Depois disso: tipografia do patch ao longo dos 8s, etiqueta da coxa sem sumir, dois materiais distinguíveis, mechas agrupadas, pés descalços, prancha no braço direito.
