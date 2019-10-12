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
                    2: self.filtra_registro,
                    0: self.voltar}
        while True:
            opcao = self.__tela_registro.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastrar_registro(self, registro):
        self.__registros[registro.motivo] = registro

    def lista_registros(self):
        print("---------TODOS OS REGISTROS--------")
        for registro in self.__registros:
            self.imprime_registro(self.__registros[registro])

    @property
    def registros(self):
        return self.__registros

    def imprime_registro(self, registro):
        print(registro)

    def filtra_registro(self):
        numeros_validos = [1, 2]
        print("1: Número de matrícula")
        print("2: Placa de veículo")
        entrada = input("Filtrar por: ")
        filtros = {1: self.filtrar_matricula}
        try:
            inteiro = int(entrada)
            if numeros_validos and inteiro not in numeros_validos:
                raise ValueError
            else:
                filtro = filtros[inteiro]
                filtro()

        except ValueError:
            print("Valor incorreto")
            print("Valores validos: ", numeros_validos)

    def filtrar_matricula(self):
        try:
            matricula = int(input("Digite o número de matricula: "))
            if matricula:
                for registro in self.__registros:
                    if matricula in self.__registros:
                        print(self.__registros[registro])
            else:
                raise ValueError
        except ValueError:
            print("Matrícula deve ser número inteiro")

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
