from Telas.TelaRegistro import TelaRegistro
from Entidades.Registro import Registro
from Entidades.Registro import EventoRegistro

class ControladorRegistro:
    def __init__(self, controlador_principal):
        self.__tela_registro = TelaRegistro(self)
        self.__registros = {}
        self.__controlador_principal = controlador_principal

    def abre_registros(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {1: self.lista_registros,
                    2: 0}
        while True:
            opcao = self.__tela_registro.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastrar_registro(self, data, matricula_funcionario, motivo, placa_veiculo, evento: EventoRegistro):
        try:
            registro = Registro(data, matricula_funcionario, motivo, placa_veiculo, evento)
            if registro not in self.__registros:
                self.__registros[registro] = registro
            else:
                raise Exception
        except Exception:
            print("Registro já cadastrado")

    def lista_registros(self):
        for registro in self.__registros:
            print(registro)

    @property
    def registros(self):
        return self.__registros

    def imprime_registro(self, registro):
        print(registro)