
class Veiculo:
    def __init__(self, placa, modelo, marca, ano, quilometragem_atual, chave):
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__quilometragem_atual = quilometragem_atual
        self.__chave = chave

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def quilometragem_atual(self):
        return self.__quilometragem_atual

    @quilometragem_atual.setter
    def quilometragem_atual(self, quilometragem_atual):
        self.__quilometragem_atual = quilometragem_atual

    @property
    def chave(self):
        return self.__chave

    @chave.setter
    def chave(self, chave):
        self.__chave = chave

    def __eq__(self, other):
        return self.__placa == other.placa