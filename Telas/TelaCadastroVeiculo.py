import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastroVeiculo(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Placa", size=(15, 1)), sg.InputText()],
            [sg.Text("Modelo", size=(15, 1)), sg.InputText()],
            [sg.Text("Marca", size=(15, 1)), sg.InputText()],
            [sg.Text("Ano", size=(15, 1)), sg.InputText()],
            [sg.Text("KM atual", size=(15, 1)), sg.InputText()],
            [sg.Submit("Salvar", size=(30, 1), key="salvar")]
        ]

        self.__window = sg.Window("Cadastro de Veículos", default_element_size=(150, 300)).Layout(layout)

    def save(self):
        button, values = self.__window.Read()
        print(button, values)
        return button, values

    def mostrar_opcoes(self):
        print("---------------VEÍCULO---------------")
        print("1: CADASTRAR VEÍCULO")
        print("2: LISTA DE VEÍCULOS")
        print("3: ALTERAR VEÍCULO")
        print("4: DELETAR VEÍCULO")
        print("0: VOLTAR PARA TELA PRINCIPAL")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

    def show_message(self, title, message):
        sg.Popup(title, message)
