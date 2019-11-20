import pickle
from Entidades.src.DAO import DAO
from Entidades.Funcionario import Funcionario


class FuncionarioDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("funcionarios.pkl")

    def add(self, matricula, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario) and funcionario is not None:
            super().add(matricula, funcionario)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
