from Telas.TelaPrincipal import TelaPrincipal
from Controladores.ControladorFuncionario import ControladorFuncionario
from Controladores.ControladorVeiculo import ControladorVeiculo

class ControladorPrincipal:
    __instance = None

    def __init__(self):
        self.__tela_principal = TelaPrincipal(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_veiculo = ControladorVeiculo(self)

    def __new__(cls, *args, **kwargs):
        if ControladorPrincipal.__instance is None:
            ControladorPrincipal.__instance = object.__new__(cls)
            return ControladorPrincipal.__instance

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        options = {0: self.funcionario, 1: self.veiculo}
        button, values = self.__tela_principal.open()
        return options[button]()

    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario

    @property
    def controlador_veiculo(self):
        return self.__controlador_veiculo

    def funcionario(self):
        self.__controlador_funcionario.abre_funcionario()

    def veiculo(self):
        self.__controlador_veiculo.abre_veiculo()