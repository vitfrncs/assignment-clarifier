# Assignment Clarifier

Programa para ajudar estudantes a identificar objetivos, entregas, regras e prazos em enunciados acadêmicos.


**Projeto desenvolvido no P0 da capacitação TrendsAI, da Softex.**

## Planejamento da solução

### Qual problema será resolvido?

Enunciados acadêmicos podem apresentar objetivos, entregas e regras
espalhados pelo texto, dificultando a identificação do que precisa
ser feito.

O programa ajudará a transformar esses enunciados em uma análise
organizada, preservando as informações e condições do texto original.

A solução não resolverá a atividade nem substituirá a leitura do
enunciado pelo estudante.

### Quem possui essa necessidade?

Estudantes que precisam compreender e organizar as exigências de
atividades acadêmicas.

### Qual será a entrada?

Um enunciado acadêmico em formato textual, informado pelo terminal.

Na implementação atual, o texto deve ser informado em uma única linha.
Entradas vazias ou compostas apenas por espaços são rejeitadas.

### Qual será a saída?

Uma análise textual em português, organizada em sete seções:

- Objetivo;
- Entregas obrigatórias;
- Regras e restrições;
- Itens opcionais;
- Permissões;
- Prazo;
- Pontos a esclarecer.

Quando não houver informação para uma seção, o modelo será instruído
a indicar “Não informado no enunciado”.


### Por que um LLM é adequado?

A tarefa exige interpretar instruções escritas em linguagem natural,
que podem expressar a mesma exigência de formas diferentes.

Um LLM pode ajudar a identificar e reorganizar essas informações,
distinguindo obrigações, permissões e itens opcionais.


### Quais erros receberão tratamento específico?

O programa já identifica entradas vazias ou compostas apenas por espaços.

Durante a evolução do projeto, está previsto o tratamento de:

- configuração ausente ou inválida;
- falha de conexão;
- tempo de espera excedido;
- indisponibilidade do serviço;
- resposta vazia ou em formato inesperado;


## Estado atual

- Recebe um enunciado pelo terminal.
- Impede o processamento de entradas vazias.
- Prepara e exibe o prompt de análise.

A integração com o LLM institucional ainda não foi implementada :).

## Execução

É necessário ter Python 3 instalado.

Execute:

```bash
python3 src/main.py
```