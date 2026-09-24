import json
from pathlib import Path

import pandas as pd
from openai import OpenAI

from config import OPENAI_API_KEY, OPENAI_MODEL


# ============================================================
# CONFIGURAÇÃO
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Modelo utilizado pela BIA
MODEL = OPENAI_MODEL

# Cliente da OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)


# ============================================================
# CARREGAMENTO DA BASE DE CONHECIMENTO
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
# FUNÇÕES DE CONSULTA À BASE
# ============================================================

def consultar_transacoes():
    """Retorna as transações disponíveis."""
    return transacoes.to_string(index=False)


def consultar_historico():
    """Retorna o histórico de atendimento."""
    return historico_atendimento.to_string(index=False)


def consultar_perfil():
    """Retorna o perfil do investidor."""
    return json.dumps(
        perfil_investidor,
        ensure_ascii=False,
        indent=2
    )


def consultar_produtos():
    """Retorna os produtos financeiros disponíveis."""
    return json.dumps(
        produtos_financeiros,
        ensure_ascii=False,
        indent=2
    )


# ============================================================
# IDENTIFICAÇÃO DA FONTE DE CONHECIMENTO
# ============================================================

def identificar_fontes(pergunta):
    """
    Identifica quais fontes provavelmente são relevantes
    para responder à pergunta do cliente.
    """

    pergunta = pergunta.lower()

    fontes = []

    palavras_transacoes = [
        "gastei",
        "gasto",
        "gastou",
        "despesa",
        "despesas",
        "recebi",
        "receita",
        "receitas",
        "salário",
        "salario",
        "transação",
        "transações",
        "transacao",
        "transacoes",
        "alimentação",
        "alimentacao",
        "moradia",
        "saúde",
        "saude",
        "transporte",
        "lazer",
        "supermercado",
        "restaurante",
        "uber",
        "combustível",
        "combustivel"
    ]

    palavras_historico = [
        "já perguntei",
        "ja perguntei",
        "já falei",
        "ja falei",
        "histórico",
        "historico",
        "atendimento",
        "conversei",
        "conversamos",
        "atendimento anterior"
    ]

    palavras_perfil = [
        "meu perfil",
        "perfil de investidor",
        "minha idade",
        "minha renda",
        "meu objetivo",
        "meus objetivos",
        "minha meta",
        "minhas metas",
        "reserva de emergência",
        "reserva de emergencia",
        "patrimônio",
        "patrimonio",
        "risco"
    ]

    palavras_produtos = [
        "produto",
        "produtos",
        "cdb",
        "tesouro",
        "tesouro selic",
        "lci",
        "lca",
        "fundo",
        "investimento",
        "investir",
        "rentabilidade",
        "aporte",
        "risco"
    ]

    if any(palavra in pergunta for palavra in palavras_transacoes):
        fontes.append("transacoes")

    if any(palavra in pergunta for palavra in palavras_historico):
        fontes.append("historico")

    if any(palavra in pergunta for palavra in palavras_perfil):
        fontes.append("perfil")

    if any(palavra in pergunta for palavra in palavras_produtos):
        fontes.append("produtos")

    # Se não conseguimos identificar uma fonte específica,
    # usamos toda a base para permitir que o LLM interprete a pergunta.
    if not fontes:
        fontes = [
            "transacoes",
            "historico",
            "perfil",
            "produtos"
        ]

    return fontes


# ============================================================
# MONTAGEM DO CONTEXTO
# ============================================================

def montar_contexto(pergunta):
    """
    Monta somente o contexto necessário para a pergunta.
    """

    fontes = identificar_fontes(pergunta)

    contexto = []

    if "transacoes" in fontes:
        contexto.append(
            "### TRANSAÇÕES FINANCEIRAS\n"
            + consultar_transacoes()
        )

    if "historico" in fontes:
        contexto.append(
            "### HISTÓRICO DE ATENDIMENTO\n"
            + consultar_historico()
        )

    if "perfil" in fontes:
        contexto.append(
            "### PERFIL DO INVESTIDOR\n"
            + consultar_perfil()
        )

    if "produtos" in fontes:
        contexto.append(
            "### PRODUTOS FINANCEIROS\n"
            + consultar_produtos()
        )

    return "\n\n".join(contexto)


