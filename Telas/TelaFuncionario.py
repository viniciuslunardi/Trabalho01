from Telas.AbstractTela import AbstractTela
import PySimpleGUI as sg
from Controladores.ControladorVeiculo import ControladorVeiculo

class TelaFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None
        self.init_components()

    def init_components(self):
        layout = [
            [sg.Text("aiaiaiai")]
        ]

        self.__window = sg.Window("Funcionários", default_element_size=(150, 300)).Layout(layout)

    def mostrar_opcoes(self):
        # print("---------------FUNCIONÁRIO---------------")
        # print("1: CADASTRAR FUNCIONÁRIO")
        # print("2: LISTA DE FUNCIONÁRIOS")
        # print("3: LIBERAR ACESSO DE VEÍCULO")
        # print("4: VERIFICAR ACESSO DE VEÍCULOS POR MATRÍCULA")
        # print("5: ALTERAR FUNCIONÁRIO")
        # print("6: DEMITIR FUNCIONÁRIO")
        # print("7: DESBLOQUEAR FUNCIONÁRIO")
        # print("0: VOLTAR PARA TELA PRINCIPAL")
        # opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6, 7])
        #
        # return opcao
        print("x")

    def open(self):
        buttons, values = self.__window.Read()
        return buttons, values


