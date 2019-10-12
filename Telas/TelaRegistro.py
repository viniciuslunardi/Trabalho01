from Telas.AbstractTela import AbstractTela


class TelaRegistro(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador

    def mostrar_opcoes(self):
        print("---------------REGISTROS---------------")
        print("0: CADASTRAR REGISTRO")
        print("1: LISTA DE REGISTROS")
        print("3: ")
        print("4: ")
        print("5: ")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

        return opcao

