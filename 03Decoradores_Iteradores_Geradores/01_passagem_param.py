def mensagem(nome):
    print('Executando Nome')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('Executando mensagem longa')
    return f'Olá, tudo bem com você {nome}?'

def executar(funcao,nome):
    print('Executando Executar')
    return funcao(nome)

print(executar(mensagem,'Sarah'))
print(executar(mensagem_longa,"Renata"))