import pickle
from Entidades.src.DAO import DAO
from Entidades.Aluno import Aluno


class AlunoDAO(DAO):
    __instance = None

    def __init__(self):
        super().__init__("alunos.pkl")

    def __new__(cls, *args, **kwargs):
        if AlunoDAO.__instance is None:
            AlunoDAO.__instance = object.__new__(cls)

        return AlunoDAO.__instance

    def add(self, matricula, aluno: Aluno):
        if isinstance(aluno, Aluno) and aluno is not None:
            super().add(matricula, aluno)

    def get(self, key):
        return super().get(key)

    def get_all(self):
        return super().get_all()

    def getByCpf(self, key):
        return super().getByCpf(key)

    def remove(self, key):
        return super().remove(key)
