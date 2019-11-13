import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaVeiculo(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None
        self.init_components()

    def mostrar_opcoes(self):
        print("---------------VEÍCULO---------------")
        print("1: CADASTRAR VEÍCULO")
        print("2: LISTA DE VEÍCULOS")
        print("3: ALTERAR VEÍCULO")
        print("4: DELETAR VEÍCULO")
        print("0: VOLTAR PARA TELA PRINCIPAL")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

        return opcao

    def init_components(self):
        layout = [
            [sg.Submit("Cadastrar Veículo", size=(30, 1), key="cadastrar")],
            [sg.Submit("Lista de veículos", size=(30, 1), key="lista")],
            [sg.Submit("Alterar veículo", size=(30, 1), key="alterar")],
            [sg.Submit("Deletar veículo", size=(30, 1), key="deletar")],
            [sg.Submit("Voltar", size=(30, 1), key="voltar")],
            # [sg.Listbox(values=('Listbox 1', "Funcionario"), size=(100, 1), key="lb_itens")]
        ]
        self.__window = sg.Window("Veículos", default_element_size=(150, 300)).Layout(layout)

    def open(self):
        button, values = self.__window.Read()
        return button, values
