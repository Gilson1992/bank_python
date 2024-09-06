# Sistema Bancário PY_bank
# Esse sistema irei desenvolver as funções em inglês para deixar o código mais universal
# Sou o Gilson Souza da Silva
# Estudante do Bootcamp NTT Data de Engenheiro de Dados.


# Criar uma nova conta / Create a new account
def new_conta() :
    holder = input("Digite o nome do titular da conta = ")
    balance = 0
    return holder, balance

# Função de Depositar / Deposit function
def deposit(balance) :
    value = float(input("Digite o valor em R$ "))
    if value > 0 :
        balance += value
        print(f"Depósito de R${value:.2f} realizado com sucesso.")
    else : 
        print("Valor de depósito inválido.")
    return balance

# Função de Sacar / Withdraw Function
def withdraw(balance) :
    value = float(input("Digite o valor em R$"))
    if 0 < value <= balance :
        balance -= value
        print(f"Saque de R${value:.2f} realizado com sucesso.")
    else:
        print("Saque inválido ou saldo insuficiente.")
    return balance

# Função de extrato bancário / Bank statement function
def bank_statement(holder,balance) :
    print(f"Saldo atual de {holder}: R${balance:.2f}")


def menu():
    print("\nBem-vindo ao Sistema Bancário!")
    holder, balance = new_conta()

    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Verificar saldo")
        print("4. Sair")
        
        opcao = input("Opção: ")

        if opcao == "1":
            balance = deposit(balance)
        elif opcao == "2":
            balance = withdraw(balance)
        elif opcao == "3":
            bank_statement(holder, balance)
        elif opcao == "4":
            print("Obrigado por utilizar o Sistema Bancário!")
            break
        else:
            print("Opção inválida, tente novamente.")

# Inicia o programa / start the program
menu()

