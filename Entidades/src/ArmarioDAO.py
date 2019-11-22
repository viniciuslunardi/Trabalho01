import pickle
from Entidades.src.DAO import DAO
from Entidades.Veiculo import Veiculo


class ArmarioDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("armario.pkl")

    def __new__(cls, *args, **kwargs):
        if ArmarioDAO.__instance is None:
            ArmarioDAO.__instance = object.__new__(cls)
            return ArmarioDAO.__instance

    def add(self, placa, veiculo: Veiculo):
        super().add(placa, veiculo)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
