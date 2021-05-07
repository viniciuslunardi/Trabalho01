from .Funcionario import Funcionario

class Recepcionista(Funcionario):
    def __init__(self, codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria, salario, pagamentos):
        super().__init__(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria, salario, pagamentos)