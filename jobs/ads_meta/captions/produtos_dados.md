# Dados de produto — linha Neoprene (fonte de verdade para legendas + destino dos ads)

Fonte parcial recuperada **sem token**, do repo `zerohora-painel` (GA4 `analytics.json`,
janela 2025-08-11 → 2026-08-11, propriedade 469097391) e `vendas.json`. A linha é
**lançamento** (views mas ~0 compras), então catálogo/preço/URL não estão nas bases;
dependem do ERP (BaseLinker) ou Nuvemshop.

## Confirmado (GA4)
| Produto (nome comercial exato) | Cor | Tamanhos vistos | Sinal ago/26 | Preço | URL destino |
|---|---|---|---|---|---|
| **CAMISETA NEOPRENE CABO FRIO** | Preto | P (+?) | 62 views, 0 compra | ⟨falta⟩ | ⟨falta⟩ |
| **SAPATILHA ESPORTIVA NEOPRENE** | Preto | 34 a 37 (+?) | 30 views, 0 compra | ⟨falta⟩ (ref. venda avulsa R$ 78,98) | ⟨falta⟩ |
| **BERMUDA NEOPRENE** ⟨nome a confirmar⟩ | Preto | ⟨falta⟩ | sem página/views no GA4 | ⟨falta⟩ | ⟨falta⟩ |

## Contexto de marca/linha (para copy)
- Material: neoprene **1,5 mm** (top em poliamida UV50 + corpo/barra neoprene, ver CLAUDE.md).
- Naming sugere posicionamento água fria: "CABO FRIO". Casa com tagline "FEITO PARA A ÁGUA FRIA".
- Demanda já existente: 30 buscas internas por "NEOPRENE"; Paid Search e e-mail de lançamento ativos.

## O que ainda falta e de onde vem
- **Preço, tamanhos completos, SKU, URL de destino** e **nome da bermuda**:
  - via **BaseLinker** `getInventoryProductsList/Data` (token = secret `BASELINKER_API_TOKEN`, não exposto aqui), ou
  - via **Nuvemshop** (`scripts/pull-products.mjs`, precisa `STORE_ID`+`ACCESS_TOKEN`; store id informado: **38816**), ou
  - **paste manual** do Raphael (3 linhas: preço + tamanhos + URL por produto + nome da bermuda).
- URL de destino é o único item **obrigatório** para o anúncio de conversão (não dá pra inventar link).
