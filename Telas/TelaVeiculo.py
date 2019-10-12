from Telas.AbstractTela import AbstractTela


class TelaVeiculo(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador

    def mostrar_opcoes(self):
        print("---------------VEÍCULO---------------")
        print("1: CADASTRAR VEÍCULO")
        print("2: LISTA DE VEÍCULOS")
        print("3: DELETAR VEÍCULO")
        print("0: VOLTAR PARA TELA PRINCIPAL")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3])

        return opcao