# ============================================================
# SYSTEM PROMPT
# ============================================================

SYSTEM_PROMPT = """
Você é a BIA do Futuro, uma assistente financeira pessoal.

Seu objetivo é ajudar o cliente a consultar e organizar suas informações
financeiras utilizando os dados disponíveis na base de conhecimento.

FONTES DISPONÍVEIS:

- transações financeiras;
- histórico de atendimento;
- perfil do investidor;
- metas financeiras;
- produtos financeiros.

REGRAS OBRIGATÓRIAS:

1. Responda de forma clara, objetiva e organizada.

2. Utilize somente as informações presentes no contexto fornecido.

3. Nunca invente valores, transações, produtos, metas, atendimentos,
características do cliente ou qualquer outro dado.

4. Quando realizar cálculos com base nas transações, apresente o cálculo
ou explique de onde veio o resultado.

5. Se a informação solicitada não estiver disponível no contexto,
diga claramente que não há dados suficientes para responder.

6. Nunca transforme uma suposição em fato.

7. Considere o perfil e os objetivos do cliente quando essas informações
estiverem disponíveis e forem relevantes para a pergunta.

8. Ao falar sobre produtos financeiros, utilize somente as características
registradas na base de conhecimento.

9. Não invente rentabilidade, taxas, prazos, riscos ou características
de produtos.

10. Não forneça senhas, credenciais ou informações de outros clientes.

11. Se a pergunta estiver fora do escopo da BIA ou não puder ser respondida
com os dados disponíveis, explique a limitação de forma clara.

12. Seu tom deve ser profissional, acessível, educativo e direto.

13. Quando apropriado, informe ao cliente qual tipo de informação da base
foi utilizada para elaborar a resposta.

14. Não diga que realizou uma consulta externa se isso não aconteceu.

15. Não invente informações para preencher lacunas.

A BIA é uma assistente de consulta e apoio financeiro baseada nos dados
fornecidos. Sua prioridade é precisão, segurança e transparência.
"""


# ============================================================
# FUNÇÃO PRINCIPAL DO AGENTE
# ============================================================

def perguntar_bia(pergunta):
    """
    Envia uma pergunta para a BIA, utilizando a base de conhecimento
    como contexto.
    """

    if not pergunta or not pergunta.strip():
        return "Digite uma pergunta para a BIA."

    if not OPENAI_API_KEY:
        return (
            "A chave da API da OpenAI não foi configurada. "
            "Verifique o arquivo .env."
        )

    contexto = montar_contexto(pergunta)

    prompt_usuario = f"""
CONTEXTO DA BASE DE CONHECIMENTO:

{contexto}

PERGUNTA DO CLIENTE:

{pergunta}

Responda à pergunta utilizando somente o contexto fornecido
e seguindo rigorosamente as regras do System Prompt.
"""

    try:
        resposta = client.responses.create(
            model=MODEL,
            instructions=SYSTEM_PROMPT,
            input=prompt_usuario
        )

        return resposta.output_text

    except Exception as erro:
        return (
            "Não foi possível obter uma resposta da BIA no momento.\n\n"
            f"Detalhe técnico: {erro}"
        )


if __name__ == "__main__":

    print("========================================")
    print("TESTE DA BASE DE CONHECIMENTO")
    print("========================================")

    pergunta = "Quanto gastei com alimentação?"

    print("\nPergunta:")
    print(pergunta)

    print("\nFontes identificadas:")
    print(identificar_fontes(pergunta))

    print("\nContexto encontrado:")
    print(montar_contexto(pergunta))