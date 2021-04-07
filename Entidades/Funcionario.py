from enum import Enum
from abc import ABC
from .Usuario import Usuario


class Funcionario(ABC, Usuario.Usuario):
    def __init__(self, codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria, salario):
        super().__init__(codigo, senha, nome, cpf, data_nasc, email)
        self.__pix = pix
        self.__carga_horaria = carga_horaria
        self.__salario = salario

    @property
    def pix(self):
        return self.__pix

    @pix.setter
    def pix(self, pix):
        self.__pix = pix

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
