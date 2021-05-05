from .Usuario import Usuario
from .Mensalidade import Mensalidade
from datetime import datetime


class Aluno(Usuario.Usuario):
    def __init__(self, cpf, data_nasc, email, codigo, nome, senha, mensalidade, venc_mensalidade):
        super().__init__(codigo, senha, nome, cpf, data_nasc, email)
        self.__ativo = True

        if mensalidade:
            current_month = datetime.now().strftime('%m')
            current_year_full = datetime.now().strftime('%Y')

            if current_month == 12:
                venc_month = "01"
                venc_year = str(int(current_year_full) + 1)
            else:
                venc_month = str(int(current_month) + 1)
                venc_year = str(current_year_full)

            self.__mensalidades = [Mensalidade("Primeira mensalidade", False, int(mensalidade),
                                             vencimento=venc_mensalidade + "/" + venc_month + "/" + venc_year)]
            self.__valor_mensalidade = int(mensalidade)
        else:
            self.__mensalidades = []
        if venc_mensalidade:
            self.__venc_mensalidade = int(venc_mensalidade)
        else:
            self.__venc_mensalidade = 1


    @property
    def ativo(self):
        return self.__ativo

    @ativo.setter
    def ativo(self, ativo):
        self.__ativo = ativo

    @property
    def valor_mensalidade(self):
        return self.__valor_mensalidade

    @valor_mensalidade.setter
    def valor_mensalidade(self, valor_mensalidade):
        self.__valor_mensalidade = valor_mensalidade

    @property
    def mensalidades(self):
        return self.__mensalidades

    @mensalidades.setter
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
            if mensalidade.verifica_atraso():
                return True
            else:
                return False

    def __eq__(self, other):
        return self.__codigo == other.__codigo
