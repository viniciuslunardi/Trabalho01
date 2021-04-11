import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastroAluno(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, alunos):
        cpf = ""
        dia_nasc = ""
        mes_nasc = ""
        ano_nasc = ""
        matricula = ""
        email = ""
        nome = ""
        senha = ""
        mensalidade = ""
        venc_mensalidade = ""
        if alunos:
            cpf = alunos.cpf
            dia_nasc = alunos.data_nasc.split('/')[0]
            mes_nasc = alunos.mes_nasc.split('/')[1]
            ano_nasc = alunos.ano_nasc.split('/')[2]
            matricula = alunos.matricula
            nome = alunos.nome
            senha = alunos.senha
            email = alunos.email
            mensalidade = alunos.mensalidade
            venc_mensalidade = alunos.venc_mensalidade
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("CPF*", size=(15, 1)), sg.InputText(cpf, size=(15,1)), sg.Button("Buscar", size=(5, 1), key='buscar')],
            [sg.Text("Nome*", size=(15, 1)), sg.InputText(nome)],
            [sg.Text("Data nasc.*", size=(15, 1)), sg.InputText(dia_nasc,size=(2,1)), sg.Text("/", size=(0, 1)), sg.InputText(mes_nasc, size=(2, 1)), sg.Text("/", size=(0, 1)), sg.InputText(ano_nasc,size=(4,1))],
            [sg.Text("Email*", size=(15, 1)), sg.InputText(email)],
            [sg.Text("Código*", size=(15, 1)), sg.InputText(matricula)],
            [sg.Text("Senha*", size=(15, 1)), sg.InputText(senha)],
            [sg.Text("Mensalidade", size=(15, 1)), sg.InputText(mensalidade)],
            [sg.Text("Venc. mensalidade*", size=(15, 1)), sg.InputText(venc_mensalidade)],
            [sg.Button("Salvar", size=(30, 1), key="salvar",)]
        ]

        self.__window = sg.Window("Cadastro de Alunos", font=("Helvetica", 15), keep_on_top=True).Layout(layout)

    def open(self, alunos=None):
        self.init_components(alunos)
        button, values = self.__window.Read()
        return button, values

    def close(self):
        self.__window.Close()

    def show_message(self, title, message):

        sg.Popup(title, message, font=("Helvetica", 15), keep_on_top=True)
