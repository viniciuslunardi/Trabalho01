from Telas.TelaFuncionario import TelaFuncionario
from Entidades.Funcionario import Funcionario
from Entidades.Funcionario import Cargo
from Controladores.ControladorVeiculo import ControladorVeiculo


class ControladorFuncionario:
    def __init__(self, controlador_principal):
        self.__tela_funcionario = TelaFuncionario(self)
        self.__funcionarios = {}
        self.__cargo = None
        self.__controlador_veiculo = ControladorVeiculo
        self.__controlador_principal = controlador_principal

    def abre_funcionario(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {
            1: self.cadastra,
            2: self.lista_funcionario,
            3: self.dar_acesso_veiculo,
            4: self.veiculos_funcionario,
            5: self.deletar_funcionario,
            0: self.voltar
        }
        while True:
            opcao = self.__tela_funcionario.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def cadastrar_funcionario(self, numero_matricula, nome, data_nascimento, telefone, cargo: Cargo):
        try:
            funcionario = Funcionario(numero_matricula, nome, data_nascimento, telefone, cargo)
            if self.existe_funcionario(numero_matricula):
                raise Exception
            else:
                self.__funcionarios[numero_matricula] = funcionario
                if funcionario.cargo == Cargo.DIRETORIA:
                    funcionario.veiculos = self.__controlador_principal.controlador_veiculo.veiculos
                else:
                    self.dar_acesso_veiculo(numero_matricula)
        except Exception:
            print("-----------------ATENÇÃO----------------- \n * Funcionário já cadastrado * ")

    def cadastra(self):
        while True:
            try:
                matricula = int(input("Informe o número de matrícula do funcionário: "))
                if matricula:
                    try:
                        nome = input("Informe o nome do funcionário: ")
                        data = input("Informe a data de nascimento do funcionário: ")
                        telefone = input("Informe o número do telefone do funcionário ")
                        if nome == "" or data == "" or telefone == "":
                            raise Exception
                        else:
                            self.cadastrar_funcionario(matricula, nome, data, telefone, Cargo(self.cadastrar_cargo()))
                            return
                    except Exception:
                        print("Todos os campos devem ser preenchidos!")
                else:
                    raise Exception
            except Exception:
                print("Matrícula do funcionário deve ser um número inteiro")

    def cadastrar_cargo(self):
        numeros_validos = [1, 2, 3]
        while True:
            entrada = input("CARGO: \n  * 1: DIRETORIA \n  * 2: COMERCIAL \n  * 3: DESENVOLVEDOR \n")
            try:
                inteiro = int(entrada)
                if numeros_validos and inteiro not in numeros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto")
                print("Valores validos: ", numeros_validos)

    def lista_funcionario(self):
        if len(self.__funcionarios) > 0:
            for funcionario in self.__funcionarios:
                cargo = self.__funcionarios[funcionario].cargo
                if cargo == cargo.DIRETORIA:
                    cargo = "Diretoria"
                elif cargo == cargo.COMERCIAL:
                    cargo = "Comercial"
                else:
                    cargo = "Desenvolvedor"
                print("NÚMERO DE MATRICULA: ", str(self.__funcionarios[funcionario].numero_matricula),
                      "NOME: ", str(self.__funcionarios[funcionario].nome),
                      "DATA DE NASCIMENTO: ", str(self.__funcionarios[funcionario].data_nascimento),
                      "TELEFONE: ", str(self.__funcionarios[funcionario].telefone),
                      "CARGO: ", cargo)
                print("")
        else:
            print("Nenhum funcionário cadastrado")

    def existe_funcionario(self, numero_matricula):
        return numero_matricula in self.__funcionarios

    def dar_acesso_veiculo(self, num_matricula: str = None):
        veiculos = self.__controlador_principal.controlador_veiculo.veiculos
        if not num_matricula:
            matricula = input("Digite a matricula do funcionário a ser autorizado: ")
        else:
            matricula = num_matricula
        if matricula not in self.__funcionarios:
            print("Não existe funcionário com matrícula '" + str(matricula) + "' cadastrado no sistema")
            return
        else:
            funcionario = self.__funcionarios[matricula]
        if funcionario.cargo == Cargo.DIRETORIA:
            print("Este funcionário já tem acesso a todos os veiculos da garagem")
            print("Funcionário tem acesso aos seguintes veículos: ")
            for carro in funcionario.veiculos:
                print("PLACA: %s MODELO: %s" % (funcionario.veiculos[carro].placa, funcionario.veiculos[carro].modelo))
            return
        try:
            qtd_carros = int(input("Digite quantos veículos este funcionário terá acesso: "))
            carros_cadastrados = 0
            if qtd_carros:
                while True:
                    if qtd_carros > len(self.__controlador_principal.controlador_veiculo.veiculos):
                        print("Não existem tantos veículos assim na garagem!")
                        break
                    else:
                        while carros_cadastrados < qtd_carros:
                            placa = input("Digite a placa do veículo autorizado: ")
                            if placa not in veiculos:
                                print("Não existe veículo com placa '" + str(placa) + "' na garagem")
                                return
                            veiculo = veiculos[placa]
                            if placa not in funcionario.veiculos:
                                funcionario.veiculos[placa] = veiculo
                            else:
                                print("Funcionário já tem acesso a esse veículo")
                            print("Funcionário tem acesso aos seguintes carros: ")
                            carros_cadastrados += 1
                            for carro in funcionario.veiculos:
                                print("PLACA: %s MODELO: %s"
                                      % (funcionario.veiculos[carro].placa, funcionario.veiculos[carro].modelo))
                    return
            else:
                raise ValueError
        except ValueError:
            print("Quantidade de carros deve ser um número inteiro")


    def veiculos_funcionario(self):
        while True:
            matricula = input("Digite o número de matrícula do funcionário que deseja verificar: ")
            if matricula not in self.__funcionarios:
                print("Não existe funcionário com matrícula '" + str(matricula) + "' cadastrado no sistema")
            else:
                funcionario = self.__funcionarios[matricula]
                print("Funcionário tem acesso aos seguintes carros: ")
                for carro in funcionario.veiculos:
                    print("PLACA: %s MODELO: %s"
                          % (funcionario.veiculos[carro].placa, funcionario.veiculos[carro].modelo))
                return

    def deletar_funcionario(self):
        matricula = input("Digite o número de matrícula do funcionário: ")
        if matricula in self.__funcionarios:
            del self.__funcionarios[matricula]
        else:
            print("Não existe funcionário com esse número de matrícula")
        return

    @property
    def funcionarios(self):
        return self.__funcionarios

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
