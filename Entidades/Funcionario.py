from enum import Enum


class Cargo(Enum):
    DIRETORIA = 1
    RH = 2
    OPERARIO = 3


class Funcionario:
    def __init__(self, numero_matricula, nome, data_nascimento, telefone, cargo: Cargo):
        self.__numero_matricula = numero_matricula
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__telefone = telefone
        self.__cargo = cargo
        self.__veiculos = {}

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

    def __eq__(self, other):
        return self.__numero_matricula == other.numero_matricula
