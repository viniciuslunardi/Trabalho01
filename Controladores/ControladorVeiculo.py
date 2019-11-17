from Telas.TelaVeiculo import TelaVeiculo
from Telas.TelaCadastroVeiculo import TelaCadastroVeiculo
from Entidades.Veiculo import Veiculo


class ControladorVeiculo:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_veiculo = TelaVeiculo(self)
        self.__tela_cadastro = TelaCadastroVeiculo(self)
        self.__veiculos = {}
        self.__controlador_principal = controlador_principal

    def __new__(cls, *args, **kwargs):
        if ControladorVeiculo.__instance is None:
            ControladorVeiculo.__instance = object.__new__(cls)
            return ControladorVeiculo.__instance

    def abre_veiculo(self):
        self.abre_tela_inicial()

    @property
    def tela_veiculo(self):
        return self.__tela_veiculo

    def abre_tela_inicial(self):
        veiculos = []
        for placa in self.__veiculos:
            veiculos.append(self.__veiculos[placa].placa + ' - ' +
                            self.__veiculos[placa].marca + ' - ' +
                            self.__veiculos[placa].modelo + ' - ' +
                            self.__veiculos[placa].ano + ' - ' +
                            str(self.__veiculos[placa].quilometragem_atual))

        button, values = self.__tela_veiculo.open(veiculos)
        options = {4: self.voltar,
                   1: self.cadastra,
                   2: self.alterar_carro,
                   3: self.deletar_carro}

        return options[button]()

    def cadastra(self):
        button, values = self.__tela_cadastro.open()
        try:
            placa = values[0]
            modelo = values[1]
            marca = values[2]
            ano = values[3]
            km = float(values[4])
            if km:
                self.cadastrar_veiculo(placa, modelo, marca, ano, km)
            else:
                raise ValueError
        except ValueError:
            print("Quilometragem atual deve ser informada em números "
                  " (utilize '.' para números não inteiros)")
            self.__tela_cadastro.show_message("Erro",
                                              "Quilometragem atual deve ser informada em números "
                                              " (utilize '.' para números não inteiros)")
        self.abre_veiculo()

    def cadastrar_veiculo(self, placa, modelo, marca, ano, quilometragem_atual):
        try:
            veiculo = Veiculo(placa, modelo, marca, ano, quilometragem_atual)
            if self.existe_veiculo(placa):
                raise Exception
            else:
                self.__veiculos[placa] = veiculo
                self.__tela_cadastro.show_message("Sucesso",
                                                  "Veículo cadastrado com sucesso")
                return True
        except Exception:
            print("---------------ATENÇÃO--------------- \n * Veículo já cadastrado *")
            return False

    def existe_veiculo(self, placa):
        return placa in self.__veiculos

    def lista_veiculo(self):
        if len(self.__veiculos) > 0:
            for placa in self.__veiculos:
                return self.__veiculos[placa]
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
                            self.__veiculos[placa] = self.__veiculos.pop(placa_anterior)
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
