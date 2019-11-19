import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaFiltroRegistro(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Filtrar por: ")],
            [sg.Submit("Matrícula", size=(30, 1), key=1), sg.Submit("Placa", size=(30, 1), key=2)]
        ]
        self.__window = sg.Window("Filtro", font=("Helvetica", 15)).Layout(layout)

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values
