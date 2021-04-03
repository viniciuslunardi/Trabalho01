from enum import Enum
from .Usuario import Usuario


class Funcao(Enum):
    GERENTE = 1
    PROFESSOR = 2
    RECEPCIONISTA = 3


class Funcionario(Usuario.Usuario):
    def __init__(self, codigo, senha, nome, cpf, data_nasc, email, conta_bancaria, carga_horaria, salario):
        super().__init__(cpf, data_nasc, email, codigo, nome, senha)
        self.__conta_bancaria = conta_bancaria
        self.__carga_horaria = carga_horaria
        self.__salario = salario

    @property
    def conta_bancaria(self):
        return self.__conta_bancaria

    @conta_bancaria.setter
    def conta_bancaria(self, conta_bancaria):
        self.__conta_bancaria = conta_bancaria

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario
