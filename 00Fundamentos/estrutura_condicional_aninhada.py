contaNormal = False
contaUniversitaria = False
contaEspecial = True

saldo = 2000
saque = 1500
chequeEspecial = 450

if contaNormal:
    if saldo >= saque:
        print('Saque realizado com sucesso.')
    elif saque <= (saldo + chequeEspecial):
        print('Saque realizado com uso do cheque especial.')
    else:
        print('Não foi possivel realizar o saque, saldo insuficiente.')
elif contaUniversitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso.')
    else:
        print('Saldo insuficiente.')
elif contaEspecial:
    print('Conta Especial Selecionada.')
else:
    print('Sistema não reconheceu o seu tipo de conta, entre em contato com seu gerente.')