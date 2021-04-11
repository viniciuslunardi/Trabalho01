import pickle
from Entidades.src.DAO import DAO
from Entidades.Conta import Conta


class ContaDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("contas.pkl")

    def __new__(cls, *args, **kwargs):
        if ContaDAO.__instance is None:
            ContaDAO.__instance = object.__new__(cls)
            return ContaDAO.__instance

    def add(self, identificador, conta: Conta):
        if isinstance(conta, Conta) and conta is not None:
            super().add(identificador, conta)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
