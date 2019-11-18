from enum import Enum


class Cargo(Enum):
    DIRETORIA = 1
    COMERCIAL = 2
    DESENVOLVEDOR = 3


class Funcionario:
    def __init__(self, numero_matricula, nome, data_nascimento, telefone, cargo: Cargo):
        self.__numero_matricula = numero_matricula
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__telefone = telefone
        self.__cargo = cargo
        self.__tentativas = 0
        self.__veiculos = {}
        self.__veiculo_usado = {}
        self.__bloqueado = False

    @property
    def numero_matricula(self):
        return self.__numero_matricula

    @numero_matricula.setter
    def numero_matricula(self, numero_matricula):
        self.__numero_matricula = numero_matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def veiculos(self):
        return self.__veiculos

    @veiculos.setter
    def veiculos(self, veiculos):
        self.__veiculos = veiculos

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

    @property
    def veiculo_usado(self):
        return self.__veiculo_usado

    @veiculo_usado.setter
    def veiculo_usado(self, veiculo_usado):
        self.__veiculo_usado = veiculo_usado

    @property
    def bloqueado(self):
        return self.__bloqueado

    @bloqueado.setter
    def bloqueado(self, bloqueado):
        self.__bloqueado = bloqueado

    @property
    def tentativas(self):
        return self.__tentativas

    @tentativas.setter
    def tentativas(self, tentativas):
        self.__tentativas = tentativas

    def __eq__(self, other):
        return self.__numero_matricula == other.numero_matricula
