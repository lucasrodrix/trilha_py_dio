arquivo = open('C:/Users/lucas/Projects/python/trilha_py_dio/05ManipulacaoArquivos/OperacaoEscrita.txt', 'w')

arquivo.write('Escrevendo dados em um novo arquivo.')
arquivo.writelines(['\n','Escrevendo','\n', 'um','\n', 'novo','\n', 'texto'])

arquivo.close()