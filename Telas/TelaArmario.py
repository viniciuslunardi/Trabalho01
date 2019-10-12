from Telas.AbstractTela import AbstractTela


class TelaArmario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador

    def mostrar_opcoes(self):
        print("---------------ARMÁRIO---------------")
        print("1: VEÍCULOS NA GARAGEM - CHAVES DISPONÍVEIS")
        print("2: PEGAR VEÍCULO")
        print("3: DEVOLVER VEÍCULO")
        print("4: VEÍCULOS EMPRESTADOS ")
        print("0: VOLTAR PARA TELA PRINCIPAL")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

        return opcao

