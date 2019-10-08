from Telas.AbstractTela import AbstractTela


class TelaVeiculo(AbstractTela):
    def __init__(self, controlador):
        super().__init__(controlador)
        self.__controlador = controlador

    def mostrar_opcoes(self):
        print("---------------VEICULO---------------")
        print("0: CADASTRAR VEÍCULO")
        print("1: LISTA DE VEÍCULOS")
        print("3: ")
        print("4: ")
        print("5: ")
        opcao = self.le_num_inteiro("Escolha a opção: ", [0, 1, 2, 3, 4])

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