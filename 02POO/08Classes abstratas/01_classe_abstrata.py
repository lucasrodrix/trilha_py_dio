from abc import ABC,abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

    @property
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print('Ligando a TV...')
        print('Ligada!')

    def desligar(self):
        print('Desligando a TV...')
        print('Desligada!')
    @property
    def marca(self):
        return "Philco"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o ArCondicionado...')
        print('Ligado!')

    def desligar(self):
        print('Desligando o ArCondicionado...')
        print('Desligado!')

    @property
    def marca(self):
        return "LG"

controle = ControleTv()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)