class ContaJahExisteException(Exception):
    def __init__(self):
        super().__init__("Conta já existe com esse identificador")
