import PySimpleGUI as sg
from Telas.AbstractTela import AbstractTela


class TelaMarcaPagamentoFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador
        self.__window = None

    def init_components(self):
        identificador = ""
        descricao = ""
        dia_venc = ""
        mes_venc = ""
        ano_venc = ""
        valor = ""
        exclude = False
        new = True
        sg.change_look_and_feel("Reddit")
        layout = [
            [sg.Text("Identificador:", size=(15, 1)), sg.InputText(identificador, disabled=exclude)],
            [sg.Text("Data de Pagamento.:", size=(15, 1)), sg.InputText(dia_venc, size=(2, 1), disabled=exclude),
             sg.Text("/", size=(0, 1)), sg.InputText(mes_venc, size=(2, 1), disabled=exclude),
             sg.Text("/", size=(0, 1)), sg.InputText(ano_venc, size=(4, 1), disabled=exclude)],
            [sg.Text("Valor (R$):", size=(15, 1)), sg.InputText(valor, disabled=exclude)],
            [sg.Text("Descrição:", size=(15, 1)), sg.InputText(descricao, disabled=exclude)],
            [sg.Button("Salvar", size=(15, 1), key=5, button_color='green', visible=new),
             sg.Button("Voltar", size=(15, 1), key=4)]
        ]

        self.__window = sg.Window("Marcacao de pagamentos dos funcionários", default_element_size=(50, 0), font=("Helvetica", 15)).Layout(
            layout)

    def open(self):
        self.init_components()
        button, values = self.__window.Read()
        self.close()
        return button, values

    def close(self):
        self.__window.Close()
