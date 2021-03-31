from .Usuario import Usuario


class Aluno(Usuario.Usuario):
    def __init__(self, cpf, data_nasc, email, matricula, nome, senha, mensalidade, venc_mensalidade):
        super().__init__(cpf, data_nasc, email, matricula, nome, senha)
        self.__ativo = True
        self.__mensalidade = mensalidade
        self.__venc_mensalidade = venc_mensalidade

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
        return self.__matricula == other.__matricula
