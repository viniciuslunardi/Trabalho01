import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaContas(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None
        self.__dados_tela = {}

    def init_components(self, contas):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text('Contas cadastradas')],
            [sg.Listbox(values=contas, size=(150, 10))],
            [sg.Button('Voltar', key=4), sg.Button('Excluir conta', key=9)]
        ]
        self.__window = sg.Window("Contas", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(layout)

    def open(self, contas):
        self.init_components(contas)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values

    def close(self):
        self.__window.Close()
