from Telas.AbstractTela import AbstractTela


class TelaRegistro(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador

    def mostrar_opcoes(self):
        print("---------------REGISTROS---------------")
        print("1: LISTA DE REGISTROS")
        print("2: FILTRAR REGISTROS")
        print("0: VOLTAR PARA TELA PRINCIPAL")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1])
        return opcao

