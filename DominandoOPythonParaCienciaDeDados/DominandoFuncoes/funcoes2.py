print("Position only")
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Logan", 2016, "QSG8915", marca="Renault", motor="1.0", combustivel="flex")

criar_carro("Logan", 2016, "QSG8915", "Renault", "1.0", "flex")

# criar_carro(modelo="Logan", ano=2016, placa="QSG8915", marca="Renault", motor="1.0", combustivel="flex") # invalido

print()
print("Keyword only")
def criar_moto(*, modelo, ano, placa):
    print(modelo, ano, placa)

criar_moto(modelo="Titan 160", ano=2015, placa="sad5842")
# criar_moto("Titan 160", 2015, "sad5842") #invalido

print()
print("Keyword and positional only")

def criar_kwid(ano, placa, /, *, motor):
    print(ano, placa, motor)

criar_kwid(2022, "QSG8915", motor="1.0")
# criar_kwid(2022, "QSG8915", "1.0") #Invalido

print()
print("Objetos de primeira classe")
def somar(a,b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} ? {b} = {resultado}")

exibir_resultado(10, 20, somar)
exibir_resultado(10, 20, subtrair)

soma = somar
print(soma(2, 6))

print()
print("Escopo local e escopo global")

salario = 2000
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))


