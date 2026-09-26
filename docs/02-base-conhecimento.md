# Base de Conhecimento — BIA do Futuro

## 1. Visão Geral

A BIA do Futuro utiliza uma base de conhecimento local composta por arquivos
CSV e JSON.

Esses arquivos armazenam as informações utilizadas pelo agente para responder
às perguntas do cliente.

Atualmente, a base de conhecimento é composta por:

- `data/transacoes.csv`
- `data/historico_atendimento.csv`
- `data/perfil_investidor.json`
- `data/produtos_financeiros.json`

O agente não realiza consultas externas para obter essas informações.
Os dados são carregados localmente pelo arquivo `src/agente.py`.

---

## 2. Estrutura da Base

```text
data/
├── transacoes.csv
├── historico_atendimento.csv
├── perfil_investidor.json
└── produtos_financeiros.json
