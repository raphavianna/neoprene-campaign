# R2 — Encontro com a câmera · briefing para rodar direto no Higgsfield

Use isto para reproduzir o take pela interface, sem passar por esta sessão.
O job equivalente já rodado por MCP é o `b88358a2-8b09-436b-aaa0-c428157d05c6`, 52 créditos.

## Configuração

| Campo | Valor |
|---|---|
| Modelo | **Seedance 2.5** |
| Modo | **Omni reference** (porque há start frame + referências) |
| Duração | **8s** |
| Resolução | **720p** |
| Aspect ratio | **16:9** |
| Áudio | **ligado** |
| Variantes | 1 |

**Se aparecer a sugestão de preset "IN THE DARK", recuse.** Ela sobrescreve a bíblia de câmera e luz do projeto — 85mm, f/2.8, Portra 400, obturador 180°.

## Imagens a anexar — três, com papéis distintos

### 1 · Start frame (papel: *start image*)
`assets/start_frames/sf_002_setup_a_plano_medio_16x9.png` — 2752×1536

É o take inteiro nascendo daqui. Já está sem marca d'água e com o badge do peito e a etiqueta da coxa **compostos com a arte canônica**. Anexar qualquer outra versão reintroduz o logo adulterado.

https://github.com/raphavianna/neoprene-campaign/blob/claude/ativar-workflow-projeto-axprrl/assets/start_frames/sf_002_setup_a_plano_medio_16x9.png

### 2 · Referência de identidade — rosto (papel: *image reference*)
`assets/identity/face/face_001.png` — 1024×1024

https://github.com/raphavianna/neoprene-campaign/blob/claude/ativar-workflow-projeto-axprrl/assets/identity/face/face_001.png

### 3 · Referência de identidade — corpo (papel: *image reference*)
`assets/identity/body/body_002_setup_a_retrato.png` — 1792×2390

https://github.com/raphavianna/neoprene-campaign/blob/claude/ativar-workflow-projeto-axprrl/assets/identity/body/body_002_setup_a_retrato.png

As duas últimas cumprem a regra de identity lock do master prompt: em plano médio ou mais próximo, sempre uma de rosto **e** uma de corpo.

**Não anexar:** as fotos de produto (`top_front_product`, `patch_thigh_macro`, `bootie_sole_product`). O modelo delas não é o talent — entrariam como referência de identidade e trocariam o personagem.

## Prompt — copiar inteiro

Está em `prompt_en.md`, no mesmo diretório. 3.447 caracteres, dentro do teto de 3.500.

## O que conferir no resultado

1. **Tipografia do patch ao longo dos 8s.** O frame 0 está correto; o risco é o modelo redesenhar o texto adiante. É o item mais crítico.
2. Poliamida fosca e colada contra neoprene com brilho de borracha e mais volume — dois materiais, não um.
3. Cabelo em mechas agrupadas, nunca blob uniforme.
4. Pés descalços e prancha sob o braço direito.
5. Água sem respingo acima da metade da canela; gotas com peso real.
6. Grão irregular e clumpy, não ruído digital uniforme.
