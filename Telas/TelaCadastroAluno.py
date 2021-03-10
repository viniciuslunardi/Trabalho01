import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastroAluno(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, alunos):
        placa = ""
        modelo = ""
        marca = ""
        ano = ""
        km = ""
        if alunos:
            placa = alunos.placa
            modelo = alunos.modelo
            marca = alunos.marca
            ano = alunos.ano
            km = alunos.quilometragem_atual
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Placa", size=(5, 1)), sg.InputText(placa)],
            [sg.Text("Modelo", size=(5, 1)), sg.InputText(modelo)],
            [sg.Text("Marca", size=(5, 1)), sg.InputText(marca)],
            [sg.Text("Ano", size=(5, 1)), sg.InputText(ano)],
            [sg.Text("KM atual", size=(8, 1)), sg.InputText(km)],
            [sg.Button("Salvar", size=(30, 1), key="salvar")]
        ]

        self.__window = sg.Window("Cadastro de Alunos", default_element_size=(50, 0), font=("Helvetica", 15)).Layout(
            layout)

    def open(self, alunos=None):
        self.init_components(alunos)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()
