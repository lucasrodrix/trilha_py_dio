nome = "Lucas"
idade = 38
profissao = "Programador"
linguagem = "Python"
saldo = 2063.00

pessoa = {'nome':'Lucas','idade':38,'profissao':'Programador','linguagem':'Python'}#Dicionario

#OldStyle %
print('Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s.'%(nome,idade,profissao,linguagem))

#Método format
print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}'.format(linguagem,profissao,idade,nome))
print('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(nome=nome,idade=idade,profissao=profissao,linguagem=linguagem))
print('Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.'.format(**pessoa))

#fstring
print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.')

print(f'Nome: {nome} - Idade: {idade} - Saldo: R${saldo:.2f}')
