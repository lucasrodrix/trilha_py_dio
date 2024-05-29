#[DIO]Desafio - Criando um Sistema Bancário
'''
Implementar as funcionalidades:
-Estabelecer um limite de 10 transações diárias por conta;
-Se o usuario tentar fazer uma transação após atingir o limite, deve ser informado que ele excedeu o número de transações permitidas para aquele dia;
-Mostre no estrato, a data e hora de todas as transações;
'''
from datetime import datetime

class Historico:
    # Classe Historico
        # Essa classe representa o histórico de transações de uma conta.
    # Atributos:
        # transacoes: uma lista que armazena todas as transações realizadas na conta.
    # Métodos:
        # adicionar_transacao(transacao): adiciona uma nova transação ao histórico.
        # gerar_relatorio(tipo_transacao): Permite filtrar transações por tipo.
        # transacoes_dia(): Permite filtrar as transações realizadas no dia atual
    def __init__(self) -> None:
        self.transacoes = list()
    
    def adicionar_transacao(self,transacao):
        self.transacoes.append(transacao)
    
    def gerar_relatorio(self,tipo_transacao=None):
        if tipo_transacao:
            return(transacao for transacao in self.transacoes if transacao.lower().startswith(tipo_transacao.lower()))
        else:
            return iter(self.transacoes)
        
    def transacoes_dia(self):
        hoje = datetime.now().date()
        return[transacao for transacao in self.transacoes if transacao['data'.date() == hoje]]

class Transacao:
    # Classe Transacao
        # Essa é uma classe abstrata para representar uma transação genérica. Não possui atributos específicos e define um método abstrato que deve ser implementado pelas classes filhas.
    # Métodos:
        # registrar(conta): método abstrato para registrar uma transação na conta. As classes filhas devem implementar esse método.
    def registrar(self,conta):
        pass

class Deposito(Transacao):
    # Classe Deposito
        # Essa classe representa a operação de depósito.
    # Atributos:
        # valor: valor a ser depositado.
    # Métodos:
        # registrar(conta): adiciona o valor do depósito ao saldo da conta e registra a transação no histórico.    
    def __init__(self,valor):
        self.valor = valor
    
    def registrar(self, conta):
        conta.saldo += self.valor
        transacao = {'tipo':'Depósito','valor':self.valor,'data':datetime.now(),'descricao':f'Depósito: R${self.valor:.2f}'}
        conta.historico.adicionar_transacao(transacao)

class Saque(Transacao):
    # Classe Saque
        # Essa classe representa a operação de saque.
    # Atributos:
        # valor: valor a ser sacado.
    # Métodos:
        # registrar(conta): verifica se há saldo suficiente e, se houver, subtrai o valor do saque do saldo da conta e registra a transação no histórico. Se o saldo for insuficiente, exibe uma mensagem de erro.
    def __init__(self,valor):
        self.valor = valor
    
    def registrar(self, conta):
        if self.valor > conta.saldo:
            print('Saque não permitido. Saldo Insuficiente.')
        else:
            conta.saldo -= self.valor
            transacao = {'tipo':'Saque','valor':self.valor,'data':datetime.now(),'descricao':f'Saque: R${self.valor:.2f}'}
            conta.historico.adicionar_transacao(transacao)

class Conta:
    # Classe Conta
        # Essa classe representa uma conta bancária genérica.
    # Atributos:
        # saldo: saldo atual da conta.
        # numero: número da conta.
        # agencia: agência da conta.
        #cliente: cliente proprietário da conta.
        # historico: objeto da classe Historico para armazenar as transações da conta.
    # Métodos:
        # saldo_atual(): retorna o saldo atual da conta.
        # sacar(valor): realiza a operação de saque, chamando o método registrar da classe Saque.
        # depositar(valor): realiza a operação de depósito, chamando o método registrar da classe Deposito.
    def __init__(self,saldo,numero_conta,agencia,cliente):
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def saldo_atual(self):
        return self.saldo
    
    def sacar(self,valor):
        saque = Saque(valor)
        saque.registrar(self)

    def depositar(self,valor):
        deposito = Deposito(valor)
        deposito.registrar(self)

