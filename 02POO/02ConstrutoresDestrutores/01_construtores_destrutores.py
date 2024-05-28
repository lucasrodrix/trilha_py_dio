class Cachorro:
    def __init__(self, nome, cor, acordado = True) -> None:
        print('Inicializando a Classe')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def falar(self):
        print('Auau')
    
    def __del__(self):
        print('Removendo a instancia da classe')
    
def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()