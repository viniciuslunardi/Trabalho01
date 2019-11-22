import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaRegistro(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, registros):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Lista de registros")],
            [sg.Listbox(values=registros, size=(100, 10))],
            [sg.Submit("Filtrar registros", key=1), sg.Submit("Limpar Filtro", key=2),
             sg.Submit("Voltar", key=9)],
        ]
        self.__window = sg.Window("Registros", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(layout)

    def open(self, registros=None):
        self.init_components(registros)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values
