class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criarPorDataNasc(cls,ano,mes,dia,nome):
        idade = 2024 - ano
        return cls(nome,idade)
    
    @staticmethod
    def maioridade(idade):
        return idade >= 18
    
p = Pessoa.criarPorDataNasc(1985, 6, 22, "Lucas")
print(p.nome, p.idade)

print(Pessoa.maioridade(18))
print(Pessoa.maioridade(8))