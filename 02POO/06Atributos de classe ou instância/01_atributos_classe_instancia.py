class Estudante:
    escola = 'DIO' #Variavel da classe

    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'
    
def mostrarValores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante('Lucas',1)
aluno2 = Estudante('Renata',2)
mostrarValores(aluno1,aluno2)

Estudante.escola = 'Python'
aluno3 = Estudante('Alice',3)
mostrarValores(aluno1,aluno2,aluno3)