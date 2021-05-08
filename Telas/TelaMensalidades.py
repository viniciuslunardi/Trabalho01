import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaMensalidades(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None
        self.__dados_tela = {}

    def init_components(self, mensalidades):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text('Mensalidades')],
            [sg.Listbox(values=mensalidades, size=(150, 10))],
            [sg.Button('Voltar', key=4), sg.Button('Cadastrar mensalidade', key=9)]
        ]
        self.__window = sg.Window("Mensalidades", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(layout)

    def open(self, mensalidades):
        self.init_components(mensalidades)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values

    def close(self):
        self.__window.Close()
