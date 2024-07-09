from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome, cpf, endereco):
        self._nome = nome
        self._cpf = cpf
        self._endereco = endereco
    
    def __str__(self):
        return f"Cliente: {self._nome} - CPF: {self._cpf} - Endereço: {self._endereco}"
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def endereco(self):
        return self._endereco

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
    
    def __str__(self):
        return f"Conta: {self._numero} - Agência: {self._agencia} - Saldo: R$ {self._saldo:.2f}"

