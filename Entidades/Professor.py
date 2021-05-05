from .Funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria, salario):
        super().__init__(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria, salario)