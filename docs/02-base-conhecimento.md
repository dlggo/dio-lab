# Base de Conhecimento — BIA do Futuro

## 1. Visão Geral

A BIA do Futuro utiliza uma base de conhecimento local composta por arquivos
CSV e JSON.

Esses arquivos armazenam as informações utilizadas pelo agente para responder
às perguntas do cliente.

Atualmente, a base de conhecimento é composta por:

* `data/transacoes.csv`
* `data/historico_atendimento.csv`
* `data/perfil_investidor.json`
* `data/produtos_financeiros.json`

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
```

---

## 3. Arquivo `transacoes.csv`

O arquivo `transacoes.csv` contém as movimentações financeiras utilizadas
pela BIA.

Esses dados permitem responder perguntas relacionadas a:

* receitas;
* despesas;
* categorias de gastos;
* valores;
* datas;
* movimentações financeiras.

### Exemplo de informações

| Data | Descrição | Categoria | Valor | Tipo |
| ---- | --------- | --------- | ----: | ---- |
| —    | —         | —         |     — | —    |

A BIA utiliza essas informações para realizar consultas e cálculos sobre as
transações disponíveis na base.

### Exemplo de consulta

**Pergunta:**

> Quanto gastei com alimentação?

A BIA pode consultar as transações relacionadas à categoria de alimentação
e realizar a soma dos valores encontrados.

**No teste realizado:**

```text
Supermercado   R$ 450,00
Restaurante    R$ 120,00
```

**Cálculo:**

```text
R$ 450,00 + R$ 120,00 = R$ 570,00
```

**Resposta:**

> Você gastou R$ 570,00 com alimentação.

---

## 4. Arquivo `historico_atendimento.csv`

O arquivo `historico_atendimento.csv` contém registros de atendimentos
anteriores do cliente.

Essa fonte é utilizada para responder perguntas relacionadas ao histórico
de atendimento.

Exemplos:

* assuntos já consultados;
* atendimentos anteriores;
* canais de atendimento;
* datas dos atendimentos;
* dúvidas anteriores.

### Exemplo de consulta

**Pergunta:**

> Já perguntei sobre CDB?

A BIA consulta o histórico de atendimento para verificar se existe um
registro relacionado ao assunto.

**No teste realizado, foi identificado um atendimento sobre CDB em:**

```text
Data: 15/09/2025
Canal: Chat
Assunto: Rentabilidade e prazos do CDB
```

---

## 5. Arquivo `perfil_investidor.json`

O arquivo `perfil_investidor.json` contém informações relacionadas ao perfil
financeiro e de investidor do cliente.

Entre as informações utilizadas pelo agente estão:

* perfil de investidor;
* renda;
* objetivos;
* metas;
* patrimônio;
* tolerância a risco;
* informações relacionadas à reserva de emergência.

As metas financeiras também fazem parte das informações armazenadas nesse
arquivo.

### Exemplo de consulta

**Pergunta:**

> Qual é o meu perfil de investidor?

A BIA consulta o arquivo `perfil_investidor.json`.

**Resultado do teste:**

```text
Perfil: Moderado
```

---

## 6. Arquivo `produtos_financeiros.json`

O arquivo `produtos_financeiros.json` contém os produtos financeiros
disponíveis na base de conhecimento.

Entre os produtos cadastrados estão:

* Tesouro Selic;
* CDB Liquidez Diária;
* LCI/LCA;
* Fundo Multimercado;
* Fundo de Ações.

As informações sobre os produtos devem ser obtidas somente a partir desse
arquivo.

A BIA não deve inventar características, taxas, riscos, rentabilidades ou
outras informações que não estejam registradas na base.

### Exemplo de consulta

**Pergunta:**

> Quais produtos financeiros estão disponíveis?

A BIA consulta o arquivo de produtos e apresenta os produtos cadastrados
na base.

---

## 7. Seleção das Fontes

O arquivo `src/agente.py` possui uma função responsável por identificar
quais fontes estão relacionadas à pergunta:

```python
identificar_fontes(pergunta)
```

A identificação atualmente utiliza palavras-chave.

### Exemplos

**Pergunta:**

> Quanto gastei com alimentação?

**Fonte identificada:**

```text
transacoes
```

---

**Pergunta:**

> Qual é o meu perfil de investidor?

**Fonte identificada:**

```text
perfil
```

---

**Pergunta:**

> Já perguntei sobre CDB?

**Fonte identificada:**

```text
historico
```

---

**Pergunta:**

> Quais produtos financeiros estão disponíveis?

**Fonte identificada:**

```text
produtos
```

---

## 8. Montagem do Contexto

Depois da identificação das fontes, o agente utiliza a função:

```python
montar_contexto(pergunta)
```

Essa função seleciona os dados necessários para a pergunta e monta o
contexto que será enviado ao modelo de linguagem.

O fluxo atual é:

```text
Pergunta do cliente
        ↓
