from enum import Enum


class Funcao(Enum):
    GERENTE = 1
    PROFESSOR = 2
    RECEPCIONISTA = 3


class Funcionario:
    def __init__(self, usuario, senha, nome, cpf, data_nascimento, email, conta_bancaria, carga_horaria, salario, funcao: Funcao):
        self.__usuario = usuario
        self.__senha = senha
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__email = email
        self.__conta_bancaria = conta_bancaria
        self.__carga_horaria = carga_horaria
        self.__salario = salario
        self.__funcao = funcao

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

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

    @property
    def alunos(self):
        return self.__alunos

    @alunos.setter
    def alunos(self, alunos):
        self.__alunos = alunos

    @property
    def funcao(self):
        return self.__funcao

    @funcao.setter
    def funcao(self, funcao):
        self.__funcao = funcao
