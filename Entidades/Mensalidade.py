from datetime import date

class Mensalidade():
    def __init__(self, descricao, pago, valor, vencimento):
        self.__descricao = descricao
        self.__pago = False
        self.__valor = valor
        self.__vencimento = vencimento

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def pago(self):
        return self.__pago

    @pago.setter
    def pago(self, pago):
        self.__pago = pago

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.valor = valor

    @property
    def vencimento(self):
        return self.__vencimento

    @vencimento.setter
    def vencimento(self, vencimento):
        self.vencimento = vencimento

    @property
    def vencimento(self):
        return self.__vencimento

    @vencimento.setter
    def vencimento(self, vencimento):
        self.vencimento = vencimento

    def verifica_atraso(self):
        if self.__pago == false:
            data_atual = date.today()
            if __vencimento < data_atual and data_atual - __vencimento > 30:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return self.__matricula == other.__matricula
