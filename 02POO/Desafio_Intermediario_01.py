class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.__nome = nome
        self.__numero = numero
        self.__plano = plano

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def plano(self):
        return self.__plano

    @plano.setter
    def plano(self, plano):
        self.__plano = plano

    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

# Entrada:
nome = input()  
numero = input()  
plano = input()  

# Criação de um novo objeto `UsuarioTelefone` com os dados fornecidos:
usuario = UsuarioTelefone(nome, numero, plano)

# Imprime a representação em string do objeto:
print(usuario)
