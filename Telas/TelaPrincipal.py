import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaPrincipal(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__window = None
        self.__controlador = controlador


    def init_components(self):
        sg.change_look_and_feel("Reddit")
        #TODO cada usuario deve ter uma tela diferente aqui, de acordo com sua funcao de funcionario ou seu aluno
        #TODO por agora, temos uma tela apenas de funcionário que vai ser vista apenas pelo gerente (vai poder acessar todos os dados do s8istema
        #TODO temos q adicionar a flag "key" pros botões que ainda não fazem nada
        layout = [
            [sg.Column(
                [
                    [sg.Text("GymSystem", size=(10, 1), font=("Helvetica", 35), justification='center')],
                    [sg.Button("Cadastrar Funcionário", size=(33, 1), key=2)],
                    [sg.Button("Cadastrar Aluno", size=(33, 1), key=3),
                     sg.Button("Cadastrar Conta", size=(33, 1), key=5),
                     sg.Button("Relatório de contas", size=(33, 1), key=888)],
                    [sg.Button("Relatório de alunos", size=(33, 1), key=1),
                     sg.Button("Relatório de funcionários", size=(33, 1), key=0),
                     sg.Button("Relatório de alunos inadimplentes", size=(33, 1), key=4)],
                    [sg.Button("Fluxo de caixa", size=(33, 1), key=66),
                     sg.Button("Mensalidades", size=(33, 1), key=6),
                     sg.Button("Salários", size=(33, 1), key=78),
                     ],
                ], element_justification='center')]

        ]
        self.__window = sg.Window("Início", default_element_size=(300, 300), font=("Helvetica", 15), grab_anywhere=True).Layout(layout)

    def mostrar_opcoes(self):
        print('x')

    def open(self):
        self.init_components()
        buttons, values = self.__window.Read()
        self.close()
        return buttons, values

    def close(self):
        self.__window.Close()