class ContaCorrente(Conta):
    # Classe ContaCorrente
        # Essa classe representa uma conta corrente, que é um tipo específico de conta bancária.
    # Atributos:
        # valor_limite_saque: limite de valor para saque da conta.
        # limite_saque_diario: número máximo de saques permitidos por dia.
    # Métodos:
        # Herdados da classe Conta.
        # sacar(valor): realiza um saque na conta corrente, respeitando os limites de valor, quantidade de saques diários e limite de transações diarias.
        # depositar(valor): realiza um deposito na conta corrente respeitando limite de transações diarias.

    def __init__(self, saldo, numero_conta, agencia, cliente, valor_limite_saque, limite_saque_diario):
        super().__init__(saldo, numero_conta, agencia, cliente)
        self.valor_limite_saque = valor_limite_saque
        self.limite_saque_diario = limite_saque_diario
        self.saques_diarios = 0

    def sacar(self,valor):
        transacoes_hoje = self.historico.transacoes_dia()
        if len(transacoes_hoje) >= 10:
            print('Limite diário de transações atingido')
            return
        if valor > self.valor_limite_saque:
            print(f'Saque não permitido. Valor limite de R${self.valor_limite_saque:.2f} atingido.')
        elif valor > self.saldo:
            print('Saque não permitido. Saldo insuficiente.')
        elif self.saques_diarios >= self.limite_saque_diario:
            print(f'Saque não permitido. Limite diário de {self.limite_saque_diario} saques atingido.')
        else:
            super().sacar(valor)
            self.saques_diarios += 1
            print(f'Saque de R${valor:.2f} realizado com sucesso.')

    def depositar(self, valor):
        transacoes_hoje = self.historico.transacoes_dia()
        if len(transacoes_hoje) >= 10:
            print('Limite diário de transações atingido')
            return
        super().depositar(valor)
        print(f'Depósito de R${valor:.2f} realizado com sucesso.')

class Cliente:
    # Classe Cliente
        # Essa classe representa um cliente do banco.
    # Atributos:    
        # endereco: endereço do cliente.
        # contas: lista de contas associadas ao cliente.
    # Métodos:
        # adicionar_conta(conta): adiciona uma conta à lista de contas do cliente.
        # realizar_transacao(conta, transacao): realiza uma transação na conta especificada.
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas = list()

    def adicionar_conta(self,conta):
        self.contas.append(conta)

    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)

class PessoaFisica(Cliente):
    # Classe PessoaFisica
        # Essa classe representa um cliente do tipo pessoa física, que herda de Cliente.
    # Atributos:
        # cpf: CPF do cliente.
        # nome: nome do cliente.
        # data_nasc: data de nascimento do cliente.
    # Métodos:
        # Herdados da classe Cliente.    
    def __init__(self, endereco,cpf,nome,data_nasc):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nasc = data_nasc

class ContaIterador:
    def __init__(self,contas) -> None:
        self.contas = contas
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._contas):
            conta = self._contas[self._index]
            self._index += 1
            return conta
        raise StopIteration



def log_transacao(func):
    def envelope(*args,**kwargs):
        now = datetime.now().strftime('%Y.%m.%d %H:%M:%S')
        res = func(*args,**kwargs)
        print(f'[{now}] Transação: {func.__name__.capitalize()}')
        return res
    return envelope

def menu():
    print()
    print('=' * 15,'MENU','=' * 15)
    print('[c] - Novo Cliente')
    print('[a] - Nova Conta')
    print('[l] - Listas Contas')
    print('[d] - Depositar')
    print('[s] - Sacar')
    print('[e] - Extrato')
    print('[r] - Relatório de Transações')
    print('[q] - Sair')
    print('=' * 15,'MENU','=' * 15)
    print()

