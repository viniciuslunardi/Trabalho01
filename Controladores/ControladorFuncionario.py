from Telas.TelaFuncionario import TelaFuncionario
from Entidades.Funcionario import Funcionario
from Entidades.Funcionario import Cargo
from Controladores.ControladorVeiculo import ControladorVeiculo
#PARA VEÍCULOS, PRECISAREMOS USAR A CLASSE DE VEÍCULOS :)

class ControladorFuncionario:
    def __init__(self):
        self.__tela_funcionario = TelaFuncionario(self)
        self.__funcionarios = []
        self.__cargo = None

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {0: self.cadastra, 1: self.lista_funcionario}
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
        cargo = {1: Cargo.DIRETORIA, 2: Cargo.RH, 3: Cargo.OPERARIO}
        self.cadastrar_funcionario(input("NÚMERO MATRICULA: "), input("NOME: "), input("DATA NASC: "), input("TELEFONE"),
                               input("VEICULOS: "),
                                   Cargo(self.cadastrar_cargo())) #mostrar opcoes de cargo

    def cadastrar_cargo(self):
        cargo = {1: Cargo.DIRETORIA, 2: Cargo.RH, 3: Cargo.OPERARIO}
        numeros_validos = [1, 2, 3]
        while True:
            entrada = input("CARGO: \n  * 1 = DIRETORIA \n  * 2 = RH \n  * 3 = OPERARIO \n")
            try:
                inteiro = int(entrada)
                if numeros_validos and inteiro not in numeros_validos:
                    raise ValueError
                else:
                    self.__cargo = Cargo(cargo[inteiro])
                return inteiro
            except ValueError:
                print("Valor incorreto")
                print("Valores validos: ", numeros_validos)



    def lista_funcionario(self):
        for funcionario in self.__funcionarios:
            print("NÚMERO MATRICULA: ", funcionario.numero_matricula, "NOME: ", funcionario.nome, "DATA NASC: ", funcionario.data_nascimento,
                  "TELEFONE: ", funcionario.telefone,
                  "VEICULOS: ", funcionario.veiculos, "CARGO: ", funcionario.cargo)

    def existe_funcionario(self, funcionario):
        return funcionario in self.__funcionarios

    @property
    def funcionarios(self):
        return self.__funcionarios

