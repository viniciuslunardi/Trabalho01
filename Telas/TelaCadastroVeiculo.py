import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastroVeiculo(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, veiculo):
        placa = ""
        modelo = ""
        marca = ""
        ano = ""
        km = ""
        if veiculo:
            placa = veiculo.placa
            modelo = veiculo.modelo
            marca = veiculo.marca
            ano = veiculo.ano
            km = veiculo.quilometragem_atual
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Placa", size=(5, 1)), sg.InputText(placa)],
            [sg.Text("Modelo", size=(5, 1)), sg.InputText(modelo)],
            [sg.Text("Marca", size=(5, 1)), sg.InputText(marca)],
            [sg.Text("Ano", size=(5, 1)), sg.InputText(ano)],
            [sg.Text("KM atual", size=(8, 1)), sg.InputText(km)],
            [sg.Button("Salvar", size=(30, 1), key="salvar")]
        ]

        self.__window = sg.Window("Cadastro de Veículos", default_element_size=(50, 0), font=("Helvetica", 15)).Layout(
            layout)

    def show_message(self, title, message):
        sg.Popup(title, message, font=("Helvetica", 15))

    def open(self, veiculo=None):
        print(veiculo)
        self.init_components(veiculo)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()
