from Telas.TelaPrincipal import TelaPrincipal
from Controladores.ControladorFuncionario import ControladorFuncionario
from Controladores.ControladorVeiculo import ControladorVeiculo
from Controladores.ControladorArmario import ControladorArmario
from Controladores.ControladorRegistro import ControladorRegistro


class ControladorPrincipal:
    __instance = None

    def __init__(self):
        self.__tela_principal = TelaPrincipal(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_veiculo = ControladorVeiculo(self)
        self.__controlador_armario = ControladorArmario(self)
        self.__controlador_registro = ControladorRegistro(self)

    def __new__(cls, *args, **kwargs):
        if ControladorPrincipal.__instance is None:
            ControladorPrincipal.__instance = object.__new__(cls)
            return ControladorPrincipal.__instance

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        options = {0: self.funcionario, 1: self.veiculo, 2: self.armario, 3: self.registros}
        button, values = self.__tela_principal.open()
        return options[button]()

    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario

    @property
    def controlador_veiculo(self):
        return self.__controlador_veiculo

    @property
    def controlador_armario(self):
        return self.__controlador_armario

    @property
    def controlador_registro(self):
        return self.__controlador_registro

    def funcionario(self):
        self.__controlador_funcionario.abre_funcionario()

    def veiculo(self):
        self.__controlador_veiculo.abre_veiculo()

    def armario(self):
        self.__controlador_armario.abre_armario()

    def registros(self):
        self.__controlador_registro.abre_registros()
