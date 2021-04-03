from .Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, codigo, senha, nome, cpf, data_nasc, email, conta_bancaria, carga_horaria, salario):
        super().__init__(cpf, data_nasc, email, codigo, nome, senha, conta_bancaria, carga_horaria, salario)