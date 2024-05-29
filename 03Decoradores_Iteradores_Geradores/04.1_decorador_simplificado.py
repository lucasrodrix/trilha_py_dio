def decorador(funcao):
    def envelope():
        print('Faz algo antes de executar.')
        funcao()
        print('Faz algo depois de exeutar.')

    return envelope

@decorador
def olaMundo():
    print('Olá Mundo!')

olaMundo()