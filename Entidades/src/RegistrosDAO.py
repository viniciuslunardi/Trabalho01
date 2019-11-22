import pickle
from Entidades.src.DAO import DAO
from Entidades.Registro import Registro


class RegistroDAO(DAO):
    instance = None

    def __init__(self):
        super().__init__("registros.pkl")

    def __new__(cls, *args, **kwargs):
        if RegistroDAO.instance is None:
            RegistroDAO.instance = object.__new__(cls)
            return RegistroDAO.instance

    def add(self, key, registro: Registro):
        super().add(key, registro)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
