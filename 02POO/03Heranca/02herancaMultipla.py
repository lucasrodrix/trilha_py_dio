class Animal:
    def __init__(self, nroPatas):
        self.nroPatas = nroPatas
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'

class Mamifero(Animal):
    def __init__(self, corPelo, **kw):
        super().__init__(**kw)
        self.corPelo = corPelo

class Ave(Animal):
    def __init__(self, corBico, **kw):
        super().__init__(**kw)
        self.corBico = corBico

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero,Ave):
    def __init__(self, corBico, corPelo, nroPatas):
        super().__init__(corPelo=corPelo, corBico=corBico, nroPatas=nroPatas)
        print(Ornitorrinco.__mro__)
        

print(Gato(nroPatas = 4,corPelo='Preto'))
print(Ornitorrinco(nroPatas=4, corPelo='Marrom', corBico = 'Laranja'))