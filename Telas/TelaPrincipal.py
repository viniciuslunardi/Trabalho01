import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaPrincipal(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__window = None
        self.__controlador = controlador


    def init_components(self):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Button("Ir para Funcionários", size=(45, 1), key=0)],
            [sg.Button("Ir para Veículos", size=(45, 1), key=1)],
            [sg.Button("Ir para Armário", size=(45, 1), key=2)],
            [sg.Button("Ir para Registros", size=(45, 1), key=3)],
            # [sg.Listbox(values=('Listbox 1', "Funcionario"), size=(100, 1), key="lb_itens")]
        ]
        self.__window = sg.Window("Início", default_element_size=(300, 300), font=("Helvetica", 15)).Layout(layout)

    def mostrar_opcoes(self):
        print('x')

    def open(self):
        self.init_components()
        buttons, values = self.__window.Read()
        self.close()
        return buttons, values

    def close(self):
        self.__window.Close()
