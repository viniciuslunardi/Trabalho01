import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaArmario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, garagem):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Veículos na garagem")],
            [sg.Listbox(values=garagem, size=(100, 10))],
            [sg.Submit("Pegar veículo", key=2),
             sg.Submit("Devolver veículo", key=3),
             sg.Submit("Veículos emprestados", key=4),
             sg.Submit("Voltar", key=9)],
        ]
        self.__window = sg.Window("Armário", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(layout)

    def open(self, garagem):
        self.init_components(garagem)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values
