# Dossiê de personagem — neoprene-campaign

> Extrato de consulta. Fonte de verdade: `CLAUDE.md` → `<dossie_de_personagem>`.
> Divergência entre este arquivo e o master prompt resolve-se sempre a favor do master prompt.

**Fonte visual:** `face_001`, `body_001` a `body_004`.
Tudo abaixo é visualmente confirmável nas referências — o que não é confirmável está marcado como tal, não inventado.

## Traços travados

| Atributo | Definição |
|---|---|
| Sexo / idade aparente | Homem, final da casa dos 20 a meados dos 30 anos. |
| Pele | Tom bronzeado/oliva, bronzeado de praia visível (contraste entre área coberta pela bermuda e pele exposta). Sem sardas proeminentes visíveis na resolução disponível. |
| Cabelo | Castanho, comprimento curto a médio. **Estado seco não documentado** — todas as referências mostram cabelo molhado, mechas agrupadas e definidas colando na testa e nuca, nunca efeito "blob" uniforme. |
| Rosto | Mandíbula definida, barba rala de poucos dias (stubble curto, não desenhada), sobrancelhas retas, olhos castanhos. |
| Físico | Compleição atlética magra, tipo nadador/surfista — ombros e dorso desenvolvidos, sem volume de hipertrofia pesada. |
| Altura / proporção | Sem referência de escala absoluta. Manter a proporção corporal exibida nas referências, não ajustar. |

## Marca de continuidade — tatuagem

Tatuagem escura na canela direita, visível abaixo da barra da bermuda em `body_003`. Desenho não determinável na resolução disponível.

**Decisão do usuário:** não entra na descrição verbal do prompt. A referência de imagem carrega essa informação nos takes onde a perna aparece. Em takes sem referência de perna direta, tratar como ausente sem risco — não é elemento de continuidade obrigatório. Não existe instrução de removê-la do resultado.

## Expressão por referência

- `body_001` / `body_002` — olhar direto para a câmera, expressão neutra-séria.
- `body_003` / `body_004` — olhar para fora de quadro, expressão neutra-relaxada.
- `face_001` — boca levemente entreaberta, olhar de três-quartos.

## Regra de identity lock

Não há Soul Character treinado. A identidade é ancorada por referência de imagem direta em cada chamada Seedance:

- **Plano médio ou mais próximo, personagem visível:** carregar pelo menos uma imagem de `face_001` **e** uma de `body_001`–`body_004`, mesmo que o enquadramento do take não seja idêntico ao das fotos.
- **Plano geral / distante:** referência de `body` é suficiente.

## Pendência aberta

Correção de cabelo iniciada e **não fechada** na sessão de still. Não usar como padrão de referência para o vídeo — é pendência aberta, não decisão tomada.
