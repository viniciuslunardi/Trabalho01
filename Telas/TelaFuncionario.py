from Telas.AbstractTela import AbstractTela
import PySimpleGUI as sg
from Controladores.ControladorVeiculo import ControladorVeiculo


class TelaFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Submit("Cadastrar funcionário", size=(30, 1), key="cadastro")],
            [sg.Submit("Lista de funcionários", size=(30, 1), key="lista")],
            [sg.Submit("Liberar acesso de veículo", size=(30, 1), key="liberar")],
            [sg.Submit("Verificar acesso de veículo por matrícula", size=(30, 1), key="verificar")],
            [sg.Submit("Alterar funcionário", size=(30, 1), key="alterar")],
            [sg.Submit("Demitir funcionário", size=(30, 1), key="demitir")],
            [sg.Submit("Desbloquear funcionário", size=(30, 1), key="desbloquear")],
            [sg.Submit("Voltar", size=(30, 1), key="voltar")],
            # [sg.Listbox(values=('Listbox 1', "Funcionario"), size=(100, 1), key="lb_itens")]
        ]
        self.__window = sg.Window("Funcionários", default_element_size=(150, 300), font=("Helvetica", 15)).Layout(
            layout)

    def mostrar_opcoes(self):
        # print("---------------FUNCIONÁRIO---------------")
        # print("1: CADASTRAR FUNCIONÁRIO")
        # print("2: LISTA DE FUNCIONÁRIOS")
        # print("3: LIBERAR ACESSO DE VEÍCULO")
        # print("4: VERIFICAR ACESSO DE VEÍCULOS POR MATRÍCULA")
        # print("5: ALTERAR FUNCIONÁRIO")
        # print("6: DEMITIR FUNCIONÁRIO")
        # print("7: DESBLOQUEAR FUNCIONÁRIO")
        # print("0: VOLTAR PARA TELA PRINCIPAL")
        # opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4, 5, 6, 7])
        #
        # return opcao
        print("x")

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        return button, values
