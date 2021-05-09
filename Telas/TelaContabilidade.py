import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaContabilidade(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None
        self.__dados_tela = {}

    def init_components(self, salarios):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text('Fluxo de caixa')],
            [sg.Listbox(values=salarios, size=(150, 10))],
            [sg.Button('Voltar', key=4)]
        ]
        self.__window = sg.Window("Fluxo de caixa", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(layout)

    def open(self, salarios):
        self.init_components(salarios)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values

    def close(self):
        self.__window.Close()