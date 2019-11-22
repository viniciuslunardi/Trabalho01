class VeiculoJahExisteException(Exception):
    def __init__(self):
        super().__init__("Veículo já cadastrado com essa placa")
