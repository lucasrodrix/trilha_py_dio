#[DIO]Desafio - Criando um Sistema Bancário
'''
Objetivo Geral:
-Iniciar a modelagem do Sistema bancario em POO;
-Adicionar classes para Cliente e as Operações Bancárias: Depósito e Saque;

Desafio:
-Atualizar a implementação do Sistema bancário, para armazenar os dados de clientes e contas bancárias em objetos ao invés de dicionários. O Código deve seguir o modelo de classes UML na imagem fornecida

Extra:
-Após comcluir a modelagem das classes e a criação dos métodos, atualizar os métodos que tratam as opções do menu, para funcionarem com as classes modeladas;
'''

class Historico:
    # Classe Historico
        # Essa classe representa o histórico de transações de uma conta.
    # Atributos:
        # transacoes: uma lista que armazena todas as transações realizadas na conta.
    # Métodos:
        # adicionar_transacao(transacao): adiciona uma nova transação ao histórico.    
    def __init__(self) -> None:
        self.transacoes = list()
    
    def adicionar_transacao(self,transacao):
        self.transacoes.append(transacao)

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
        conta.historico.adicionar_transacao(f'Depósito: R${self.valor:.2f}')

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
            conta.historico.adicionar_transacao('Saque: R${self.valor:.2f}')

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
        # sacar(valor): realiza um saque na conta corrente, respeitando os limites de valor e quantidade de saques diários.

    def __init__(self, saldo, numero_conta, agencia, cliente, valor_limite_saque, limite_saque_diario):
        super().__init__(saldo, numero_conta, agencia, cliente)
        self.valor_limite_saque = valor_limite_saque
        self.limite_saque_diario = limite_saque_diario
        self.saques_diarios = 0

    def sacar(self,valor):
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

def deposito(contas):
    print('=' * 20,'Depósito','=' * 20)
    numero_conta = int(input('Número da Conta: '))

    conta = next((conta for conta in contas if conta.numero_conta == numero_conta),None)
    if conta:
        valor = float(input('Valor do Depósito: R$'))
        conta.depositar(valor)
        print(f'R${valor:.2f} depositado com sucesso.')
    else:
        print('Conta não Encontrada.')

def sacar(contas):
    print('=' * 20, 'Saque', '=' * 20)
    numero_conta = int(input('Número da Conta: '))

    conta = next((conta for conta in contas if conta.numero_conta == numero_conta),None)
    if conta:
        valor = float(input('Valor do Saque:R$'))
        conta.sacar(valor)
    else:
        print('Conta não Encontrada.')

def extrato_bancario(contas):
    print('=' * 20, 'Extrato', '=' * 20)
    numero_conta = int(input('Número da Conta: '))
    
    conta = next((conta for conta in contas if conta.numero == numero_conta), None)
    if conta:
        if not conta.historico.transacoes:
            print('Não foram realizadas movimentações na conta')
        else:
            for movimentacao in conta.historico.transacoes:
                print(movimentacao)
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
    elif opcao == 'q':
        print('Obrigado por Utilizar nosso Sistema.')
        break
    else:
        print('Opção Inválida. Por favor, escolha novamente.')