def decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar.')
        funcao(*args, **kwargs)
        print('Faz algo depois de exeutar.')

    return envelope

@decorador
def olaMundo(nome):
    print(f'Olá {nome}!')

olaMundo('Alice')