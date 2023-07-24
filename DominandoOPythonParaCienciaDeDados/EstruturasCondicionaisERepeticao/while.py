while True:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    
    if opcao == 0:
        break
    elif opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Extrato...")
    else:
        print("Inválido...")

print("Obrigado por usar nosso sistema bancário, até logo!")