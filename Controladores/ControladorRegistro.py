from Telas.TelaRegistro import TelaRegistro
from Telas.TelaFiltroRegistro import TelaFiltroRegistro


class ControladorRegistro:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_registro = TelaRegistro(self)
        self.__registros = {}
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
            for chave in self.__registros:
                registros.append("Data: " + str(self.__registros[chave].data) + '  -  ' +
                                 "Matrícula: " + str(self.__registros[chave].matricula_funcionario) + '  -  ' +
                                 "Motivo: " + str(self.__registros[chave].motivo) + '  -  ' +
                                 "Placa: " + str(self.__registros[chave].placa_veiculo) + '  -  ' +
                                 "Evento: " + str(self.__registros[chave].evento))
        else:
            for chave in filtro:
                registros.append("Data: " + str(self.__registros[chave].data) + '  -  ' +
                                 "Matrícula: " + str(self.__registros[chave].matricula_funcionario) + '  -  ' +
                                 "Motivo: " + str(self.__registros[chave].motivo) + '  -  ' +
                                 "Placa: " + str(self.__registros[chave].placa_veiculo) + '  -  ' +
                                 "Evento: " + str(self.__registros[chave].evento))

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
        chave = self.__chave
        self.__registros[chave] = registro
        self.__chave += 1

    def lista_registros(self):
        print("---------TODOS OS REGISTROS-------")
        for registro in self.__registros:
            self.imprime_registro(self.__registros[registro])

    @property
    def registros(self):
        return self.__registros

    def imprime_registro(self, registro):
        print(registro)

    def filtra_registro(self):
        button, values = self.__tela_filtro.open()
        options = {1: self.filtrar_matricula,
                  # 2: self.filtrar_placa}
                   }
        return options[button]()

    def filtrar_matricula(self):
        filtro = {}
        try:
            matricula_funcionario = int(self.__tela_filtro.ask_verification("Digite o número de matricula: ", "Info"))
            if matricula_funcionario:
                for chave in self.__registros:
                    if self.__registros[chave].matricula_funcionario == matricula_funcionario:
                        filtro[chave] = self.__registros[chave]
                        print(self.__registros[chave])
                self.abre_tela_inicial(filtro)
            else:
                raise ValueError
        except ValueError:
            print("Matrícula deve ser número inteiro")
            self.__tela_filtro.show_message("Erro", "Matrícula deve ser número inteiro")
            self.abre_registros()

    def filtrar_placa(self):
        placa_veiculo = (input("Digite o número da placa do veículo: "))
        if placa_veiculo:
            for chave in self.__registros:
                if self.__registros[chave].placa_veiculo == placa_veiculo:
                    print(self.__registros[chave])

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
