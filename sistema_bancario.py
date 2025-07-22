menu = """
  ############ Banco Python ##################
  O que deseja fazer?
  Depositar[1]
  Sacar[2]
  Exibir extrato[3]
  Sair[4]
  ###############################
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saques = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito\n"))

        if valor > 0:
            saldo+= valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação Falhou. Valor informado é inválido")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque\n"))
        
        if valor > saldo:
            print("Saldo insuficiente")
        
        elif valor > limite:
            print("O valor excedeu o limite")

        elif numero_saques >= limite_saques:
            print("Número máximo de saques excedido")
        
        elif valor > 0:
            saldo -=valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saques +=1
        
        else:
            print("O valor informado é inválido")

    elif opcao == "3":
        print("\n =================== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n saldo: R$ {saldo:.2f}")
        print( "=============================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a opção desejada")