# neoprene-campaign

Produção de vídeo ultra-realista para **OH | Use Zero Hora** — linha de neoprene/beachwear. Ensaio de surf na Praia de Maresias, litoral norte de SP. Motor de geração: Seedance 2.0 via MCP Higgsfield, dentro do sistema `[HIGG] - Creative`.

O `CLAUDE.md` na raiz é a **fonte de verdade** do projeto: identidade do agente, contexto da campanha, bíblias, shot list, framework de prompt e regras de aprovação. Os arquivos em `docs/` são extrato de consulta rápida — em caso de divergência, vale o `CLAUDE.md`.

## Estado atual

**Fase 0 (bootstrap) concluída. Aguardando aprovação para a Fase 1.**
Zero créditos consumidos. Nenhuma chamada ao Higgsfield feita até aqui.

| Fase | O que é | Status |
|---|---|---|
| 0 — Bootstrap | Estrutura de repo, bíblias extraídas, assets catalogados | ✅ concluída (com pendência de upload de assets) |
| 1 — Shot list | Onda 1 aprovada, risco de logo decidido por take, Onda 2 formalmente decidida | ⏸ proposta em `docs/shot_list.md`, aguardando aprovação |
| 2 — Prompt Seedance | Prompt EN por take, blocos travados, teto de 3500 caracteres | ⛔ não iniciada |
| 3 — Execução + quality gate | Preflight de custo, aprovação explícita, checklist anti-AI | ⛔ não iniciada |
| 4 — Arquivamento | `prompt_en.md`, `job_metadata.json`, vídeo, commit, push | ⛔ não iniciada |

### Bloqueadores conhecidos

1. **Nenhum asset no repositório.** As pastas de `assets/` estão criadas e vazias. A identidade do personagem é ancorada por referência de imagem direta em cada chamada (não há Soul Character treinado) — sem os arquivos Tier 1, nenhum take pode ser gerado. **Para subir: `docs/como_subir_assets.md`.** Para o destino de cada arquivo: `docs/asset_inventory.md`.
2. **Decisões de risco de logo em aberto** para T1, T3 e T4 — precisam ser tomadas take a take antes da execução.
3. **Onda 2 sem decisão formal** — seguir sem referência, aguardar material, ou cortar do escopo.

## Estrutura

```
neoprene-campaign/
├── README.md               ← você está aqui
├── CLAUDE.md               ← master prompt v2.0, fonte de verdade
├── assets/
│   ├── _raw/               ← originais preservados antes de renomear
│   ├── identity/{face,body}/   ← Tier 1, ancoragem de identidade
│   ├── wardrobe/           ← Tier 2, ancoragem de peça
│   ├── scenario/           ← plates de locação, praia sem personagem
│   ├── start_frames/       ← primeiro frame literal de um take
│   └── support_marketing/  ← Tier 3, suporte de prompt apenas
├── jobs/
│   ├── stills/
│   └── video/take_<NN>_<slug>/{prompt_en.md,job_metadata.json,output.mp4}
└── docs/
    ├── como_subir_assets.md  ← onde colocar cada imagem
    ├── shot_list.md
    ├── character_bible.md
    ├── cinematography_bible.md
    ├── location_bible.md
    ├── continuity_tracker.md
    ├── asset_inventory.md
    ├── anti_ai_checklist_log.md
    ├── changelog.md
    └── history/            ← versões anteriores do master prompt
```

## Como retomar

1. Abrir uma sessão do Claude Code apontada para este repositório — o `CLAUDE.md` carrega sozinho.
2. Ler este README e `docs/changelog.md` para o estado corrente.
3. Se houver assets novos, importá-los primeiro para `assets/_raw/` e só então renomear para o tier de destino, atualizando `docs/asset_inventory.md`.
4. Retomar na primeira fase marcada como não concluída na tabela acima, respeitando o ciclo de aprovação: **da Fase 2 em diante, cada take é seu próprio ciclo** — não empacotar múltiplos takes numa aprovação só.

## Regras que não se negociam

- Zero geração no Higgsfield sem aprovação explícita de prompt **e** custo.
- Preflight (`get_cost: true`) antes de cada chamada; todo job aprovado documentado.
- Checklist anti-AI aplicado antes de aceitar qualquer output; take reprovado vai para `docs/anti_ai_checklist_log.md` com o motivo, nunca é arquivado como aprovado.
- Balance abaixo de 10% do plano → avisar antes de continuar.
- Onda 2 (bloco de ação) nunca inicia sem decisão formal separada.
