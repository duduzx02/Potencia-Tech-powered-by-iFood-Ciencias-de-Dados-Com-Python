# Tipos de dados
## Por que usamos tipos?
- Os tipos servem para definir as caracteristicas e comportamentos de um valor (objeto) para o interpretador.
- Ex: 
- - Com esse tipo eu sou capaz de realizar operações matemáticas.
- - Esse tipo para ser armazenado em memória irá consumir 24 bytes.

## Tipos em Python
- Os tipos built-in são:
- - Texto           str
- - Númerico        int, float, complex
- - Sequência       list, tuple, range
- - Mapa            Disct
- - Coleção         set, fronzenset
- - Booleano        boll
- - Binário         bytes, bytearray, memoryview 

## Números inteiros
- São representado pela classe **int** e possuem precição ilimtitada.
- - 1, 10, 100, -58, -1000

## Npumeros de ponto flutuante
- Representam os números racionais e sua implementação é feita pela classe **float**
- 1.5, -10.49, 0.76
- 

## Booleano
- É usado para representar verdadeiro ou falso, e é implementado pela classe **bool**, em python é uma subclasse de int, uma vez que qualquer número diferente de 0 representa verdaiero e 0 representa falso. 
- True e False

## Strings
- Strings ou cadeia de caracteres são usadas para representar valores alfanúmericos, e é implementada pela classe str.
- "Python", 'python', """Python""", '''Python'''

# Modo interativo
- O interpretador python pode executar em modo que possibilite o desenvolvedor a escrever código, e ver o resultado na hora.

## iniciando o modo interativo
- Existem duas formas de iniciar o modo interativo, chamando apenas o interpretador (python) ou executando o script com a flag -i (python -i app.py)

## função dir
- Sem argumentos, retorna a lista de nomes no escopo local atual. Com um argumento, retorna uma lista de atributos válidos para o objeto
- Ex:
- - dir()
- - dir(100)

## função help
- Invoca o sistema de ajuda integrada. É possível fazer buscas em modo interativo ou informar por parâmetro qual o nome do módulo, função, classe, método ou variável.
- - help()
- - help(100)

# Variáveis e constantes

## Variáveis 
- Em linguagens de programação podemos definir valores que podem sofrer alterações no decorrer da execução do programa. Esses valores recebem o nome de variáveis, pois eles nascem com um valor e não necessariamente devem permanecer com o mesmo durante a execução do programa.
## Alterandos os valores
- Não precisamos definir o tipo de dados da variável, o python faz isso automaticamente. E por isso não é possivel criar uma variável sem atribuir um valor. Para alterar o valor da variável basta fazer uma atribuição de um novo valor.

## Constantes
- Assim como as variáveis, são utilizadas para armazenar valores. Uma constante nasce com um valor e permanece com ele até o final da execução do programa, ou seja, o valor é imutável.

## Python não tem constantes
- Não existe uma palavra reservada para informar ao interpretador que o valor é constante.
- Em python usamos a convenção que diz ao programador que a variável é uma constante. Para fazer isso, você deve criar a variável com o nome todo em letras maíusculas.

## Boas práticas
- O padrão de nomes deve ser snake case
- Escolher nomes sugestivos
- Nome de constantes todo em maiúcuslo.

# Conversão de tipos
## Convertendo tipos
- Em alguns momentos é necessário converter o tipo de uma variável para manipular de forma diferente. Ex:
- Variáveis do tipo string, que armazenam número e precisamos fazer alguma operação matemática com esse valor.

# Funções de entrada e saída
## Lendo valores com a função input
- A função builtin input é utilizada quando queremos ler dados da entrada padrão(teclado). Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A função lê a entrada, converte para string e retorna o valor.

## Exibindo valores com a função print
- A função builtin print é utilizada quando queremos exibir dados na saída padrão (tela). Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.