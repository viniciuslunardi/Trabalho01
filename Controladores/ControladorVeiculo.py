from Telas.TelaVeiculo import TelaVeiculo
from Entidades.Veiculo import Veiculo

class ControladorVeiculo:
    def __init__(self, controlador_principal):
        self.__tela_veiculo = TelaVeiculo(self)
        self.__veiculos = {}
        self.__veiculos_emprestados = []
        self.__veiculos_disponives = []
        self.__controlador_principal = controlador_principal

    def abre_veiculo(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {0: self.voltar,
                    1: self.cadastra,
                    2: self.lista_veiculo}
        while True:
            opcao = self.__tela_veiculo.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastrar_veiculo(self, placa, modelo, marca, ano, quilometragem_atual, chave):
        try:
            veiculo = Veiculo(placa, modelo, marca, ano, quilometragem_atual, chave)
            if self.existe_veiculo(placa):
                raise Exception
            else:
                self.__veiculos[placa] = veiculo
        except Exception:
            print("---------------ATENÇÃO--------------- \n * Veículo já cadastrado *")

    def existe_veiculo(self, placa):
        return placa in self.__veiculos

    def cadastra(self):
        self.cadastrar_veiculo(input("PLACA: "), input("MODELO: "), input("MARCA: "), input("ANO: "),
                               input("KM ATUAL: "), input("CHAVE: "))

    def lista_veiculo(self):
        if len(self.__veiculos) > 0:
            for placa in self.__veiculos:
                print("PLACA: ", self.__veiculos[placa].placa,
                      "MODELO: ", self.__veiculos[placa].modelo,
                      "MARCA: ", self.__veiculos[placa].marca,
                      "ANO: ", self.__veiculos[placa].ano,
                      "QUILOMETRAGEM ATUAL: ", self.__veiculos[placa].quilometragem_atual,
                      "CHAVE", self.__veiculos[placa].chave)
        else:
            print("Nenhum veículo cadastrado")

    def mostrar_veiculos(self):
        print("MODELO: PLACA: ")
        for placa in self.__veiculos:
            print("%s: %s:", self.__veiculos[placa].modelo, self.__veiculos[placa].placa)

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

    def atualiza_quilometragem(self, placa, km_andado):
        km_atual = float(self.__veiculos[placa].quilometragem_atual)
        float(km_atual)
        km_atual += km_andado
        self.__veiculos[placa].quilometragem_atual = km_atual

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()