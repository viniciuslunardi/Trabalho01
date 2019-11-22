import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaFiltroEvento(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Filtrar por tipo de Evento: ")],
            [sg.Submit("ACESSO PERMITIDO", size=(30, 1), key=1), sg.Submit("ACESSO NEGADO", size=(30, 1), key=2)],
            [sg.Submit("ACESSO BLOQUEADO", size=(30, 1), key=3), sg.Submit("VEÍCULO DEVOLVIDO", size=(30, 1), key=4)],

        ]
        self.__window = sg.Window("Filtro", font=("Helvetica", 15)).Layout(layout)

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values
