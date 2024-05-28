class Pessoa:
    def __init__(self,nome,anoNasc):
        self.nome = nome
        self._anoNasc = anoNasc
    
    @property
    def idade(self):
        _anoAtual = 2024
        return _anoAtual - self._anoNasc
    
pessoa = Pessoa('Lucas',1985)
print(f'Nome: {pessoa.nome} \tIdade: {pessoa.idade}')