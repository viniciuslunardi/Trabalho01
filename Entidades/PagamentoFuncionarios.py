import datetime

class PagamentoFuncionario():
    def __init__(self, identificador, data_pagamento, valor, descricao):
        self.__identificador = identificador
        self.__data_pagamento = data_pagamento
        self.__valor = valor
        self.__descricao = descricao


    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

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
        self.valor = valor

    @property
    def data_pagamento(self):
        return self.__data_pagamento

    @data_pagamento.setter
    def data_pagamento(self, data_pagamento):
        self.__data_pagamento = data_pagamento
