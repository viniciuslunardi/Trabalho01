import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaArmario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None
        self.init_components()

    def init_components(self):
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Submit("Veículos na garagem", size=(30, 1), key="veiculos_garagem")],
            [sg.Submit("Pegar veículo", size=(30, 1), key="pegar_veiculo")],
            [sg.Submit("Devolver veículo", size=(30, 1), key="devolver")],
            [sg.Submit("Veículos emprestados", size=(30, 1), key="emprestados")],
            [sg.Submit("Voltar", size=(30, 1), key="voltar")],
            # [sg.Listbox(values=('Listbox 1', "Funcionario"), size=(100, 1), key="lb_itens")]
        ]
        self.__window = sg.Window("Armário", default_element_size=(150, 300)).Layout(layout)

    def mostrar_opcoes(self):
        print("---------------ARMÁRIO---------------")
        print("1: VEÍCULOS NA GARAGEM - CHAVES DISPONÍVEIS")
        print("2: PEGAR VEÍCULO")
        print("3: DEVOLVER VEÍCULO")
        print("4: VEÍCULOS EMPRESTADOS ")
        print("0: VOLTAR PARA TELA PRINCIPAL")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

        return opcao

    def open(self):
        buttons, values = self.__window.Read()
        return buttons, values
