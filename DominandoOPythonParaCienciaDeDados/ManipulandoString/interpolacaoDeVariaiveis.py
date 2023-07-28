#old style %
nome = "Eduardo"
idade = 27

print("Nome: %s Idade: %d" % (nome, idade))

# Método format

print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))

#Metodo f-string
print(f"Nome: {nome} Idade: {idade}")

# Formatar string com f-strings

PI = 3.14159

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}")

dados = {
    "nome": "Eduardo",
    "idade": 27
}

print("Nome: {nome} Idade: {idade}".format(**dados))

