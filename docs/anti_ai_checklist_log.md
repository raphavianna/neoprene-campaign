# Log do quality gate anti-AI — neoprene-campaign

Registro de **toda** avaliação de output, aprovada ou reprovada. Take reprovado não é arquivado como aprovado — fica aqui com o motivo, porque histórico de falha calibra o próximo prompt.

Referência do checklist: checklist anti-AI de vídeo do `HIGG_SystemPrompt`, na íntegra, mais as camadas específicas desta campanha (`CLAUDE.md` → `<fase_3_execucao_e_quality_gate>`, item 5):

1. Fidelidade do patch conforme a decisão de logo do take.
2. Coerência de material entre poliamida (top, brilho baixo) e neoprene (bermuda, brilho de borracha molhada).
3. Aderência à família de lente/luz da bíblia de cinematografia.
4. Aderência ao tracker de continuidade contra o take anterior aprovado.

---

## Entradas

Nenhuma avaliação registrada. Nenhum job de vídeo executado — o projeto está na saída da Fase 0.

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
