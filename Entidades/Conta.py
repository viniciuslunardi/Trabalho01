
class Conta:
    def __init__(self, agencia, codigo_banco, numero, tipo):
        self.__agencia = agencia
        self.__codigo_banco = codigo_banco
        self.__numero = numero
        self.__tipo = tipo

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def codigo_banco(self):
        return self.__codigo_banco

    @codigo_banco.setter
    def codigo_banco(self, codigo_banco):
        self.__codigo_banco = codigo_banco

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo