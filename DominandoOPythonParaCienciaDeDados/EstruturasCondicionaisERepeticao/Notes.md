# Indentação e blocos
## A estética
- Identar código pe uma forma de manter o código fonte mais legível e manutenível. Mas em python ela exerce um segundo papel, através da indentação o interpretador consegue determinar onde um bloco de comando inicia e onde ele termina.
  
## Bloco de comando
- As linguagens de programação costumam utilizar caracteres ou palavras reservadas para terminar o início e fim do bloco. Em Java e C por exemple, utilizamos chaves.

## Utilizando espaços
- Existe uma convenção em Python, que define as boas práticas para escrita de código na linguagem. Nesse documento é indicado utilizar 4 espaços em branco por nível de indentação, ou seja, a cada novo bloco adicionamos 4 novos espaços em branco.

# Estruturas condicionais
## O que são?
- A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

## if
- Para criar uma estrutura condicional simples, composta por um único desvio, podemos utilizar a palavra reservada if. O comando irá testar a expressão lógica, e em caso de retorno verdadeiro as ações presentes no bloco de código do if serão executadas.

## if/else
- Para criar uma estrutura condicional com dois desvios, podemos utilizar as palavras reservadas if e else. Como sabemos se a expressão lógica testada no if for verdadeira, então o bloco de código do if será executado. Caso contrário o bloco de código else será executado.

## if/elif/else
- Em alguns cenários queremos mais de dois desvios, para isso podemos utilizar a palavra reservada elif. O elif é composto por uma nova expressão lógica, que será testada e caso retorne verdadeiro o bloco de código do elif será executado. Não existe um número máximo de elifs que podemos utilizar, porém evite criar grandes estruturas condicionais, pois elas aumentam a complexxidade do código.

## if aninhado
- Podemos criar estruturas condicionais aninhadas, para isso basta adicionar estruturas if/elif/else dentro do bloco de código de estrutura if/elif/else

## if ternário
- O if ternário permite escrever uma condição em uma única linha. Ele é composto por três partes, a primeira parte é o retorno caso a expressão retorne verdadeiro, a segunda parte é a expressão lógica e a terceira parte é o retorno caso a expressão não seja atendida.

# Estrutura de repetição
## O que são estruturas de repetição?
- São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

## Comando for
- O comando for é usado para percorrer um objeto iterável. Faz sentido usar for quando sabemos o número exato de vezes que nosso bloco deve ser executado, ou quando queremos percorrer um objeto iterável.

## Função range
- Range é uma função buil-in do python, ela é usada para produzir uma sequÊncia de números inteiros a partir de um ínicio(inclusivo) para um fim (exclusivo). Se usarmos range(i, j) será produzido: 

- i, i +1, i + 2, ..., j - 1.
- Ela recebe 3 argumentos: stop(obrigatório), start (opcional) e step (opcional).

## Comando while
- O comando while é usado para repetir um bloco de código várias vezes. Faz sentido usar while quando não sabemos o número exato de vezes que nosso bloco de código deve ser executado.