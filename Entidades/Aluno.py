from .Usuario import Usuario
from .Mensalidade import Mensalidade

class Aluno(Usuario.Usuario):
    def __init__(self, cpf, data_nasc, email, codigo, nome, senha, mensalidades, venc_mensalidade):
        super().__init__(cpf, data_nasc, email, codigo, nome, senha)
        self.__ativo = True
        self.mensalidades = mensalidades
        self.__venc_mensalidade = int(venc_mensalidade)

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    @property
    def mensalidades(self):
        return self.__mensalidades

    @mensalidade.setter
    def mensalidades(self, mensalidades):
        self.__mensalidades = mensalidades

    @property
    def venc_mensalidade(self):
        return self.__venc_mensalidade

    @venc_mensalidade.setter
    def venc_mensalidade(self, venc_mensalidade):
        self.__venc_mensalidade = venc_mensalidade

    def tem_mensalidade_atrasada(self):
        for mensalidade in self.mensalidades:
            if mensalidade.verifica_atraso:
                return true
            else:
                return false

    def __eq__(self, other):
        return self.__codigo == other.__codigo
