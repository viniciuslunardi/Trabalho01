import datetime

class Mensalidade():
    def __init__(self, identificador, descricao, pago, valor, vencimento):
        self.__identificador = identificador
        self.__descricao = descricao
        self.__pago = pago
        self.__valor = valor
        self.__vencimento = vencimento

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

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
        if self.__pago == False:
            data_atual = datetime.datetime.today()
            [dia, mes, ano] = self.__vencimento.split('/')
            diferenca = data_atual - datetime.datetime(int(ano), int(mes), int(dia))
            if diferenca.days > 30:
                return True
            else:
                return False
        else:
            return False

    def __eq__(self, other):
        return self.__matricula == other.__matricula
