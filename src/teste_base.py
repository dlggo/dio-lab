import json
from pathlib import Path

import pandas as pd


# ============================================================
# CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


# ============================================================
# CARREGAMENTO
# ============================================================

transacoes = pd.read_csv(
    DATA_DIR / "transacoes.csv"
)

historico_atendimento = pd.read_csv(
    DATA_DIR / "historico_atendimento.csv"
)

with open(
    DATA_DIR / "perfil_investidor.json",
    "r",
    encoding="utf-8"
) as arquivo:
    perfil_investidor = json.load(arquivo)

with open(
    DATA_DIR / "produtos_financeiros.json",
    "r",
    encoding="utf-8"
) as arquivo:
    produtos_financeiros = json.load(arquivo)


# ============================================================
# TESTES
# ============================================================

print("=" * 50)
print("TESTE DA BASE DE CONHECIMENTO")
print("=" * 50)

print("\n[1] TRANSAÇÕES")
print(transacoes)

print("\n[2] HISTÓRICO DE ATENDIMENTO")
print(historico_atendimento)

print("\n[3] PERFIL DO INVESTIDOR")
print(json.dumps(
    perfil_investidor,
    ensure_ascii=False,
    indent=2
))

print("\n[4] PRODUTOS FINANCEIROS")
print(json.dumps(
    produtos_financeiros,
    ensure_ascii=False,
    indent=2
))

print("\n" + "=" * 50)
print("BASE CARREGADA COM SUCESSO!")
print("=" * 50)