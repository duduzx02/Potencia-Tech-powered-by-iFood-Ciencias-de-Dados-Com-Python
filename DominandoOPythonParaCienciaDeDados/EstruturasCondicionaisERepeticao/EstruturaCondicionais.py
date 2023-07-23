saldo = 2000.00
saque = float(input("Informe o valor do saque: "))

# if saldo > saque:
#     print("Realizando o saque!")

# if saldo < saque:
#     print("Saldo insuficiente!")

# quantidade = 200
# tirada = int(input("digite a tirada: "))

# if quantidade > tirada:
#     print("Tirada com sucesso!")
# else:
#     print("Saldo insuficiente!")

# opcao = int(input("Informe uma opção: [1] sacar \n[2] extrato:\n"))
# if opcao == 1:
#     valor = int(input("Informe a quantidade para o saque: "))
# elif opcao == 2:
#     print("Exibindo o extrato")
# else:
#     print("Opção inválida!")

idade = int(input("Informe sua idade: "))
if idade >= 18:
    if idade == 18:
        print("Você tem 18!")
    elif idade == 19:
        print("Você tem 19!")
    elif idade == 20:
        print("Você tem 20!")
    else:
        print("Você tem mais de 20!")
else:
    print("Você ainda é de menor.")

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
