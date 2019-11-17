import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastroFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, funcionario):
        cargos = ["Diretoria", "Comercial", "Desenvolvedor"]
        matricula = ""
        nome = ""
        data_nascimento = ""
        telefone = ""
        cargo = ""

        if funcionario:
            matricula = funcionario.numero_matricula
            nome = funcionario.nome
            data_nascimento = funcionario.data_nascimento
            telefone = funcionario.telefone
            cargo = funcionario.cargo

        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Matrícula", size=(10, 1)), sg.InputText(matricula)],
            [sg.Text("Nome", size=(10, 1)), sg.InputText(nome)],
            [sg.Text("Data de Nascimento", size=(10, 1)), sg.InputText(data_nascimento)],
            [sg.Text("Telefone", size=(10, 1)), sg.InputText(telefone)],
            [sg.Text("Cargo"), sg.Combo(size=(20, 1), values=cargos)],
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
