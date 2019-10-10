from Telas.TelaArmario import TelaArmario
from Entidades.Armario import Armario
from Controladores.ControladorVeiculo import ControladorVeiculo
from Controladores.ControladorFuncionario import ControladorFuncionario


class ControladorArmario:
    def __init__(self, controlador_principal):
        self.__tela_armario = TelaArmario(self)
        self.__chaves = {}
        self.__chaves_emprestadas = []
        self.__chaves_disponiveis = []
        self.__controlador_principal = controlador_principal

    def abre_armario(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {1: self.veiculos_na_garagem, 2: self.pegar_veiculo}
        while True:
            opcao = self.__tela_armario.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def lista__chaves(self):
        for chave in self.__chaves:
            print("CHAVE", chave.chave)

    def veiculos_na_garagem(self):
        veiculos = self.__controlador_principal.controlador_veiculo.veiculos
        print("--------------GARAGEM--------------")
        for veiculo in veiculos:
            print("MODELO: %s PLACA: %s" % (veiculos[veiculo].modelo, veiculos[veiculo].placa))

    def pegar_veiculo(self):
        self.veiculos_na_garagem()
        matricula = input("Digite o seu número de matrícula: ")
        if not self.__controlador_principal.controlador_funcionario.existe_funcionario(matricula):
           print("Não existe funcionário com matrícula '" + str(matricula) + "' cadastrado no sistema")
        else:
            funcionario = self.__controlador_principal.controlador_funcionario.funcionarios
            veiculos = funcionario[matricula].veiculos
            if len(veiculos) > 1:
                placa = input("Digite a placa do veículo que deseja utilizar: ")
                if placa not in veiculos:
                    print("Não existe veículo com placa '" + str(placa) + "' na garagem")
                else:
                    print("Pode pegar a chave")


    def devolver_chave(self):
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

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()