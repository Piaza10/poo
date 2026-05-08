class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("O saldo não pode ser negativo")
        else:
            self._saldo = valor

    def saque(self, valor):
        if self._saldo >= valor:
            self.saldo -= valor
            print("Saldo realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposito(self, valor):
        self.saldo += valor

    def extrato(self):
        print(f"Cliente: {self.titular}\n Saldo atual: {self.saldo}")
