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
        dia_venc = ""
        mes_venc = ""
        ano_venc = ""
        descricao = ""
        valor = ""
        exclude = False
        new = True
        pagou = 'Não'
        if contas:
            exclude = True
            new = False
            identificador = contas.identificador
            nome = contas.nome
            dia_venc = contas.data_venc.split('/')[0]
            mes_venc = contas.data_venc.split('/')[1]
            ano_venc = contas.data_venc.split('/')[2]
            descricao = contas.descricao
            valor = contas.valor
            if contas.paga:
                pagou = "Sim"
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Identificador:", size=(15, 1)), sg.InputText(identificador, disabled=exclude),
             sg.Button("Buscar", size=(6, 1), key="buscar")],
            [sg.Text("Nome:", size=(15, 1)), sg.InputText(nome, disabled=exclude)],
            [sg.Text("Data de Venc.:", size=(15, 1)), sg.InputText(dia_venc, size=(2, 1), disabled=exclude),
             sg.Text("/", size=(0, 1)), sg.InputText(mes_venc, size=(2, 1), disabled=exclude),
             sg.Text("/", size=(0, 1)), sg.InputText(ano_venc, size=(4, 1), disabled=exclude)],
            [sg.Text("Valor (R$):", size=(15, 1)), sg.InputText(valor, disabled=exclude)],
            [sg.Text("Descrição:", size=(15, 1)), sg.InputText(descricao, disabled=exclude)],
            [sg.Text("Paga:", visible=new), sg.Combo(size=(15, 1), values=paga, visible=new), sg.Text("Paga:"),
             sg.Text(pagou, size=(15, 1), visible=exclude)],
            [sg.Button("Salvar", size=(15, 1), key="salvar", button_color='green', visible=new),
             sg.Button("Voltar", size=(15, 1), key="voltar"),
             sg.Button("Excluir", size=(15, 1), key="excluir", visible=exclude, button_color="red")]
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
