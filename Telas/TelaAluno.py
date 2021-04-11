import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaAluno(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None
        self.__dados_tela = {}

    def init_components(self, alunos):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text('Alunos cadastrados')],
            [sg.Listbox(values=alunos, size=(150, 10))],
            [sg.Button('Voltar', key=4),
            sg.Button('Add mensalidade', key=5)]
        ]
        self.__window = sg.Window("Alunos", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(layout)

    def open(self, alunos):
        self.init_components(alunos)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values

    def close(self):
        self.__window.Close()
