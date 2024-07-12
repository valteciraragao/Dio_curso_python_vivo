from abc import ABC, abstractmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        
    @property
    def endereco(self):
        return self._endereco


class PessoaFisica(Cliente):


    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf


    @property
    def nome(self):
        return self._nome


    @property
    def data_nascimento(self):
        return self._data_nascimento


    @property
    def cpf(self):
        return self._cpf


    def __str__(self):
        return f"Cliente PF: {self._nome} - CPF: {self._cpf} - Endereço: {self._endereco}"


class PessoaJuridica(Cliente):


    def __init__(self, nome_empresa, data_inicio_atividade, cnpj, endereco):
        super().__init__(endereco)
        self._nome_empresa = nome_empresa
        self._data_inicio_atividade = data_inicio_atividade
        self._cnpj = cnpj
        
    @property
    def nome_atividade(self):
        return self._nome_empresa
    
    @property
    def data_inicio_atividadeo(self):
        return self._data_inicio_atividade
    
    @property
    def cnpj(self):
        return self._cnpj
    
    def __str__(self):
        return f"Cliente: {self._nome_empresa} - CPF: {self._cnpj} - Endereço: {self._endereco}"


class Conta(ABC):


    def __init__(self, saldo, numero, agencia, cliente):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()
        
    @abstractmethod
    def sacar(self, valor):
        pass
    
    @abstractmethod
    def depositar(self, valor):
        pass
    
    @abstractmethod
    def saldo(self):
        pass
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
class ContaCorrente(Conta):
    def __init__(self, saldo, numero, agencia, cliente, limite_saque_diario=500):
        super().__init__(saldo, numero, agencia, cliente)
        self._limite_saque_diario = limite_saque_diario
        self._quantidade_saque_diario = 0

    def sacar(self, valor):
        saque_invalido = valor > self._saldo
        excedeu_saque_diario = self._limite_saque_diario < self._limite_saque_diario
        excedeu_valor_limite = valor > self._limite_saque_diario
        
        if saque_invalido:
            print("Saldo insuficiente")
        elif excedeu_saque_diario:
            print("Quantidade diária de saque excedida.")
        elif excedeu_valor_limite:
            print(f"O valor máximo permitido para saque é R$\t{self._limite_saque_diario:.2f}")
        else:
            self._saldo -= valor
            print(f"==== Saque realizado com sucesso R$ {valor:.2f} ====")
            self._historico.adicionar_transacao(f"Saque Conta Corrente\t\tR$\t{valor:.2f}\n")
            self._quantidade_saque_diario += 1

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao(f"Depósito\tR$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"""\
            C/C:\t\t{self._numero}
            Titular:\t{self.cliente.nome}
            Agência:\t\t{self._agencia}
            Saldo: R$\t\t{self._saldo:.2f}
        """


class ContaPoupanca(Conta):
    def __init__(self, saldo, numero, agencia, cliente, taxa_rendimento=0.01, limite_saque_diario=500):
        super().__init__(saldo, numero, agencia, cliente)
        self._taxa_rendimento = taxa_rendimento
        self._limite_saque_diario = limite_saque_diario
        self._quantidade_saque_diario = 0
    
    def sacar(self, valor):
        saque_invalido = valor > self._saldo
        excedeu_valor_limite = valor > self._limite_saque_diario
        
        if saque_invalido:
            print("Saldo insuficiente")
        elif excedeu_valor_limite:
            print(f"O valor máximo permitido para saque é R$\t{self._limite_saque_diario:.2f}")
        else:
            self._saldo -= valor
            print(f"==== Saque realizado com sucesso R$ {valor:.2f} ====")
            self._historico.adicionar_transacao(f"Saque Conta Poupança\t\tR$\t{valor:.2f}\n")
            self._quantidade_saque_diario += 1
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar_transacao(f"Depósito\tR$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")
    
    def saldo(self):
        return self._saldo
    
    def render_juros(self):
        juros = self._saldo * self._taxa_rendimento
        self._saldo += juros
        self._historico.adicionar_transacao(f"Rendimento\tR$ {juros:.2f}")
        print(f"Rendimento de R$ {juros:.2f} aplicado com sucesso!")
    
    def __str__(self):
        return f"""\
            C/P:\t\t{self._numero}
            Titular:\t{self.cliente.nome}
            Agência:\t\t{self._agencia}
            Saldo: R$\t\t{self._saldo:.2f}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y %H:%M:%s"),
            }
        )

    def __str__(self):
        return "\n".join(self._transacoes)


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrador_transacao(self, valor):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrador_transacao(self, conta):
        valida_transacao = conta.sacar(self._valor)
        if valida_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrador_transacao(self, conta):
        valida_transacao = conta.depositar(self._valor)
        if valida_transacao:
            conta.historico.adicionar_transacao(self)


