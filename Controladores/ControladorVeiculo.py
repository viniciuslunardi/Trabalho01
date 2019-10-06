from Telas.TelaVeiculo import TelaVeiculo
from Entidades.Veiculo import Veiculo


class ControladorVeiculo:
    def __init__(self):
        self.__tela_veiculo = TelaVeiculo(self)
        self.__veiculos = []
        self.__veiculos_emprestados = []
        self.__veiculos_disponives = []

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {0: self.cadastra}
        while True:
            opcao = self.__tela_veiculo.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastrar_veiculo(self, placa, modelo, marca, ano, quilometragem_atual, chave):
        try:
            veiculo = Veiculo(placa, modelo, marca, ano, quilometragem_atual, chave)
            if veiculo not in self.__veiculos:
                self.__veiculos.append(veiculo)
            else:
                raise Exception
        except Exception:
            print("Veículo já cadastrado")

    def cadastra(self):
        self.cadastrar_veiculo(input("PLACA: "), input("MODELO: "), input("MARCA"), input("ANO"),
                               input("KM ATUAL: "), input("CHAVE"))

    def emprestar_veiculo(self):
        pass

    def devolver_veiculo(self):
        pass

    def veiculos_disponiveis(self):
        pass

    def atualizar_veiculo(self):
        pass

    def alterar_veiculo(self):
        pass

    @property
    def veiculos(self):
        return self.__veiculos

    @property
    def veiculos_emprestados(self):
        return self.__veiculos_emprestados

    @property
    def veiculos_disponiveis(self):
        return self.__veiculos_disponives
