#[DIO]Desafio - Criando um Sistema Bancário
'''
Objetivo Geral: Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar cliente e cadastrar conta bancária;

Desafio: Precisamos criar funções para as operações existentes: Sacar, depositar e extrato; Além disso precisamos criar duas novas funções: Criar Cliente e Criar Conta Corrente(vincular com cliente);

Separação em Funções: Devemos criar funções para todas as operações do sistema. Cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida da melhor forma;

#Saque: A função deve receber os argumentos apenas por nome(keyword only); Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques. Sugestão de Retorno: saldo e extrato;
#Depósito: A função deve receber os argumentos apenas por posição(positional only); Sugestão de argumentos: saldo, valor, extrato. Sugestão de Retorno: saldo e extrato.
#Extrato: a função deve receber os argumentos por posição e nome(positional only e keyword only). Argumentos posicionais: Saldo; Argumentos nomeados: Extrato

-Novas Funções:
#Criar Cliente: O programa deve armazenar os clientes em uma lista, um cliente é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logadouro, numero - bairro - cidade/estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 clientes com o mesmo CPF;
#Criar Conta - O programa deve armazenar as contas em um lista, uma conta é composta por: agencia - numero da conta - cliente. O numero da conta é sequencial, iniciando em 1. o numero da agencia é fixo 0001. o cliente pode ter mais de uma conta, mas a conta não pode ter mais de um cliente;

Dica: Para vincular um usuario a uma conta, filtre a lsita de clientes buscando o numero do CPF informado para cada cliente da lista;
'''

def menu():
    print()
    print('=' * 15,'MENU','=' * 15)
    print('[c] - Novo Cliente')
    print('[a] - Nova Conta')
    print('[l] - Listas Contas')
    print('[d] - Depositar')
    print('[s] - Sacar')
    print('[e] - Extrato')
    print('[q] - Sair')
    print('=' * 15,'MENU','=' * 15)
    print()

def deposito(saldo,extrato):
    print('=' * 20,'Depósito','=' * 20)
    deposito = int(input('Valor do Depósito: R$'))
    print(f'R${deposito:.2f} depositado com sucesso.')
    saldo += deposito
    extrato.append(f'Depósito: R${deposito:.2f}')
    return saldo,extrato

def sacar(saldo, extrato, numero_saques):
    valor_limite_saque = 500
    limite_saque_diario = 3
    print('=' * 20,'Saque','=' * 20)
    saque = int(input('Valor do Saque: R$'))
    if saque > valor_limite_saque:
        print(f'Saque não permitido. Valor limite atingido.({valor_limite_saque})')
    elif saque > saldo:
        print('Saque não Permitido. Saldo insuficiente.')
    elif numero_saques >= limite_saque_diario:
        print(f'Saque não Permitido. Limite diário atingido.({numero_saques})')
    else:
        saldo -= saque
        extrato.append(f'Saque: R${saque:.2f}')
        numero_saques += 1
        print(f'Saque de R${saque:.2f} realizado com sucesso.')
    return saldo, extrato, numero_saques

def extrato_bancario(saldo,extrato):
    print('=' * 20,'Saque','=' * 20)
    if not extrato:
        print('Não foram realizadas movimentações na conta')
    else:
        for movimentacao in extrato:
            print(movimentacao)
    print(f'\tSaldo Atual: R${saldo:.2f}')

def criar_cliente(clientes):
    print('=' * 20,'Criar Cliente','=' * 20)
    cpf = int(input('Informe o CPF[somente números]: '))
    #verifica se o CPF já existe na lista de clientes
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print('CPF já cadastrado.')
            return clientes
        
    nome = str(input('Nome Completo: '))
    data_nasc = str(input('Data de nascimento[dd/mm/aaaa]: '))
    endereco = str(input('Endereço Completo[logadouro,n - bairro - cidade/uf]: '))
    
    clientes.append({'nome':nome, 'data_nasc':data_nasc, 'cpf':cpf, 'endereco':endereco})
    print('Cliente Cadastrado com Sucesso.')
    return clientes
    
def criar_conta(clientes, contas):
    print('=' * 20,'Criar Conta','=' * 20)
    cpf_cliente = int(input('CPF Cliente[somente números]: '))
    numero_conta = len(contas) + 1
    agencia = '0001'
    
    busca_cliente = None
    for cliente in clientes:
        if cliente['cpf'] == cpf_cliente:
            busca_cliente = cliente
            break
    if busca_cliente is None:
        print('Cliente não encontrado. Não é possivel criar a Conta.')
        return contas
    
    contas.append({'agencia':agencia, 'numero_conta':numero_conta, 'cliente':busca_cliente})
    print('Conta criada com Sucesso.')
    return contas

def listar_contas(contas):
    print('=' * 20, 'Lista de Contas', '=' * 20)
    if not contas:
        print('Nenhuma conta cadastrada.')
    else:
        for conta in contas:
            print(f'Agência:{conta['agencia']} | Conta:{conta['numero_conta']} | Cliente:{conta['cliente']['nome']}')


#Programa Principal
saldo = numero_saques = 0
extrato = list()
clientes = list()
contas = list()

while True:
    menu()
    opcao = input('Operação: ').strip().lower()[0]

    if opcao == 'c':
        clientes = criar_cliente(clientes)
    elif opcao == 'a':
        contas = criar_conta(clientes,contas)
    elif opcao == 'l':
        listar_contas(contas)
    elif opcao == 'd':
        saldo,extrato = deposito(saldo,extrato)
    elif opcao == 's':
        saldo,extrato,numero_saques = sacar(saldo,extrato,numero_saques)
    elif opcao == 'e':
        extrato_bancario(saldo,extrato)
    elif opcao == 'q':
        print('Obrigado por Utilizar nosso Sistema.')
        break
    else:
        print('Opção Inválida. Por favor, escolha novamente.')