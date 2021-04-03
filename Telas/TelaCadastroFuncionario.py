import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastroFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, funcionario):
        codigo = ""
        senha = ""
        nome = ""
        cpf = ""
        data_nascimento = ""
        email = ""
        conta_bancaria = ""
        carga_horaria = ""
        salario = ""

        if funcionario:
            codigo = funcionario.usuario
            senha = funcionario.senha
            cpf = funcionario.cpf
            conta_bancaria = funcionario.conta_bancaria
            carga_horaria = funcionario.carga_horaria
            salario = funcionario.salario
            nome = funcionario.nome
            data_nascimento = funcionario.data_nascimento
            email = funcionario.email

        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Código", size=(15, 1)), sg.InputText(codigo)],
            [sg.Text("Senha", size=(15, 1)), sg.InputText(senha)],
            [sg.Text("Nome", size=(15, 1)), sg.InputText(nome)],
            [sg.Text("Data de Nascimento", size=(15, 1)), sg.InputText(data_nascimento)],
            [sg.Text("Email", size=(15, 1)), sg.InputText(email)],
            [sg.Text("CPF", size=(15, 1)), sg.InputText(cpf)],
            [sg.Text("Conta bancária", size=(15, 1)), sg.InputText(conta_bancaria)],
            [sg.Text("Carga horaria", size=(15, 1)), sg.InputText(carga_horaria)],
            [sg.Text("Salário", size=(15, 1)), sg.InputText(salario)],
            [sg.Button("Salvar", size=(30, 1), key="salvar")]
        ]

        self.__window = sg.Window("Cadastro de Funcionários", default_element_size=(50, 0),
                                  font=("Helvetica", 15)).Layout(layout)

    def open(self, funcionario=None):
        self.init_components(funcionario)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()
