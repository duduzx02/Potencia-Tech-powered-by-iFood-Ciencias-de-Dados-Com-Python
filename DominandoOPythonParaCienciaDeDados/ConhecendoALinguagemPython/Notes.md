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