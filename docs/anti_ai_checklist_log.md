# Log do quality gate anti-AI — neoprene-campaign

Registro de **toda** avaliação de output, aprovada ou reprovada. Take reprovado não é arquivado como aprovado — fica aqui com o motivo, porque histórico de falha calibra o próximo prompt.

Referência do checklist: checklist anti-AI de vídeo do `HIGG_SystemPrompt`, na íntegra, mais as camadas específicas desta campanha (`CLAUDE.md` → `<fase_3_execucao_e_quality_gate>`, item 5):

1. Fidelidade do patch conforme a decisão de logo do take.
2. Coerência de material entre poliamida (top, brilho baixo) e neoprene (bermuda, brilho de borracha molhada).
3. Aderência à família de lente/luz da bíblia de cinematografia.
4. Aderência ao tracker de continuidade contra o take anterior aprovado.

---

## Entradas

Nenhum job de vídeo executado. As entradas abaixo são de tratamento de asset, não de take.

### Fase 0 — neutralização isolada do badge do peito — REPROVADA

**O que se tentou:** apagar a marcação adulterada do badge (anel + `OH` + arco de texto) nos dois frames de partida, deixando tecido limpo para composição posterior — a rota que o `achado_critico_logo` prevê para risco alto.

**Duas implementações, as duas reprovadas:**

1. *Detecção local da tinta + inpaint TELEA nos traços.* Removeu a geometria, mas deixou a área **lisa**: o inpaint apagou a microtextura pontilhada do neoprene e sobrou um fantasma de disco liso no meio de tecido texturizado — mais denunciante que o próprio logo errado. Sobrou também um arco claro residual na borda esquerda.

2. *Abertura morfológica + reinjeção de microtextura clonada do tecido vizinho.* A supressão por abertura funcionou melhor que o inpaint, mas a clonagem de textura trouxe junto as **gotas d'água** da região de origem, carimbando gotas falsas dentro do badge. O logo virou um fantasma pontilhado escuro.

**Por que nenhuma fecha:** a marcação cobre uma fração grande do disco (~87 px de diâmetro), não é traço esparso. Removê-la exige *sintetizar* fabric novo com o gradiente de contraluz correto, a malha pontilhada correta e as gotas coerentes. Isso é síntese de textura, não retoque local — e todo método local deixa fantasma.

**Conclusão que muda o plano:** neutralizar era passo intermediário desnecessário. O badge correto ocupa **a mesma área** do errado, então compor a arte certa por cima **cobre** a marcação adulterada — não é preciso reconstruir tecido limpo embaixo. A neutralização isolada só se justificaria se a decisão fosse entregar a peça *sem* logo nenhum.

**Decisão:** rota abandonada, script descartado. Segue o compositing direto do badge correto, que depende das macros do logo entrarem no repo.

### Modelo de entrada

```
## <data> — take NN <slug> — job <job_id>
- Modelo / parâmetros:
- Decisão de logo aplicada:
- Checklist HIGG: (itens que falharam, ou "sem falha")
- Patch:
- Materiais (poliamida vs neoprene):
- Lente / luz vs bíblia:
- Continuidade vs take anterior:
- **Decisão:** aprovado | iterar prompt | trocar parâmetro | re-roll
- **Motivo:**
```
