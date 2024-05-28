class Conta:
    def __init__(self, nroAgencia, saldo=0):
        self.nroAgencia = nroAgencia
        self._saldo = saldo
        
    def depositar(self,valor):
        self._saldo += valor
        
    def sacar(self,valor):
        self._saldo -= valor
        
    def mostrarSaldo(self):
        return self._saldo
    
conta = Conta('0001',100)
conta.depositar(100)
print(conta.nroAgencia)
print(conta.mostrarSaldo())