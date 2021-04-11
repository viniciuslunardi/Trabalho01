import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaCadastraConta(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self, contas):
        paga = ["Não", "Sim"]
        identificador = ""
        nome = ""
        data_venc = ""
        descricao = ""
        valor = ""
        if contas:
            identificador = contas.identificador
            nome = contas.nome
            data_venc = contas.data_venc
            descricao = contas.descricao
            valor = contas.valor
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Identificador", size=(15, 1)), sg.InputText(identificador)],
            [sg.Text("Nome", size=(15, 1)), sg.InputText(nome)],
            [sg.Text("Data de vencimento", size=(15, 1)), sg.InputText(data_venc)],
            [sg.Text("Valor (R$)", size=(15, 1)), sg.InputText(valor)],
            [sg.Text("Descrição", size=(15, 1)), sg.InputText(descricao)],
            [sg.Text("Paga"), sg.Combo(size=(15, 1), values=paga)],
            [sg.Button("Salvar", size=(30, 1), key="salvar"), sg.Button("Voltar", size=(30, 1), key="voltar")]
        ]

        self.__window = sg.Window("Cadastro de Conta", default_element_size=(50, 0), font=("Helvetica", 15)).Layout(
            layout)

    def open(self, contas=None):
        self.init_components(contas)
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()
