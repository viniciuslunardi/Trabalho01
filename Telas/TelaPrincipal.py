import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaPrincipal(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__window = None
        self.__controlador = controlador

        layout = [
            [sg.Text("Início")],
            [sg.Listbox(values=('Listbox 1', 'Listbox 2'), size=(20, 3), key="lb_itens")]
        ]
        self.__window = sg.Window("Início", default_element_size=(40, 1)).Layout(layout)

    def mostrar_opcoes(self):
        print("---------------INÍCIO---------------")
        print("1: IR PARA ÁREA DE FUNCIONÁRIO")
        print("2: IR PARA ÁREA DE VEÍCULOS")
        print("3: IR PARA ARMÁRIO")
        print("4: IR PARA ÁREA DE REGISTROS")
        opcao = self.le_num_inteiro("Escolha a opção: ", [1, 2, 3, 4])
        self.open()
        return opcao

    def open(self):
        buttons, values = self.__window.Read()
        return buttons, values


