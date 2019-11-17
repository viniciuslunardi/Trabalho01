from Telas.AbstractTela import AbstractTela
import PySimpleGUI as sg
from Controladores.ControladorVeiculo import ControladorVeiculo


class TelaFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, funcionarios):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Funcionários cadastrados")],
            [sg.Listbox(values=funcionarios, size=(69, 10))],
            [sg.Submit("Cadastrar", key=1),
             sg.Submit("Liberar acesso", key=2),
             sg.Submit("Verificar acesso", key=3),
             sg.Submit("Alterar", key=4),
             sg.Submit("Demitir", key=5),
             sg.Submit("Desbloquear", key=6),
             sg.Submit("Voltar",key=0)],
        ]
        self.__window = sg.Window("Funcionários", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(
            layout)

    def open(self, funcionarios):
        self.init_components(funcionarios)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values
