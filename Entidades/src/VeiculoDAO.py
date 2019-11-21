import pickle
from Entidades.src.DAO import DAO
from Entidades.Veiculo import Veiculo


class VeiculoDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("veiculos.pkl")

    def __new__(cls, *args, **kwargs):
        if VeiculoDAO.__instance is None:
            VeiculoDAO.__instance = object.__new__(cls)
            return VeiculoDAO.__instance

    def add(self, placa, veiculo: Veiculo):
        if isinstance(veiculo, Veiculo) and veiculo is not None:
            super().add(placa, veiculo)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
