import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaRegistro(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def mostrar_opcoes(self):
        print("-------------REGISTROS------------")
        print("1: LISTA DE REGISTROS")
        print("2: FILTRAR REGISTROS")
        print("0: VOLTAR PARA TELA PRINCIPAL")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2])
        return opcao

    def init_components(self):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Submit("Lista de registros", size=(30, 1), key="lista")],
            [sg.Submit("Filtrar registros", size=(30, 1), key="filtrar")],
            [sg.Submit("Voltar", size=(30, 1), key="voltar")],
            # [sg.Listbox(values=('Listbox 1', "Funcionario"), size=(100, 1), key="lb_itens")]
        ]
        self.__window = sg.Window("Registros", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(layout)

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values
