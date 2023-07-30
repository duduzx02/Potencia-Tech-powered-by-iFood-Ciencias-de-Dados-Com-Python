menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [00] sair
: """

true = True
saldo = 0
limite = 500
extrato = """"""
numero_saques = 0
LIMTE_SAQUE = 3

while true:
    opcao = int(input(menu))

    if opcao == 00:
        break

    elif opcao == 1:
        deposito = int(input("Digite o valor para depositar: "))
        saldo = saldo + deposito
        extrato += f"Deposito: R${str(deposito)} \n"
    elif opcao == 2:
        saque = int(input("Valor do saque: "))
        if saque > limite:
            print("Desculpe, mas o limite para saque é de R$500.00")
        elif numero_saques >= LIMTE_SAQUE:
            print("Desculpe, mas o limite de saque diários são de 3 vezes.")
        elif saldo <= 0:
            print("Saldo insuficiente!")
        else: 
            print("Saque realizado com sucesso!")
            numero_saques += 1
            saldo = saldo - saque
            extrato += f"Saque: R${str(saque)} \n"
    elif opcao == 3:
        print(extrato)
        print(f"Total: R${saldo}")

    else:
        print("Opcão invalida! Tente novamente!")
            

print(extrato)
    