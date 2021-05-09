import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastroAluno(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, alunos, excluir_visible=False, disable_all_fields=False):
        cpf = ""
        dia_nasc = ""
        mes_nasc = ""
        ano_nasc = ""
        codigo = ""
        email = ""
        nome = ""
        senha = ""
        mensalidade = ""
        venc_mensalidade = ""
        if alunos:
            cpf = alunos[0]
            nome = alunos[1]
            dia_nasc = alunos[2].split('/')[0]
            mes_nasc = alunos[2].split('/')[1]
            ano_nasc = alunos[2].split('/')[2]
            email = alunos[3]
            codigo = alunos[4]
            senha = alunos[5]
            mensalidade = alunos[6]
            venc_mensalidade = alunos[7]

        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("CPF*", size=(15, 1)), sg.InputText(cpf, size=(15, 1), disabled=disable_all_fields),
             sg.Button("Buscar", size=(5, 1), key='buscar')],
            [sg.Text("Nome*", size=(15, 1)), sg.InputText(nome, disabled=disable_all_fields)],
            [sg.Text("Data nasc.*", size=(15, 1)), sg.InputText(dia_nasc, size=(2, 1), disabled=disable_all_fields), sg.Text("/", size=(0, 1)),
             sg.InputText(mes_nasc, size=(2, 1), disabled=disable_all_fields), sg.Text("/", size=(0, 1)), sg.InputText(ano_nasc, size=(4, 1), disabled=disable_all_fields)],
            [sg.Text("Email*", size=(15, 1)), sg.InputText(email, disabled=disable_all_fields)],
            [sg.Text("Código*", size=(15, 1)), sg.InputText(codigo, disabled=disable_all_fields)],
            [sg.Text("Senha*", size=(15, 1)), sg.InputText(senha, disabled=disable_all_fields)],
            [sg.Text("Mensalidade", size=(15, 1)), sg.InputText(mensalidade, disabled=disable_all_fields)],
            [sg.Text("Venc. mensalidade*", size=(15, 1)), sg.InputText(venc_mensalidade, disabled=disable_all_fields)],
            [sg.Button("Salvar", size=(20, 1), key="salvar", button_color='green'), sg.Button("Voltar", key='voltar', size=(15, 1)), sg.Button("Excluir", key='excluir', visible=excluir_visible, size=(15, 1), button_color='red')]
        ]

        self.__window = sg.Window("Cadastro de Alunos", font=("Helvetica", 15), keep_on_top=True).Layout(layout)

    def open(self, alunos=None, excluir_visible=False, disable_all_fields=False):
        self.init_components(alunos, excluir_visible, disable_all_fields)
        button, values = self.__window.Read()
        return button, list(values.values())

    def close(self):
        self.__window.Close()

    def show_message(self, title, message):
        sg.Popup(title, message, font=("Helvetica", 15), keep_on_top=True)

