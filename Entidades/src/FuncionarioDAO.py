import pickle
from Entidades.src.DAO import DAO
from Entidades.Funcionario import Funcionario


class FuncionarioDAO(DAO):
    instance = None

    def __init__(self):
        super().__init__("funcionarios.pkl")

    def __new__(cls, *args, **kwargs):
        if FuncionarioDAO.instance is None:
            FuncionarioDAO.instance = object.__new__(cls)
            return FuncionarioDAO.instance

    def add(self, matricula, funcionario: Funcionario):
        if isinstance(funcionario, Funcionario) and funcionario is not None:
            super().add(matricula, funcionario)

    def get(self, key):
        return super().get(key)

    def remove(self, key):
        return super().remove(key)
