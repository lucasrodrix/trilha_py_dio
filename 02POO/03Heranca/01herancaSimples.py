class Veiculo:    
    def __init__(self, cor, placa, nroRodas):
        self.cor = cor
        self.placa = placa
        self.nroRodas = nroRodas
        
    def ligarMotor(self):
        print('Ligando Motor...')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'
        
class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):    
    def __init__(self, cor, placa, nroRodas, carregado):
        super().__init__(cor, placa, nroRodas)
        self.carregado = carregado
    
    def carregado(self):
        print(f'{'Sim' if self.carregado else 'Não'} estou Carregafo')
        
moto = Moto('preta','ABC-1234',2)
carro = Carro('branco','LFR-1985',4)
caminhao = Caminhao('roxo','RCF-1983',8,True)
caminhao.ligarMotor()

print(moto)
print(carro)
print(caminhao)