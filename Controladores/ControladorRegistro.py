from Telas.TelaRegistro import TelaRegistro
from Telas.TelaFiltroRegistro import TelaFiltroRegistro
from Entidades.src.RegistrosDAO import RegistroDAO
from Telas.TelaFiltroEvento import TelaFiltroEvento


class ControladorRegistro:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_registro = TelaRegistro(self)
        self.__tela_filtro_evento = TelaFiltroEvento(self)
        self.__registros = {}
        self.__registros_DAO = RegistroDAO()
        self.__chave = 0
        self.__controlador_principal = controlador_principal
        self.__tela_filtro = TelaFiltroRegistro(self)

    def __new__(cls, *args, **kwargs):
        if ControladorRegistro.__instance is None:
            ControladorRegistro.__instance = object.__new__(cls)
            return ControladorRegistro.__instance

    def abre_registros(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self, filtro=None):
        registros = []
        if not filtro:
            for chave in self.__registros_DAO.get_all():
                registros.append("Data: " + str(chave.data) + '  -  ' +
                                 "Matrícula: " + str(chave.matricula_funcionario) + '  -  ' +
                                 "Motivo: " + str(chave.motivo) + '  -  ' +
                                 "Placa: " + str(chave.placa_veiculo) + '  -  ' +
                                 "Evento: " + str(chave.evento))
        else:
            for chave in filtro:
                registros.append("Data: " + str(chave.data) + '  -  ' +
                                 "Matrícula: " + str(chave.matricula_funcionario) + '  -  ' +
                                 "Motivo: " + str(chave.motivo) + '  -  ' +
                                 "Placa: " + str(chave.placa_veiculo) + '  -  ' +
                                 "Evento: " + str(chave.evento))

        button, values = self.__tela_registro.open(registros)
        options = {
            9: self.voltar,
            1: self.filtra_registro,
            2: self.limpa_filtro
        }

        return options[button]()

    def limpa_filtro(self):
        self.abre_registros()

    def cadastrar_registro(self, registro):
        for chave in self.__registros_DAO.get_all():
            print(chave)
            self.__chave += 1
        self.__registros_DAO.add(self.__chave, registro)

    def lista_registros(self):
        print("---------TODOS OS REGISTROS-------")
        for registro in self.__registros_DAO.get_all():
            self.imprime_registro(registro)

    @property
    def registros(self):
        return self.__registros

    def imprime_registro(self, registro):
        print(registro)

    def filtra_registro(self):
        button, values = self.__tela_filtro.open()
        options = {1: self.filtrar_matricula,
                   2: self.filtrar_placa,
                   3: self.filtrar_evento}

        return options[button]()

    def filtrar_evento(self):
        filtro = []
        button, values = self.__tela_filtro_evento.open()
        for registro in self.__registros_DAO.get_all():
            if registro.evento.value == button:
                filtro.append(registro)
        self.abre_tela_inicial(filtro)

    def filtrar_matricula(self):
        filtro = []

        matricula_funcionario = (self.__tela_filtro.ask_verification("Digite o número de matricula: ", "Info"))
        if matricula_funcionario:
            try:
                matricula_funcionario = int(matricula_funcionario)
                for registro in self.__registros_DAO.get_all():
                    if registro.matricula_funcionario == matricula_funcionario:
                        filtro.append(registro)
                self.abre_tela_inicial(filtro)
            except ValueError:
                print("Matrícula deve ser número inteiro")
                self.__tela_filtro.show_message("Erro", "Matrícula deve ser número inteiro")
                self.abre_registros()
        else:
            self.abre_registros()

    def filtrar_placa(self):
        filtro = []
        placa_veiculo = self.__tela_filtro.ask_verification("Digite o número da placa do veículo: ", "Info")
        if placa_veiculo:
            for registro in self.__registros_DAO.get_all():
                if registro.placa_veiculo == placa_veiculo:
                    filtro.append(registro)
            self.abre_tela_inicial(filtro)
        else:
            self.abre_tela_inicial()

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
