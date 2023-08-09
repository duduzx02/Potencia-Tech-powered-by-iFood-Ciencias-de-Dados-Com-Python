# Funções
## O que são funções
- Funções é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, que podem ou não ter valores padrões. Funções deixam o código mais legível e reaproveitavel.
- Programar baseado em funções, é mesmo que dizer que estamos programando de maneira estruturada.

## Retornando valores
- para retornar um valor, utilizamos a palavrea reservada return.
- Toda função retorna None por padrão em python.
- Diferente de outras linguagens em python uma função pode retornar mais de um valor.

## Argumentos nomeados
- Funções também podem ser chamadas usando argumentos nomeados da forma chave=valor.

## Args e Kwards
- Podemos combinar parâmetros obrigatórios com args e kwargs. Quando esses são definidos (*args e **kwargs), o método recebe os valores como tupla e dicionário respectivamente.

## Parâmetros especiais
- Argurmentos podem ser passados para uma função python tanto por posição quanto explicitamente pelo nome.
- Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.

## Objetos de primeira classe
- Em python tudo é objeto, dessa forma funções também são objetos o que tornam objetos de primeira classe. Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estrutura de dados(lista, tuplas, dicionários, etc) e usar como valor de retorno para uma função(closures).

## Escopo local e escopo global
- Dentro do bloco da função o escopo é local. alterações feitas dentro do escopo serão perdidas quando o método terminar de ser executado. Objetos globais utilizamos a palavra-chave global, dentro de escopos locais, fazer isso é uma má prática. 