import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastroAluno(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, alunos):
        cpf = ""
        data_nasc = ""
        matricula = ""
        email = ""
        nome = ""
        senha = ""
        mensalidade = ""
        venc_mensalidade = ""
        if alunos:
            cpf = alunos.cpf
            data_nasc = alunos.data_nasc
            matricula = alunos.matricula
            nome = alunos.nome
            senha = alunos.senha
            email = alunos.email
            mensalidade = alunos.mensalidade
            venc_mensalidade = alunos.venc_mensalidade
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Nome", size=(15, 1)), sg.InputText(nome)],
            [sg.Text("CPF", size=(15, 1)), sg.InputText(cpf)],
            [sg.Text("Data nasc.", size=(15, 1)), sg.InputText(data_nasc)],
            [sg.Text("Email", size=(15, 1)), sg.InputText(email)],
            [sg.Text("Matrícula", size=(15, 1)), sg.InputText(matricula)],
            [sg.Text("Senha", size=(15, 1)), sg.InputText(senha)],
            [sg.Text("Mensalidade", size=(15, 1)), sg.InputText(mensalidade)],
            [sg.Text("Venc. mensalidade", size=(15, 1)), sg.InputText(venc_mensalidade)],
            [sg.Button("Salvar", size=(30, 1), key="salvar",)]
        ]

        self.__window = sg.Window("Cadastro de Alunos", default_element_size=(50, 0), font=("Helvetica", 15)).Layout(
            layout)

    def open(self, alunos=None):
        self.init_components(alunos)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()
