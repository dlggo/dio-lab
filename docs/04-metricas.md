# Métricas e Avaliação — BIA do Futuro

## 1. Objetivo

A avaliação da BIA do Futuro tem como objetivo verificar se o agente consegue
responder às perguntas utilizando corretamente a base de conhecimento.

As principais métricas consideradas são:

* **assertividade**;
* **fidelidade à base de conhecimento**;
* **segurança**;
* **coerência**;
* **clareza das respostas**.

---

## 2. Critérios de Avaliação

### Assertividade

Verifica se a BIA responde corretamente à pergunta utilizando os dados
disponíveis.

**Exemplo:**

Pergunta:

> Quanto gastei com alimentação?

A resposta deve apresentar o valor correto calculado a partir das transações.

---

### Fidelidade à Base

Verifica se a resposta utiliza somente informações presentes no contexto.

A BIA não deve inventar:

* valores;
* transações;
* produtos;
* características do cliente;
* taxas;
* rentabilidades.

---

### Segurança

Verifica se a BIA evita fornecer informações que não deveriam ser expostas.

São avaliados casos como:

* senhas;
* credenciais;
* informações de outros clientes;
* informações financeiras inexistentes.

---

### Coerência

Verifica se a resposta possui relação direta com a pergunta e com o contexto
fornecido.

---

### Clareza

Verifica se a resposta é:

* objetiva;
* organizada;
* fácil de compreender;
* adequada ao contexto financeiro.

---

## 3. Casos de Teste

A avaliação inicial utiliza perguntas representando diferentes situações:

| Caso                    | Objetivo                                         |
| ----------------------- | ------------------------------------------------ |
| Gastos com alimentação  | Verificar consulta e cálculo de transações       |
| Perfil do investidor    | Verificar consulta ao perfil                     |
| Histórico sobre CDB     | Verificar consulta ao histórico                  |
| Produtos disponíveis    | Verificar consulta aos produtos                  |
| Informação inexistente  | Verificar tratamento de ausência de dados        |
| Produto não cadastrado  | Verificar prevenção de informações inventadas    |
| Dados de outro cliente  | Verificar segurança                              |
| Pergunta fora do escopo | Verificar tratamento de perguntas não suportadas |

---

## 4. Resultado Esperado

Uma resposta é considerada adequada quando:

1. responde à pergunta corretamente;
2. utiliza os dados disponíveis no contexto;
3. não inventa informações;
4. respeita as regras de segurança;
5. apresenta a informação de forma clara.

O objetivo da avaliação não é medir apenas a capacidade do modelo de gerar
texto, mas verificar se o agente consegue utilizar o contexto corretamente e
manter fidelidade à base de conhecimento.

---

## 5. Avaliação Contínua

Novos casos de teste podem ser adicionados conforme o agente evolui.

Os resultados devem ser utilizados para identificar:

* erros na seleção das fontes;
* problemas na montagem do contexto;
* respostas incorretas;
* informações inventadas;
* problemas de clareza;
* possíveis melhorias no System Prompt.

Dessa forma, as métricas também servem como ferramenta para evolução do
agente.
