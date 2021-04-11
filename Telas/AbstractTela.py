from abc import ABC, abstractmethod
import PySimpleGUI as sg

class AbstractTela(ABC):
    @abstractmethod
    def __init__(self, controlador):
        self.__controlador = controlador

    def le_num_inteiro(self, mensagem: str = "", numeros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if numeros_validos and inteiro not in numeros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto")
                if numeros_validos:
                    print("valores validos", numeros_validos)

    def show_message(self, title, message):
        sg.Popup(title, message, font=("Helvetica", 15))

    def ask_verification(self, title, message):
        text = sg.PopupGetText(title, message, font=("Helvetica", 25))
        return text