class banco_DIO:
    def __init__(self):
        self.clientes = []
        self.contas = []
        self.numero_conta_corrente = 300
        self.numero_conta_poupanca = 700
        self.AGENCIA = "003"
        
    def cadastrar_cliente(self,tipo_cliente, documento, nome, endereco, data):
              
        if(tipo_cliente == "PF"):
            verifica_cliente = self.verificar_cliente(documento)
            if self.verificar_cliente is None:
                cliente = PessoaFisica(documento, nome, endereco, data)
                self.clientes.append(cliente)
                print(f"Cliente {nome} cadastrado com sucesso!")
        elif(tipo_cliente == "PJ"):
            verifica_cliente = self.verificar_cliente(documento)
            if verifica_cliente is None:
                cliente = PessoaJuridica(documento, nome, endereco, data)
                self.clientes.append(cliente)
                print(f"Cliente {nome} cadastrado com sucesso!")
        else:
            print("Cliente já cadastrado, favor utilizar outro documento.")


    def cadastrar_conta_corrente(self, cliente, saldo=0, limite_saque_diario=1000):
        if self.verificar_conta(cliente) is None:
            conta = ContaCorrente(saldo, self.numero_conta_corrente, self.AGENCIA, cliente, limite_saque_diario)
            self.contas.append(conta)
            self.numero_conta_corrente += 1
            print(f"Conta Corrente criada com sucesso para o cliente {cliente.nome}.")
            return conta
        else:
            print("Cliente já possui uma Conta Corrente.")


    def cadastrar_conta_poupanca(self, cliente, saldo=0, taxa_rendimento=0.01):
        if self.verificar_conta(cliente) is None:
            conta = ContaPoupanca(saldo, self.numero_conta_poupanca, self.AGENCIA, cliente, taxa_rendimento)
            self.contas.append(conta)
            self.numero_conta_poupanca += 1
            print(f"Conta Poupança criada com sucesso para o cliente {cliente.nome}.")
            return conta
        else:
            print("Cliente já possui uma Conta Poupança.")

            
    def verificar_cliente(self, documento):
        for cliente in self.clientes:
            if isinstance(cliente, PessoaFisica) and cliente.cpf == documento:
                return cliente
            elif isinstance(cliente, PessoaJuridica) and cliente.cnpj == documento:
                return cliente
        return None
        
    def verificar_conta(self, cliente):
        valida_conta = [conta for conta in self.contas if conta.cliente == cliente]
        return valida_conta[0] if valida_conta else None

    def menu(self):
        opcoes = """"\n
            #################### Bem-vindo ao DIOBANK o banco que pensa em você! ####################
            Escolha uma opção:
            1\tNovo Cliente
            2\tNova Conta Corrente
            3\tNova Conta Poupança
            4\tRealizar Depósito
            5\tRealizar Saque
            6\tMostrar Extrato
            0\tSair
            ###### => """
        return int(input(opcoes))

    def main(self):
        while True:
            opcao = self.menu()
            
            if opcao == 1:
                print("\t\t######## DIOBANK Cadastro de Cliente ########\t\t\n")
                tipo_cliente = input("""Para continuar informe o tipo de cliente:
                    Pessoa Física digite --> PF;
                    Pessoa Juridica digite --> PJ;
                ==> """).upper()
                if tipo_cliente == "PF":
                    documento = input("CPF:\t")
                    if len(documento) != 11:
                        print("Documento inválido, CPF contém 11 digitos.")
                    nome = input("Nome Completo\t")
                    endereco = input("Endereço: Formato: Logradouro, nro - bairro cidade / UF\t")
                    data = input("Data Nascimento:\t")
                    self.cadastrar_cliente(tipo_cliente, documento, nome, endereco, data)
                elif tipo_cliente == "PJ":
                    documento = input("CNPJ:\t")
                    if len(documento) != 14:
                        print("Documento inválido, CNPJ contém 14 digitos.")
                    nome = input("Nome Empresa\t")
                    endereco = input("Endereço: Formato: Logradouro, nro - bairro cidade / UF\t")
                    data = input("Data de início atividade:\t")
                    self.cadastrar_cliente(tipo_cliente, documento, nome, endereco, data)
                else:
                    print("Opcão inválida, escolha PF ou PJ.")
            elif opcao == 2:
                print("\t\t######## DIOBANK Cadastro de Conta Corrente ########\t\t\n")
                documento_cliente = input("Digite o CPF ou CNPJ do cliente: ")
                cliente = self.verificar_cliente(documento_cliente)
                if cliente:
                    self.cadastrar_conta_corrente(cliente)
                    print(f"{cliente.__str__} sua conta DIOBANK foi criada com sucesso!")
                else:
                    print("###### Cliente não encontrado, aproveite e se cadastre em nosso menu de opções! DIOBANK sempre com você ######")
            elif opcao == 3:
                print("\t\t######## DIOBANK Cadastro de Conta Corrente ########\t\t\n")
                documento_cliente = input("Digite o CPF ou CNPJ do cliente: ")
                cliente = self.verificar_cliente(documento_cliente)
                if cliente:
                    self.cadastrar_conta_corrente(cliente)
                    print(f"{cliente.__str__} sua conta DIOBANK foi criada com sucesso!")
                else:
                    print("###### Cliente não encontrado, aproveite e se cadastre em nosso menu de opções! DIOBANK sempre com você ######")
            elif opcao == 4:
                print("\t\t######## DIOBANK Sistema de Deposito Bancário ########\t\t\n")
                documento_cliente = input("Digite o CPF ou CNPJ do cliente: ")
                cliente = self.verificar_cliente(documento_cliente)
                if cliente:
                    conta = self.verificar_conta(cliente)
                    if conta:
                        valor = float(input("Digite o valor a ser depositado: "))
                        if valor > 0:
                            valida_deposito = input(f"Confirma o deposito no valor de R$  {valor:.2f}" + " Digite s para confirmar / n caso contrário: ").upper()
                            if valida_deposito == 'S':
                                deposito = Deposito(valor)
                                deposito.registrador_transacao(conta)
                            else:
                                print("Deposito R$\t{valor:.2f} não realizado.")
                        else:
                            print("Operação inválida, favor informar um valor válido!")
                    else:
                        print("Operação inválida, favor informar uma conta válido!")
                else:
                    print("Operação inválida, favor informar um cliente válido!")
            elif opcao == 5:
                print("\t\t######## DIOBANK Sistema de Saque Bancário ########\t\t\n")
                documento_cliente = input("Digite o CPF ou CNPJ do cliente: ")
                cliente = self.verificar_cliente(documento_cliente)
                if cliente:
                    conta = self.verificar_conta(cliente)
                    if conta:
                        valor = float(input("Digite o valor que deseja sacar:\t"))
                        saque = Saque(valor)
                        saque.registrador_transacao(conta)
                    else:
                        print("Operação inválida, favor informar um valor válido!")
                else:
                    print("Operação inválida, favor informar um cliente válido!")
            elif opcao == 6:
                print("\t\t######## DIOBANK Sistema de Saque Bancário ########\t\t\n")
                documento_cliente = input("Digite o CPF ou CNPJ do cliente: ")
                cliente = self.verificar_cliente(documento_cliente)
                if cliente:
                    conta = self.verificar_conta
                    if conta:
                        print(conta)
                    else:
                        print("Cliente não possui conta.")
                else:
                    print("Cliente não encontrado.")
            elif opcao == 0:
                print("######## Obrigado por utilizar o DIOBANK, até a próxima! ########")
                break
            else:
                print("Opção inválida. Digite um número válido.")



if __name__ == "__main__":
    banco = banco_DIO()
    banco.main()


