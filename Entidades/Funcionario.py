from enum import Enum
from abc import ABC
from .Usuario import Usuario
from .ContaBancaria import ContaBancaria


class Funcionario(ABC, Usuario.Usuario):
    def __init__(self, codigo, senha, nome, cpf, data_nasc, email, agencia, codigo_banco, numero, tipo, carga_horaria, salario):
        super().__init__(codigo, senha, nome, cpf, data_nasc, email)
        self.__conta_bancaria = ContaBancaria(agencia, codigo_banco, numero, tipo)
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
