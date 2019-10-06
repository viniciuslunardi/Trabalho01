from abc import ABC, abstractmethod

class AbstractTela(ABC):
    @abstractmethod
    def __init__(self, controlador):
        self.__controlador = controlador

    @abstractmethod
    def le_num_inteiro(self, mensagem, numeros_validos):
        pass

    @abstractmethod
    def mostrar_opcoes(self):
        pass