Identificação das fontes
        ↓
Seleção dos dados
        ↓
Montagem do contexto
        ↓
System Prompt
        ↓
OpenRouter
        ↓
Modelo de linguagem
        ↓
Resposta da BIA
```

---

## 9. Utilização das Fontes

Cada fonte possui uma finalidade específica:

| Fonte                       | Finalidade                                 |
| --------------------------- | ------------------------------------------ |
| `transacoes.csv`            | Consultar movimentações e gastos           |
| `historico_atendimento.csv` | Consultar atendimentos anteriores          |
| `perfil_investidor.json`    | Consultar perfil, renda, objetivos e metas |
| `produtos_financeiros.json` | Consultar produtos financeiros             |

Quando nenhuma fonte específica é identificada, o agente utiliza todas as
fontes disponíveis para montar o contexto.

---

## 10. Regras de Utilização da Base

A BIA deve utilizar as informações disponíveis na base de conhecimento como
fonte para suas respostas.

O agente deve:

* utilizar os dados presentes no contexto;
* apresentar os valores encontrados;
* realizar cálculos quando necessário;
* explicar os cálculos quando forem relevantes;
* informar quando uma informação não estiver disponível;
* utilizar somente as características dos produtos presentes na base.

O agente não deve:

* inventar valores;
* inventar transações;
* inventar produtos;
* inventar metas;
* inventar características do cliente;
* inventar taxas;
* inventar rentabilidades;
* inventar riscos;
* transformar suposições em fatos.

---

## 11. Informações Não Disponíveis

Quando a base de conhecimento não possuir informações suficientes para
responder uma pergunta, a BIA deve informar essa limitação.

### Exemplo

**Pergunta:**

> Qual será a taxa Selic em dezembro de 2027?

**Resposta esperada:**

> Não há dados suficientes na base de conhecimento para informar ou prever a
> taxa Selic em dezembro de 2027.

Nesse caso, a BIA não deve criar uma previsão ou apresentar um valor que não
esteja presente na base.

---

## 12. Dados de Demonstração

Os arquivos utilizados no projeto fazem parte da base de dados de demonstração
do protótipo.

Eles são utilizados para desenvolver e testar o comportamento da BIA sem
utilizar dados financeiros reais de clientes.

---

## 13. Limitações Atuais

A base de conhecimento atual possui algumas limitações:

* os dados são armazenados localmente;
* não existe atualização automática dos dados;
* o agente não consulta sistemas bancários externos;
* o agente não realiza consultas externas para complementar as informações;
* a seleção das fontes utiliza palavras-chave;
* a qualidade das respostas também depende do modelo de linguagem utilizado.

Essas limitações fazem parte da implementação atual do protótipo.

---

## 14. Resumo

A base de conhecimento da BIA do Futuro é formada por quatro fontes
principais:

```text
transacoes.csv
        ↓
Informações financeiras


historico_atendimento.csv
        ↓
Histórico de atendimentos


perfil_investidor.json
        ↓
Perfil, objetivos e metas


produtos_financeiros.json
        ↓
Produtos financeiros
```

Essas fontes fornecem o contexto necessário para que o agente possa
responder às perguntas do cliente de acordo com os dados disponíveis no
protótipo.

A separação das informações em diferentes arquivos também permite que o
agente identifique quais fontes são relevantes para cada pergunta antes de
enviar o contexto ao modelo de linguagem.
