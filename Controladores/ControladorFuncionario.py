from Telas.TelaFuncionario import TelaFuncionario
from Entidades.Funcionario import Funcionario
from Entidades.Funcionario import Cargo
from Controladores.ControladorVeiculo import ControladorVeiculo
from Telas.TelaPrincipal import TelaPrincipal


# PARA VEÍCULOS, PRECISAREMOS USAR A CLASSE DE VEÍCULOS :)

class ControladorFuncionario:
    def __init__(self, controlador_principal):
        self.__tela_funcionario = TelaFuncionario(self)
        self.__funcionarios = []
        self.__cargo = None
        self.__controlador_veiculo = ControladorVeiculo
        self.__controlador_principal = controlador_principal


    def abre_funcionario(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {1: self.cadastra, 2: self.lista_funcionario, 3: self.cadastra_veiculos, 4: self.voltar}
        while True:
            opcao = self.__tela_funcionario.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastrar_funcionario(self, numero_matricula, nome, data_nascimento, telefone, veiculos, cargo: Cargo):
        try:

            funcionario = Funcionario(numero_matricula, nome, data_nascimento, telefone, veiculos, cargo)
            if self.existe_funcionario(funcionario):
                raise Exception
            else:
                self.__funcionarios.append(funcionario)
        except Exception:
            print("-----------------ATENÇÃO----------------- \n * Funcionário já cadastrado * ")

    def cadastra(self):
        self.cadastrar_funcionario(input("NÚMERO MATRICULA: "), input("NOME: "), input("DATA NASC: "),
                                   input("TELEFONE"),
                                   input("VEICULOS: "),
                                   Cargo(self.cadastrar_cargo()))

    def cadastrar_cargo(self):
        cargo = {1: Cargo.DIRETORIA, 2: Cargo.RH, 3: Cargo.OPERARIO}
        numeros_validos = [1, 2, 3]
        while True:
            entrada = input("CARGO: \n  * 1: DIRETORIA \n  * 2: RH \n  * 3: OPERARIO \n")
            try:
                inteiro = int(entrada)
                if numeros_validos and inteiro not in numeros_validos:
                    raise ValueError
                else:
                    return inteiro
                # return inteiro
            except ValueError:
                print("Valor incorreto")
                print("Valores validos: ", numeros_validos)

    def cadastra_veiculos(self):
        for veiculo in self.__controlador_veiculo.veiculos:
            print(veiculo.placa)

    def lista_funcionario(self):
        if len(self.__funcionarios) > 0:
            for funcionario in self.__funcionarios:
                print("NÚMERO MATRICULA: ", funcionario.numero_matricula, "NOME: ", funcionario.nome, "DATA NASC: ",
                      funcionario.data_nascimento,
                      "TELEFONE: ", funcionario.telefone,
                      "VEICULOS: ", funcionario.veiculos, "CARGO: ", funcionario.cargo)
            else:
                print("Nenhum funcionário cadastrado")

    def existe_funcionario(self, funcionario):
        return funcionario in self.__funcionarios

    @property
    def funcionarios(self):
        return self.__funcionarios

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
