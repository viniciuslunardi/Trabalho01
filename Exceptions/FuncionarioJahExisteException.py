class FuncionarioJahExisteException(Exception):
    def __init__(self):
        super().__init__("Funcionário já existe com essa matrícula")
