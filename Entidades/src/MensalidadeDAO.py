import pickle
from Entidades.src.DAO import DAO
from Entidades.Mensalidade import Mensalidade


class MensalidadeDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("mensalidades.pkl")

    def __new__(cls, *args, **kwargs):
        if MensalidadeDAO.__instance is None:
            MensalidadeDAO.__instance = object.__new__(cls)
            return MensalidadeDAO.__instance

    def add(self, identificador, mensalidade: Mensalidade):
        if isinstance(mensalidade, Mensalidade) and mensalidade is not None:
            super().add(identificador, mensalidade)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
