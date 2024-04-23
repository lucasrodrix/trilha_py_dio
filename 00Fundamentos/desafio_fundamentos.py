#[DIO]Desafio - Criando um Sistema Bancário
'''
Para a primeira versão do sistema devemos implementar apenas operações: deppósito, saque e extrato;

#Operação de Depósito: deve ser possivel depositar valores positivos para a conta bancária; A v1 do projeto trabalha apenas com um usuário, dessa forma não será necessário identificar o número da agencia e conta bancária; Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato;

#Operação de Saque: deve permitir realizar 3(três) saques diários com limite máximo de 500 por saque; Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o valor por falta de saldo; Todos os saques devem ser armazenados em uma variável e exibidos na operação extrato;

#Operação de Extrato: essa operação deve listar todos os depósitos e saques realizados na conta; No fim da listagem deve ser exibido o saldo atual da conta; Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações. Os valores devem ser exibidos utilizando o formato R$ xxx.xx;
'''

menu = f'''
    ============= MENU =============
    
        [d] - Depositar
        [s] - Sacar
        [e] - Extrato
        [q] - Sair
        
    ================================
    '''
saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print(menu)
    opt = str(input('Escolha a opção desejada: ')).lower().strip()[0]
    if opt == 'd':
        print(f'''\n============= Depósito =============\n''')
        deposito = int(input('Valor a ser depositado: R$ '))
        print(f'Valor de R$ {deposito:.2f} realizado em sua conta.')
        saldo += deposito
        extrato += f'Depósito: R$ {deposito:.2f}\n'
    elif opt == 's':
        print(f'''\n============= Saque =============\n''')
        saque = int(input('Valor do Saque: R$ '))
        if saque > limite:
            print('Saque não permitido. Valor ultrapassa o limite por saque.[500]')
        elif saque > saldo:
            print('Saque não perimitido. Valor maior que o saldo da Conta')
        elif numero_saques == LIMITE_SAQUES:
            print('Saque não permitido. Limite diário atingido.[3]')
        else:
            saldo -= saque
            numero_saques += 1
            extrato += f'Saque: R${saque:.2f}\n'
            print(f'Realizado o saque de R${saque:.2f}')                
    elif opt == 'e':
        print(f'''\n============= Extrato =============\n''')
        if extrato == '':
            print('Não foram realizadas movimentações na conta.')
        else:
            print(extrato)
        print(f'\tSaldo Atual: R${saldo:.2f}')
    elif opt == 'q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
print('Obrigado por usar nosso Sistema!')