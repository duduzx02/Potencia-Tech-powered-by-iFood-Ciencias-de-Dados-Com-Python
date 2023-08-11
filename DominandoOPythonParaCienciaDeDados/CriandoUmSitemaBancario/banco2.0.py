def menu():
    menu = """
        [1]\tDepositar
        [2]\tSacar
        [3]\tExtrato
        [4]\tNova conta
        [5]\tListar contas
        [6]\tNovo usuário
        [00]\tSair
    \t: """
    return int(input(menu))

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito:\t R$ {deposito:.2f}\n"
        print("Depósito realizado com sucesso! ✔✔✔")
    else:
        print("Operação falhou! O valor informado é inválido. ❌❌❌")
    return saldo, extrato

def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente. ❌❌❌")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excedeu o limite. ❌❌❌")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saque excedido. ❌❌❌")
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque:\t\tR$ {saque:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso! ✔✔✔")
    else:
        print("Operação falhou! O valor informado é inválido. ❌❌❌")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n_____________ EXTRATO _____________")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}")
    print("___________________________________")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF! ❌❌❌")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereco (logradouro, nro - bairro - Cidade/sigla do estato(ex: SP)): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso! ✔✔✔")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso! ✔✔✔")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Usuário não encontrado, fluxo de criação de conta encerrado! ❌❌❌")

def listar_contas(contas):
    for conta in contas:
        linha = f""" 
            Agência:\t{conta['agencia']}
            C/C\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("_" * 55)
        print(linha)


def main():
    saldo = 0
    limite = 500
    extrato = """"""
    numero_saques = 0
    usuarios = []
    contas = []

    LIMTE_SAQUE = 3 
    AGENCIA = "0001"

    while True:
        opcao = menu()

        if opcao == 00:
            break

        elif opcao == 1:
            deposito = float(input("Digite o valor para depositar: "))

            saldo, extrato = depositar(saldo, deposito, extrato)
        elif opcao == 2:
            saque = float(input("Valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo,
                saque = saque,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMTE_SAQUE,
            )
 
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == 5:
            listar_contas(contas)

        elif opcao == 6:
            criar_usuario(usuarios)
        else: 
            print("Operação inválida, por favor selecione uma opção válida.")

main()