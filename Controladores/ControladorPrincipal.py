from Telas.TelaPrincipal import TelaPrincipal
from Controladores.ControladorFuncionario import ControladorFuncionario
from Controladores.ControladorVeiculo import ControladorVeiculo
from Controladores.ControladorArmario import ControladorArmario
from Controladores.ControladorRegistro import ControladorRegistro


class ControladorPrincipal:
    def __init__(self):
        self.__tela_principal = TelaPrincipal(self)
        self.__controlador_funcionario = ControladorFuncionario
        self.__controlador_veiculo = ControladorVeiculo
        self.__controlador_armario = ControladorArmario
        self.__controlador_registro = ControladorRegistro

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {0: self.funcionario, 1: self.veiculo, 2: self.armario, 3: self.registros}
        while True:
            opcao = self.__tela_principal.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def funcionario(self):
        self.__controlador_funcionario().inicia()

    def veiculo(self):
        self.__controlador_veiculo().inicia()

    def armario(self):
        self.__controlador_armario().inicia()

    def registros(self):
        self.__controlador_registro().inicia()
