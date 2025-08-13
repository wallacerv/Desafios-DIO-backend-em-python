
import textwrap
def menu():
    menu = """\n

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc]Nova Conta
    [ln]Listar contas
    [nu]Novo usuario
    [q] Sair

    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo+= saldo
        extrato += f"depósito: \t R${valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n @@@ Operação falhou! Valor informado é inválido @@@" )
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
         print("\n @@@ Operação falhou! Você não tem saldo @@@" )
    elif excedeu_limite:
         print("\n @@@ Operação falhou! O valor do saque excede o limite @@@" )
    elif excedeu_saques:
         print("\n @@@ Operação falhou! Número de saques excedido @@@" )
    elif valor>0:
        saldo-=valor
        extrato+=f"Saque: \t\t R$ {valor:.2f}\n"
        numero_saques +=1
        print("\n=== Depósito realizado com sucesso! ===")
    
    else:
         print("\n @@@ Operação falhou! Valor informado é inválido @@@" )
    
    return saldo, extrato




def exibir_extrato(saldo, /, *, extrato):
    print("\n ==================EXTRATO=================")
    print("não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\t R${saldo:.2f}")
    print("====================================================")

def criar_usuario(usuarios):
    cpf = input("informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuario com esse CPF! @@@")
        return

    nome = input("informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaa) ")
    endereco = input("Informe o endereço (logadouro, nro - bairro - cidade/siga estado): ")
    usuarios.append({"nome" : nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("==== Usuário criado com sucesso ====")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("\n === Conta criada com sucesso! ===" )
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência: \t{conta['agencia']}
            c/c:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    limite_saques = 3
    agencia = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
     
    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques
        )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia,numero_conta,usuarios)
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")




main()




