import conta
from cliente import Cliente
from conta import Conta

class Main:
    pass

c1 = Cliente("Miguel", "(21)979849927")

conta = Conta(c1.get_nome(), saldo= 2154, numero= 3387)

conta.deposito(1000)
conta.saque(50)
conta.extrato()


