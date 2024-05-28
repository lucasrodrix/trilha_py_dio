class Passaro:
    def voar(self):
        print('Voando...')

class Pardal(Passaro):
    def voar(self):
        print('Pardal pode Voar...')
    
class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não pode voar.')

#FIXME: exemplo ruim de uso de herança para 'ganhar' o método voar;
class Aviao(Passaro):
    def voar(self):
        print('Avião está decolando...')

def planoVoo(obj):
    obj.voar()

planoVoo(Pardal())
planoVoo(Avestruz())
planoVoo(Aviao())