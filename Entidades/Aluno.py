from .Usuario import Usuario
from .Mensalidade import Mensalidade

class Aluno(Usuario.Usuario):
    def __init__(self, cpf, data_nasc, email, codigo, nome, senha, mensalidade, venc_mensalidade):
        super().__init__(cpf, data_nasc, email, codigo, nome, senha)
        self.__ativo = True
        if mensalidade:
            self.__mensalidade = int(mensalidade)
        else:
            self.__mensalidade = 0
        self.__venc_mensalidade = int(venc_mensalidade)

    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    @property
    def mensalidade(self):
        return self.__mensalidade

    @mensalidade.setter
    def mensalidade(self, mensalidade):
        self.__mensalidade = mensalidade

    @property
    def venc_mensalidade(self):
        return self.__venc_mensalidade

    @venc_mensalidade.setter
    def venc_mensalidade(self, venc_mensalidade):
        self.__venc_mensalidade = venc_mensalidade

    def __eq__(self, other):
        return self.__codigo == other.__codigo
