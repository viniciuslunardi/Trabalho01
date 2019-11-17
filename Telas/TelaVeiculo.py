import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaVeiculo(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None
        self.__dados_tela = {}

    def init_components(self, veiculos):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text('Veículos cadastrados')],
            [sg.Listbox(values=veiculos, size=(50, 10))],
            [sg.Submit('Cadastrar Veículo', key=1),
             sg.Submit('Alterar Veículo', key=2),
             sg.Submit('Excluir Veículo', key=3),
             sg.Button('Voltar', key=4)],
            # [sg.Listbox(values=('Listbox 1', "Funcionario"), size=(100, 1), key="lb_itens")]
        ]
        self.__window = sg.Window("Veículos", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(layout)

    def open(self, veiculos):
        self.init_components(veiculos)
        button, values = self.__window.Read()
        self.__window.Close()
        return button, values

    def close(self):
        self.__window.Close()

    def pop_mensagem(self, mensagem):
        sg.Popup(mensagem)
