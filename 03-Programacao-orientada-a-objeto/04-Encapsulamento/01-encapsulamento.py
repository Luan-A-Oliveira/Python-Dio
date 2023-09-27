class Conta:
    def __init__(self,nro_ag, saldo=0):
        self._saldo = saldo
        self.nro_ag = nro_ag
    
    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self):
        return self._saldo

conta = Conta('0001', 100)
conta.depositar(100)
print(conta.nro_ag)
print(conta.mostrar_saldo())
