import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastroMensalidade(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, mensalidade):
        cpf = ""
        descricao = ""
        mes_venc = ""
        ano_venc = ""
        if mensalidade:
            cpf = mensalidade[0]
            descricao = mensalidade[1]
            mes_venc = mensalidade[2]
            ano_venc = mensalidade[3]

        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("CPF*", size=(15, 1)), sg.InputText(cpf, size=(15, 1))],
            [sg.Text("Descrição", size=(15, 1)), sg.InputText(descricao)],
            [sg.Text("Mês e ano de vencimento*", size=(15, 1)), sg.InputText(mes_venc, size=(2, 1)),
             sg.Text("/", size=(0, 1)), sg.InputText(ano_venc, size=(4, 1))],
            [sg.Button("Salvar", size=(20, 1), key="salvar", button_color='green'), sg.Button("Voltar", key='voltar', size=(15, 1))]
        ]

        self.__window = sg.Window("Cadastro de Mensalidade", font=("Helvetica", 15), keep_on_top=True).Layout(layout)

    def open(self, alunos=None):
        self.init_components(alunos)
        button, values = self.__window.Read()
        return button, list(values.values())

    def close(self):
        self.__window.Close()

    def show_message(self, title, message):
        sg.Popup(title, message, font=("Helvetica", 15), keep_on_top=True)