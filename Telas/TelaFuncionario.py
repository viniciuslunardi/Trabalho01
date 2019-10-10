from Telas.AbstractTela import AbstractTela
from Controladores.ControladorVeiculo import ControladorVeiculo

class TelaFuncionario(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador

    def mostrar_opcoes(self):
        print("---------------FUNCIONÁRIO---------------")
        print("1: CADASTRAR FUNCIONÁRIO")
        print("2: LISTA DE FUNCIONÁRIOS")
        print("3: LIBERAR ACESSO DE VEÍCULO")
        print("4: ")
        print("5: ")
        print("0: VOLTAR PARA TELA PRINCIPAL")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3])

        return opcao

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
