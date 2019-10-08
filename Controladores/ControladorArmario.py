from Telas.TelaArmario import TelaArmario
from Entidades.Armario import Armario


class ControladorArmario:
    def __init__(self):
        self.__tela_armario = TelaArmario(self)
        self.__chaves = []
        self.__chaves_emprestadas = []
        self.__chaves_disponiveis = []

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {0: self.cadastra, 1: self.lista_chavess}
        while True:
            opcao = self.__tela_armario.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastrar_chave(self, chave):
        try:
            chave = Armario(chave)
            if chave not in self.__chaves:
                self.__chaves.append(chave)
            else:
                raise Exception
        except Exception:
            print("Chave já cadastrado")

    def cadastra(self):
        self.cadastrar_chave(input("CHAVE"))

    def lista__chaves(self):
        for chave in self.__chaves:
            print("CHAVE", chave.chave)



    def emprestar_chave(self):
        pass

    def devolver_chave(self):
        pass

    def chaves_disponiveis(self):
        pass



    @property
    def chaves(self):
        return self.__chaves

    @property
    def chaves_emprestadas(self):
        return self.__chaves_emprestadas

    @property
    def chaves_disponiveis(self):
        return self.__chaves_disponiveis
