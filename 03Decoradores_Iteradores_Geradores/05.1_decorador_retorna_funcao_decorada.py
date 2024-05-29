def decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar.')
        res = funcao(*args, **kwargs)
        print('Faz algo depois de exeutar.')
        return res
    return envelope

@decorador
def olaMundo(nome,argumento):
    print(f'Olá {nome}!')
    return nome.upper()

print(olaMundo('Alice',2500))