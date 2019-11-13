import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaPrincipal(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__window = None
        self.__controlador = controlador
        self.init_components()

    def init_components(self):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Submit("Ir para Funcionários", size=(45, 1), key="funcionarios", font=("Helvetica", 15))],
            [sg.Submit("Ir para Veículos", size=(45, 1), key="veiculos", font=("Helvetica", 15))],
            [sg.Submit("Ir para Armário", size=(45, 1), key="armario", font=("Helvetica", 15))],
            [sg.Submit("Ir para Registros", size=(45, 1), key="registros", font=("Helvetica", 15))],
            # [sg.Listbox(values=('Listbox 1', "Funcionario"), size=(100, 1), key="lb_itens")]
        ]
        self.__window = sg.Window("Início", default_element_size=(300, 300)).Layout(layout)

    def mostrar_opcoes(self):
        # print("---------------INÍCIO---------------")
        # print("1: IR PARA ÁREA DE FUNCIONÁRIO")
        # print("2: IR PARA ÁREA DE VEÍCULOS")
        # print("3: IR PARA ARMÁRIO")
        # print("4: IR PARA ÁREA DE REGISTROS")
        # opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4])
        # self.open()
        # return opcao
        print('x')

    def open(self):
        buttons, values = self.__window.Read()
        return buttons, values


