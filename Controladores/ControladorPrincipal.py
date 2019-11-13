from Telas.TelaPrincipal import TelaPrincipal
from Controladores.ControladorFuncionario import ControladorFuncionario
from Controladores.ControladorVeiculo import ControladorVeiculo
from Controladores.ControladorArmario import ControladorArmario
from Controladores.ControladorRegistro import ControladorRegistro


class ControladorPrincipal:
    def __init__(self):
        self.__tela_principal = TelaPrincipal(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_veiculo = ControladorVeiculo(self)
        self.__controlador_armario = ControladorArmario(self)
        self.__controlador_registro = ControladorRegistro(self)

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        # switcher = {1: self.funcionario,
        #             2: self.veiculo,
        #             3: self.armario,
        #             4: self.registros}
        # while True:
        #     opcao = self.__tela_principal.mostrar_opcoes()
        #     funcao_escolhida = switcher[opcao]
        #     funcao_escolhida()
        (button, value) = self.__tela_principal.open()
        if button == "funcionarios":
            self.funcionario()
        elif button == "veiculos":
            self.veiculo()
        elif button == "armario":
            self.armario()
        else:
            self.registros()

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
