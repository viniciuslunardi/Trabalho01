from Telas.TelaVeiculo import TelaVeiculo
from Entidades.Veiculo import Veiculo


class ControladorVeiculo:
    def __init__(self, controlador_principal):
        self.__tela_veiculo = TelaVeiculo(self)
        self.__veiculos = {}
        self.__controlador_principal = controlador_principal

    def abre_veiculo(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {0: self.voltar,
                    1: self.cadastra,
                    2: self.lista_veiculo,
                    3: self.alterar_carro,
                    4: self.deletar_carro}
        while True:
            opcao = self.__tela_veiculo.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastrar_veiculo(self, placa, modelo, marca, ano, quilometragem_atual):
        try:
            veiculo = Veiculo(placa, modelo, marca, ano, quilometragem_atual)
            if self.existe_veiculo(placa):
                raise Exception
            else:
                self.__veiculos[placa] = veiculo
        except Exception:
            print("---------------ATENÇÃO--------------- \n * Veículo já cadastrado *")

    def existe_veiculo(self, placa):
        return placa in self.__veiculos

    def cadastra(self):
        while True:
            try:
                placa = input("Informe a placa do veículo: ")
                modelo = input("Informe o modelo do veículo: ")
                marca = input("Informe a marca do veículo: ")
                ano = input("Informe o ano de fabricaçao do veículo:  ")
                if placa == "" or modelo == "" or marca == "" or ano == "":
                    raise Exception
                else:
                    try:
                        km = float(input("Informe quilometragem atual do veículo "))
                        if km:
                            self.cadastrar_veiculo(placa, modelo, marca, ano, km)
                            return
                        else:
                            raise ValueError
                    except ValueError:
                        print("Quilometragem atual deve ser informada em números "
                              " (utilize '.' para números não inteiros)")
            except Exception:
                print("Todos os campos devem ser preenchidos! ")

    def lista_veiculo(self):
        if len(self.__veiculos) > 0:
            for placa in self.__veiculos:
                print("PLACA: ", self.__veiculos[placa].placa,
                      "MODELO: ", self.__veiculos[placa].modelo,
                      "MARCA: ", self.__veiculos[placa].marca,
                      "ANO: ", self.__veiculos[placa].ano,
                      "QUILOMETRAGEM ATUAL: ", self.__veiculos[placa].quilometragem_atual)
        else:
            print("Nenhum veículo cadastrado")

    def mostrar_veiculos(self):
        print("MODELO: PLACA: ")
        for placa in self.__veiculos:
            print("%s: %s:", self.__veiculos[placa].modelo, self.__veiculos[placa].placa)

    @property
    def veiculos(self):
        return self.__veiculos

    def atualiza_quilometragem(self, placa, km_andado):
        km_atual = float(self.__veiculos[placa].quilometragem_atual)
        float(km_atual)
        km_atual += km_andado
        self.__veiculos[placa].quilometragem_atual = km_atual

    def deletar_carro(self):
        placa = (input("Digite a placa do veículo: "))
        if placa in self.__veiculos:
            del self.__veiculos[placa]
            print("Veículo excluido com sucesso")
        else:
            print("Não existe veículo com essa placa cadastrado no sistema")

    def alterar_carro(self):
        while True:
            placa_anterior = (input("Digite a placa do veículo: "))
            if placa_anterior in self.__veiculos:
                print("Informe os novos valores: ")
                placa = (input("Digite o novo valor da placa do veículo: "))
                if placa in self.__veiculos:
                    print("Essa placa já está sendo utilizada por outro veículo")
                else:
                    modelo = (input("Digite o novo valor do modelo do veículo: "))
                    marca = (input("Digite o novo valor da marca do veículo: "))
                    ano = (input("Digite o novo valor do ano de fabricação do veículo: "))
                    try:
                        km = float(input("Digite o novo valor da quilometragem atual do veículo: "))
                        if km:
                            self.__veiculos[placa_anterior].placa = placa
                            self.__veiculos[placa_anterior].modelo = modelo
                            self.__veiculos[placa_anterior].marca = marca
                            self.__veiculos[placa_anterior].ano = ano
                            self.__veiculos[placa_anterior].quilometragem_atual = km
                            print("Veículo alterado com sucesso")
                            return
                        else:
                            raise ValueError
                    except ValueError:
                        print("Quilometragem atual deve ser informada em números "
                              " (utilize '.' para números não inteiros)")
            else:
                print("Não existe veículo com essa placa cadastrado no sistema")
                return

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
