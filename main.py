menu = """
[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []  
saques = []  

while True:
    opcao = input(menu).lower()

    # Opção de depósito
    if opcao == "d":
        value = float(input("Informe o valor a ser depositado: "))
        if value > 0:
            depositos.append(value)  
            saldo += value  
            print(f"Depósito realizado: R$ {value:.2f}")
            print(f"Saldo atual: R$ {saldo:.2f}")
        else:
            print("Impossível depositar esses valores.")

    
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            value = float(input("Informe o valor que deseja sacar: "))
    
            if value <= 0:
                print("Não sera Possível sacar dinheiro.")
            elif value <= saldo and value <= limite:
                saques.append(value)  
                saldo -= value  
                numero_saques += 1
                print(f"Saque de R$ {value:.2f} realizado com sucesso!")
                print(f"Saldo atual: R$ {saldo:.2f}")
            else:
                print("valor excede o limite de R$500,00.")
        else:
            print("Atingiu o limite de saques.")

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        if depositos:
            print("Depósitos realizados:")
            for value in depositos:
                print(f"Depósito: R$ {value:.2f}")
        else:
            print("Nenhum depósito realizado.")

        if saques:
            print("\nSaques realizados:")
            for value in saques:
                print(f"Saque: R$ {value:.2f}")
        else:
            print("\nNenhum saque realizado.")

     
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("==============================\n")


    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida. Por favor, selecione a operação desejada.")