@log_transacao
def deposito(contas):
    print('=' * 20,'Depósito','=' * 20)
    numero_conta = int(input('Número da Conta: '))

    conta = next((conta for conta in contas if conta.numero_conta == numero_conta),None)
    if conta:
        valor = float(input('Valor do Depósito: R$'))
        conta.depositar(valor)
    else:
        print('Conta não Encontrada.')

@log_transacao
def sacar(contas):
    print('=' * 20, 'Saque', '=' * 20)
    numero_conta = int(input('Número da Conta: '))

    conta = next((conta for conta in contas if conta.numero_conta == numero_conta),None)
    if conta:
        valor = float(input('Valor do Saque:R$'))
        conta.sacar(valor)
    else:
        print('Conta não Encontrada.')

@log_transacao
def extrato_bancario(contas):
    print('=' * 20, 'Extrato', '=' * 20)
    numero_conta = int(input('Número da Conta: '))
    
    conta = next((conta for conta in contas if conta.numero_conta == numero_conta),None)
    if conta:
        if not conta.historico.transacoes:
            print('Não foram realizadas movimentações na conta')
        else:
            for movimentacao in conta.historico.transacoes:
                data = movimentacao['data'].strftime('%Y=%m-%d %H:%M:%S')
                print(f'{data} - {movimentacao['descricao']}')
        print(f'\tSaldo Atual: R${conta.saldo_atual():.2f}')
    else:
        print('Conta não encontrada.')

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
    
    novo_cliente = PessoaFisica(endereco,cpf,nome,data_nasc)
    clientes.append(novo_cliente)
    print('Cliente Cadastrado com Sucesso.')
    return clientes
    
def criar_conta(clientes, contas):
    print('=' * 20, 'Criar Conta', '=' * 20)
    cpf_cliente = int(input('CPF Cliente[somente números]: '))
    numero_conta = len(contas) + 1
    agencia = '0001'
    
    cliente = next((cliente for cliente in clientes if cliente.cpf == cpf_cliente), None)
    if cliente is None:
        print('Cliente não encontrado. Não é possível criar a Conta.')
        return contas
    
    conta_corrente = ContaCorrente(0, numero_conta, agencia, cliente, 500, 3)
    contas.append(conta_corrente)
    print('Conta criada com Sucesso.')
    return contas

def listar_contas(contas):
    print('=' * 20, 'Lista de Contas', '=' * 20)
    if not contas:
        print('Nenhuma conta cadastrada.')
    else:
        for conta in contas:
            print(f'Agência: {conta.agencia} | Conta: {conta.numero_conta} | Cliente: {conta.cliente.nome}')

def relatorio_transacoes(contas):
    print('=' * 20, 'Relatório de Transações', '=' * 20)
    numero_conta = int(input('Número da Conta: '))

    conta = next((conta for conta in contas if conta.numero_conta == numero_conta),None)
    if conta:
        tipo_transacao = input('Digite o tipo de Transação[Depósito/Saque/Todos(emBranco)]: ')
        relatorio = conta.historico.gerar_relatorio(tipo_transacao)

        print(f'Relatório de Transações para a Conta Nº:{numero_conta}')
        for transacao in relatorio:
            print(transacao)
    else:
        print('Conta não Encontrada.')



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
        contas = criar_conta(clientes, contas)
    elif opcao == 'l':
        listar_contas(contas)
    elif opcao == 'd':
        deposito(contas)
    elif opcao == 's':
        sacar(contas)
    elif opcao == 'e':
        extrato_bancario(contas)
    elif opcao == 'r':
        relatorio_transacoes(contas)
    elif opcao == 'q':
        print('Obrigado por Utilizar nosso Sistema.')
        break
    else:
        print('Opção Inválida. Por favor, escolha novamente.')