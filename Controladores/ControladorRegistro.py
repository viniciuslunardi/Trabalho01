from Telas.TelaRegistro import TelaRegistro
from Entidades.Registro import Registro
from Entidades.Registro import EventoRegistro


class ControladorRegistro:
    def __init__(self):
        self.__tela_registro = TelaRegistro(self)
        self.__registros = []

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {0: self.cadastra, 1: self.lista_registros}
        while True:
            opcao = self.__tela_registro.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastrar_registro(self, data, matricula_funcionario, motivo, placa_veiculo, evento: EventoRegistro):
        try:
            registro = Registro(data, matricula_funcionario, motivo, placa_veiculo, evento)
            if registro not in self.__registros:
                self.__registros.append(registro)
            else:
                raise Exception
        except Exception:
            print("Chave já cadastrado")

    def cadastra(self):
        # AQUI O CADASTRO EH FEITO AUTOMATICAMENTE PELO SISTEMA, NAO SENDO FEITO POR INPUTS DE USUARIO #
        # IMPLEMENTAR A AUTOMACAO CADASTRO DE SISTEMA DE ACORDO COM AS REGRAS #
        self.cadastrar_registro(input(), input(), input(), input(), EventoRegistro(input()))

    def lista__chaves(self):
        for registro in self.__registros:
            print("REGISTRO", registro)


    @property
    def registros(self):
        return self.__registros
