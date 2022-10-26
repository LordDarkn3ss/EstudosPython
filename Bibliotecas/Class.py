from Bibliotecas.Functions import captar_data


class BankAccount:  # Classe da conta bancária

    def __init__(self, num, saldo, nome, tipo, list_extrato=None, list_saldo=None, list_data=None, status=False):

        # Esses "IFs" testam se as listas começam vazias para iniciar elas como vazias
        if list_extrato is None:
            list_extrato = []
        if list_saldo is None:
            list_saldo = []
        if list_data is None:
            list_data = []

        # Declarando os atributos
        self.num = num  # 'String' contendo o número da conta
        self.saldo = saldo  # 'Float' com o saldo da conta
        self.nome = nome  # 'String' com o mome do dono da conta
        self.tipo = tipo  # 'String' que diz se a conta é CORRENTE ou POUPANÇA
        self.list_extrato = list_extrato  # Lista que vai guardar o valor de cada deposito ou saque
        self.list_saldo = list_saldo  # Lista que vai guardar o saldo depois de cada operação
        self.list_data = list_data  # lista que vai guardar a data de cada operação
        self.status = status  # 'Boolean' que vai dizer se a conta está ATIVA ou DESATIVADA

    def ativar(self):
        if self.status:  # Se aconta já estiver ativa, informar que não pode ser ativada novamente
            print("== ERRO, CONTA JA ATIVA ==")
        else:
            self.status = True  # Se não, ativar conta
            print("== CONTA ATIVADA COM SUCESSO ==")

    def desativar(self):
        if not self.status:  # Se a conta já estiver desativada, informar que não pode ser desativada novamente
            print("== ERRO, CONTA JA DESATIVADA ==")
        else:
            if self.saldo != 0:  # Não desativar a conta se ainda tiver saldo
                print("== ERRO, CONTA AINDA COM SALDO ==")
            else:
                self.status = False  # Se não, desativar conta
                print("== CONTA DESATIVADA COM SUCESSO ==")

    def depositar(self, valor_deposito):  # A função vai receber um parametro
        if not self.status:  # Só depositar se a conta estiver ativa
            print("== CONTA INATIVA ==")
        else:
            self.saldo += valor_deposito  # Adicionar o valor do parametro no SALDO
            self.list_extrato.append(valor_deposito)  # Contabilizar valor adicionado
            self.list_saldo.append(self.saldo)  # Contabilizar o SALDO depois da operação
            self.list_data.append(captar_data())  # Contabilizar a data, chamando a função que capta a mesma

            print("== DEPOSITADO COM SUCESSO ==")

    def sacar(self, valor_saque):  # A função vai receber um parametro
        if not self.status:  # Só sacar se a conta estiver ativa
            print("== CONTA INATIVA ==")
        else:
            if valor_saque > self.saldo:  # Só sacar se tiver o valor na conta
                print("== SALDO INSUFICIENTE ==")
            else:
                self.saldo -= valor_saque  # Subtrair o valor do parametro no SALDO
                self.list_extrato.append(valor_saque * -1)  # Contabilizar valor subtraido
                self.list_saldo.append(self.saldo)  # Contabilizar o SALDO depois da operação
                self.list_data.append(captar_data())  # Contabilizar a data, chamando a função que capta a mesma

                print("== SAQUE EFETUADO COM SUCESSO ==")

    def extrato(self):
        if not self.status:  # Só mostrar o extrato se a conta estiver ativa
            print("== CONTA INATIVA ==")

        else:
            print("\n\n", 18 * "=-")  # Daqui pra baixo é só enfeite, basicamente
            print(35 * "-")

            for x in range(len(self.list_extrato)):  # Pecorrer o extrato do primeiro ao último
                if self.list_extrato[x] > 0:  # Se o valor for positivo, mostrar a mensagem de "DEPOSITO"
                    print(f" DEPOSITOU: {self.list_extrato[x]}"  # Mostrar o valor do depósito X
                          f"\n SALDO: {self.list_saldo[x]}"  # Mostrar o saldo depois desse depósito
                          f"\n DATA: {self.list_data[x]}")  # Mostrar a data do depósito
                    print(35 * "-")

                else:  # Se for negativo, mostrar a mensagem de "SAQUE"
                    print(f" SACOU: {self.list_extrato[x]}"  # Mostrar o valor do saque X 
                          f"\n SALDO: {self.list_saldo[x]}"  # Mostrar o saldo depois desse saque
                          f"\n DATA: {self.list_data[x]}")  # Mostrar a data do saque
                    print(36 * "-")

            print(18 * "=-")

    def ver_conta(self):
        if not self.status:  # Só mostrar as informações da conta se ela estiver ativa
            print("== CONTA INATIVA ==")
        else:
            print(f"""
=======================================
Nº:         {self.num}
DONO:       {self.nome}
TIPO:       {self.tipo}
SALDO:      {self.saldo}
=======================================""")
