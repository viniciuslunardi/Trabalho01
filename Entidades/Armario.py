class Armario:
    def __init__(self, chaves):
        self.__chaves = chaves
        self.__chaves_disponiveis = []

    @property
    def chaves(self):
        return self.__chaves

    @chaves.setter
    def chaves(self, chaves):
        self.__chaves = chaves

    @property
    def chaves_disponiveis(self):
        return self.__chaves_disponiveis

    @chaves_disponiveis.setter
    def chaves_disponiveis(self, chaves_disponiveis):
        self.__chaves_disponiveis = chaves_disponiveis
