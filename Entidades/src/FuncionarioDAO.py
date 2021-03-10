import pickle
from Entidades.src.DAO import DAO
from Entidades.Funcionario import Funcionario


class FuncionarioDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("funcionarios.pkl")

    def __new__(cls, *args, **kwargs):
        if FuncionarioDAO.__instance is None:
            FuncionarioDAO.__instance = object.__new__(cls)
            return FuncionarioDAO.__instance

    def add(self, matricula, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario) and funcionario is not None:
            super().add(matricula, funcionario)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
