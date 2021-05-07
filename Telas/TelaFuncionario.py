from Telas.AbstractTela import AbstractTela
import PySimpleGUI as sg
from Controladores.ControladorAluno import ControladorAluno


class TelaFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, funcionarios):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Funcionários cadastrados")],
            [sg.Listbox(values=funcionarios, size=(100, 10))],
            [sg.Submit("Alterar", key=4),
             sg.Submit("Excluir", key=5),
             sg.Submit("Voltar", key=9)],
        ]
        self.__window = sg.Window("Funcionários", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(
            layout)

    def open(self, funcionarios):
        self.init_components(funcionarios)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values