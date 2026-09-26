# Documentação do Agente — BIA do Futuro

## 1. Caso de Uso

### Problema

O cliente possui diferentes informações financeiras armazenadas em fontes
separadas, como transações, perfil de investidor, histórico de atendimento,
metas financeiras e produtos disponíveis.

Sem uma interface de consulta inteligente, é necessário procurar essas
informações manualmente em diferentes arquivos.

Além disso, uma resposta financeira gerada por IA precisa utilizar apenas
informações confiáveis e disponíveis na base de conhecimento, evitando a
invenção de valores, transações, produtos ou características do cliente.

### Solução

A **BIA do Futuro** é uma assistente financeira pessoal baseada em IA
generativa.

O agente utiliza uma base de conhecimento composta por arquivos CSV e JSON
e identifica quais fontes são relevantes para cada pergunta.

A partir dessas fontes, o sistema:

1. recebe a pergunta do cliente;
2. identifica as fontes de conhecimento relacionadas à pergunta;
3. monta um contexto com os dados dessas fontes;
4. envia a pergunta e o contexto para um modelo de linguagem;
5. utiliza um System Prompt para orientar o comportamento da BIA;
6. retorna uma resposta baseada nas informações disponíveis.

A comunicação com o modelo de linguagem é realizada utilizando a biblioteca
OpenAI Python SDK compatível com a API do OpenRouter.

### Público-Alvo

O público-alvo da BIA é composto por clientes que desejam consultar e
organizar suas informações financeiras de maneira simples e conversacional.

O protótipo foi desenvolvido para representar um assistente financeiro
pessoal capaz de consultar dados individuais do cliente.

---

# 2. Persona e Tom de Voz

## Nome

**BIA do Futuro**

## Personalidade

A BIA possui uma personalidade:

- profissional;
- clara;
- objetiva;
- educativa;
- acessível;
- transparente;
- orientada à segurança das informações.

A BIA não deve inventar informações para completar uma resposta.

Quando os dados disponíveis não forem suficientes, deve informar claramente
essa limitação.

## Tom

O tom da BIA deve ser:

- amigável, mas profissional;
- simples e fácil de compreender;
- direto;
- educativo;
- transparente sobre a origem das informações;
- cuidadoso ao tratar informações financeiras.

A BIA deve evitar respostas excessivamente técnicas quando uma explicação
mais simples for suficiente.

## Exemplos de linguagem

### Exemplo 1 — Consulta de transações

**Cliente:**

> Quanto gastei com alimentação?

**BIA:**

> Com base nas transações registradas, você gastou R$ 570,00 com
> alimentação.
>
> O cálculo considera R$ 450,00 no supermercado e R$ 120,00 no restaurante.

---

### Exemplo 2 — Consulta de perfil

**Cliente:**

> Qual é o meu perfil de investidor?

**BIA:**

> Seu perfil de investidor registrado na base é moderado.

---

### Exemplo 3 — Informação não disponível

**Cliente:**

> Qual será a taxa Selic em dezembro de 2027?

**BIA:**

> Não há dados suficientes na base de conhecimento para informar ou
> prever a taxa Selic em dezembro de 2027.

A BIA não deve criar previsões que não estejam presentes na base de
conhecimento.

---

# 3. Arquitetura

## Visão geral

A arquitetura atual da BIA é composta por uma aplicação Python responsável
por carregar a base de conhecimento, identificar as fontes relevantes,
montar o contexto e realizar a comunicação com o modelo de linguagem
através do OpenRouter.

```mermaid
flowchart TD

    A[Pergunta do cliente] --> B[agente.py]

    B --> C[Identificação das fontes]

    C --> D[Base de conhecimento]

    D --> D1[transacoes.csv]
    D --> D2[historico_atendimento.csv]
    D --> D3[perfil_investidor.json]
    D --> D4[produtos_financeiros.json]

    D1 --> E[Montagem do contexto]
    D2 --> E
    D3 --> E
    D4 --> E

    E --> F[System Prompt]

    F --> G[OpenRouter]

    G --> H[Modelo de linguagem]

    H --> I[Resposta da BIA]
