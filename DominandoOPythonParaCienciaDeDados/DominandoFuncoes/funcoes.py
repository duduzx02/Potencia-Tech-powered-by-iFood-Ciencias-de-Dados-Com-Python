def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome = "Anônimo"):
    print(f"Seja bem vindo {nome}!")

print("O que são funções: ")
print(exibir_mensagem())
exibir_mensagem()
exibir_mensagem2("Eduardo")
exibir_mensagem3()
exibir_mensagem3("Eduardo")

print()
print("Retornando valores: ")
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([0, 10, 20, 34])) #64
print(retorna_antecessor_e_sucessor(24)) #(23, 25)

print()
print("Argumentos nomeados: ")

def salvar_carro(marca, modelo, ano, placa):
    return f"Carro inserido com sucesso! {marca} / {modelo} / {ano} / {placa}"
print(salvar_carro("Fiat", "Palio", 1999, "sad-5257"))
print(salvar_carro(marca="Renault", modelo="Kwid", ano=2020, placa="QSG8915")) # argumento nomeado

print()
print("Args e Kwards")
def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Quarta, 09 de agosto de 2023", "Zen of python", "Bonito é melhor que feio", "Mais texto", autor="Tim peters", ano=1999)