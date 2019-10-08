from Telas.TelaFuncionario import TelaFuncionario
from Entidades.Funcionario import Funcionario
from Entidades.Funcionario import Cargo
#PARA VEÍCULOS, PRECISAREMOS USAR A CLASSE DE VEÍCULOS :)

class ControladorFuncionario:
    def __init__(self):
        self.__tela_funcionario = TelaFuncionario(self)
        self.__funcionarios = []

    def inicia(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {0: self.cadastra, 1: self.lista_funcionario()}
        while True:
            opcao = self.__tela_funcionario.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastrar_funcionario(self, numero_matricula, nome, data_nascimento, telefone, veiculos, cargo: Cargo):
        try:
            funcionario = Funcionario(numero_matricula, nome, data_nascimento, telefone, veiculos, cargo)
            if funcionario not in self.__funcionarios:
                self.__funcionarios.append(funcionario)
            else:
                raise Exception
        except Exception:
            print("Funcionário já cadastrado")

    def cadastra(self):
        self.cadastrar_funcionario(input("NÚMERO MATRICULA: "), input("NOME: "), input("DATA NASC: "), input("TELEFONE"),
                               input("VEICULOS: "), Cargo(int(input("CARGO: 1 2 OU 3: ")))) #mostrar opcoes de cargo

    def lista_funcionario(self):
        for funcionario in self.__funcionarios:
            print("NÚMERO MATRICULA: ", funcionario.numero_matricula, "NOME: ", funcionario.nome, "DATA NASC: ", funcionario.data_nascimento,
                  "TELEFONE: ", funcionario.telefone,
                  "VEICULOS: ", funcionario.veiculos, "CARGO: ", funcionario.cargo)

    @property
    def funcionarios(self):
        return self.__funcionarios

