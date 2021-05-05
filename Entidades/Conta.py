class Conta():
    def __init__(self, identificador, nome, data_venc, valor, descricao, paga):
        self.__identificador = identificador
        self.__nome = nome
        self.__data_venc = data_venc
        self.__valor = valor
        self.__descricao = descricao
        self.__paga = paga

    @property
    def data_venc(self):
        return self.__data_venc

    @data_venc.setter
    def data_venc(self, data_venc):
        self.__data_venc = data_venc

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def identificador(self):
        return self.__identificador

    @identificador.setter
    def identificador(self, identificador):
        self.__identificador = identificador

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def paga(self):
        return self.__paga

    @paga.setter
    def paga(self, paga):
        self.__paga = paga