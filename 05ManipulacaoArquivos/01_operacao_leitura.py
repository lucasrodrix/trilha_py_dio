arquivo = open('C:/Users/lucas/Projects/python/trilha_py_dio/05ManipulacaoArquivos/loremIpsum.txt', 'r')
print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# while len(linha := arquivo.readline()):
#     print(linha)
arquivo.close()
