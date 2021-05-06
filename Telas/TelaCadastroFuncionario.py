import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastroFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, funcionario):
        cargos = ["Gerente", "Professor", "Recepcionista"]
        codigo = ""
        senha = ""
        nome = ""
        cpf = ""
        data_nascimento = ""
        email = ""
        agencia = ""
        codigo_banco = ""
        numero = ""
        tipo = ""
        carga_horaria = ""
        salario = ""

        if funcionario:
            codigo = funcionario.codigo
            senha = funcionario.senha
            cpf = funcionario.cpf
            agencia = funcionario.agencia
            codigo_banco = funcionario.codigo_banco
            numero = funcionario.numero
            tipo = funcionario.tipo
            carga_horaria = funcionario.carga_horaria
            salario = funcionario.salario
            nome = funcionario.nome
            data_nascimento = funcionario.data_nasc
            email = funcionario.email

        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Código*", size=(15, 1)), sg.InputText(codigo)],
            [sg.Text("Senha*", size=(15, 1)), sg.InputText(senha)],
            [sg.Text("Nome*", size=(15, 1)), sg.InputText(nome)],
            [sg.Text("Data nasc.*", size=(15, 1)), sg.InputText(data_nascimento)],
            [sg.Text("Email*", size=(15, 1)), sg.InputText(email)],
            [sg.Text("CPF*", size=(15, 1)), sg.InputText(cpf)],
            [sg.Text("Agencia banc.*", size=(15, 1)), sg.InputText(agencia)],
            [sg.Text("Código do Banco*", size=(15, 1)), sg.InputText(codigo_banco)],
            [sg.Text("Numero conta*", size=(15, 1)), sg.InputText(numero)],
            [sg.Text("Tipo de conta*", size=(15, 1)), sg.InputText(tipo)],
            [sg.Text("Carga horaria*", size=(15, 1)), sg.InputText(carga_horaria)],
            [sg.Text("Salário*", size=(15, 1)), sg.InputText(salario)],
            [sg.Text("Cargo*"), sg.Combo(size=(15, 1), values=cargos)],
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
