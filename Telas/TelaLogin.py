import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaLogin(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__window = None
        self.__controlador = controlador


    def init_components(self):
        sg.change_look_and_feel("Reddit")
        login = ""
        senha = ""
        layout = [
            [sg.Text("GymSystem", size=(10, 1), font=("Helvetica", 35), justification='center')],
            [sg.Text("Login", size=(5, 1)), sg.InputText(login)],
            [sg.Text("Senha", size=(5, 1)), sg.InputText(senha, password_char='*')],
            [sg.Button("Entrar", size=(45, 1), key=1)],
        ]
        self.__window = sg.Window("Login", default_element_size=(50, 50), font=("Helvetica", 15)).Layout(layout)

    def mostrar_opcoes(self):
        print('x')

    def open(self):
        self.init_components()
        buttons, values = self.__window.Read()
        self.close()
        return buttons, values

    def close(self):
        self.__window.Close()
