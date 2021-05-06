from .Funcionario import Funcionario

class Recepcionista(Funcionario):
    def __init__(self, codigo, senha, nome, cpf, data_nasc, email, agencia, codigo_banco, numero, tipo, carga_horaria, salario):
        super().__init__(codigo, senha, nome, cpf, data_nasc, email, agencia, codigo_banco, numero, tipo, carga_horaria, salario)