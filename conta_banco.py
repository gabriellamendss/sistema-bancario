class ContaBancaria:
    def __init__(self, nome, senha):
        self.nome = nome
        self.numero_conta = random.randint(100, 999)
        self.__senha = senha  # Atributo privado
        self.__saldo = 0.0
        self.historico = []

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.historico.append(f"Depósito de R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("O valor de saque deve ser maior que zero.")
            return

        if self.__saldo >= valor:
            self.__saldo -= valor
            self.historico.append(f"Saque de R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.__saldo:.2f}")

    def exibir_historico(self):
        if not self.historico:
            print("Não há movimentações no histórico.")
        else:
            print("Histórico de movimentações:")
            for transacao in self.historico:
                print(f"- {transacao}")

    def verificar_senha(self, senha):
        return senha == self.__senha

import random

def criar_conta():
    nome = input("Informe seu nome: ")
    while True:
        senha = input("Crie uma senha numérica de 4 dígitos: ")
        if len(senha) == 4 and senha.isdigit():
            senha = int(senha)
            break
        else:
            print("A senha deve conter exatamente 4 dígitos.")
    return ContaBancaria(nome, senha)

def menu():
    print("+----------------------------------+")
    print("|        Banco Digital            |")
    print("+----------------------------------+")
    print("1 - Consultar Saldo")
    print("2 - Realizar Depósito")
    print("3 - Realizar Saque")
    print("4 - Exibir Histórico")
    print("5 - Sair")
    print("+----------------------------------+")

if __name__ == "__main__":
    print("Bem-vindo ao Banco Digital!")
    conta = criar_conta()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            senha = int(input("Digite sua senha para consultar o saldo: "))
            if conta.verificar_senha(senha):
                conta.consultar_saldo()
            else:
                print("Senha incorreta.")

        elif opcao == "2":
            try:
                valor = float(input("Digite o valor para depósito: "))
                conta.depositar(valor)
            except ValueError:
                print("Valor inválido. Por favor, insira um número.")

        elif opcao == "3":
            senha = int(input("Digite sua senha para realizar o saque: "))
            if conta.verificar_senha(senha):
                try:
                    valor = float(input("Digite o valor para saque: "))
                    conta.sacar(valor)
                except ValueError:
                    print("Valor inválido. Por favor, insira um número.")
            else:
                print("Senha incorreta.")

        elif opcao == "4":
            senha = int(input("Digite sua senha para exibir o histórico: "))
            if conta.verificar_senha(senha):
                conta.exibir_historico()
            else:
                print("Senha incorreta.")

        elif opcao == "5":
            print("Obrigado por usar o Banco Digital. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

