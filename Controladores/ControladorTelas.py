from Controladores.ControladorPrincipal import ControladorPrincipal


class ControladorTelas:
    def __init__(self):
        self.__voltar = None

    def voltar(self):
        ControladorPrincipal().inicia()
