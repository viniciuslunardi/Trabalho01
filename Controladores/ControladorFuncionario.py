from Telas.TelaFuncionario import TelaFuncionario
from Telas.TelaCadastroFuncionario import TelaCadastroFuncionario
from Entidades.Funcionario import Funcionario
from Entidades.Funcionario import Cargo
from Controladores.ControladorVeiculo import ControladorVeiculo


class ControladorFuncionario:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_funcionario = TelaFuncionario(self)
        self.__tela_cadastro = TelaCadastroFuncionario(self)
        self.__funcionarios = {}
        self.__cargo = None
        self.__controlador_veiculo = ControladorVeiculo
        self.__controlador_principal = controlador_principal

    def __new__(cls, *args, **kwargs):
        if ControladorFuncionario.__instance is None:
            ControladorFuncionario.__instance = object.__new__(cls)
            return ControladorFuncionario.__instance

    def abre_funcionario(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        funcionarios = []
        for matricula in self.__funcionarios:
            funcionarios.append("Matrícula: " + str(self.__funcionarios[matricula].numero_matricula) + '  -  ' +
                                "Nome: " + self.__funcionarios[matricula].nome + '  -  ' +
                                "Data de Nascimento: " + self.__funcionarios[matricula].data_nascimento + '  -  ' +
                                "Telefone: " + self.__funcionarios[matricula].telefone + '  -  ' +
                                "Cargo: " + str(self.__funcionarios[matricula].cargo))

        button, values = self.__tela_funcionario.open(funcionarios)
        options = {9: self.voltar,
                   1: self.cadastra,
                   #  2: self.dar_acesso_veiculo,
                   #  3: self.veiculos_funcionario,
                   4: self.alterar_funcionario,
                   5: self.deletar_funcionario,}
                  # 6: self.desbloquear_funcionario}

        return options[button]()

    def cadastrar_funcionario(self, numero_matricula, nome, data_nascimento, telefone, cargo: Cargo):
        try:
            funcionario = Funcionario(numero_matricula, nome, data_nascimento, telefone, cargo)
            if self.existe_funcionario(numero_matricula):
                raise Exception
            else:
                self.__funcionarios[numero_matricula] = funcionario
                if funcionario.cargo == Cargo.DIRETORIA:
                    funcionario.veiculos = self.__controlador_principal.controlador_veiculo.veiculos
                    self.__tela_cadastro.show_message("Sucesso", "Funcionário cadastrado com sucesso")
                else:
                    self.dar_acesso_veiculo(numero_matricula)
                    self.__tela_cadastro.show_message("Sucesso", "Funcionário cadastrado com sucesso")
        except Exception:
            print("-----------------ATENÇÃO----------------- \n * Funcionário já cadastrado * ")

            self.__tela_cadastro.show_message("Erro", "Funcionário já cadastrado com essa matrícula")

    def cadastra(self):
        button, values = self.__tela_cadastro.open()
        try:
            matricula = int(values[0])
            if matricula:
                try:
                    nome = values[1]
                    data = values[2]
                    telefone = values[3]
                    cargo = values[4]
                    if nome == "" or data == "" or telefone == "" or cargo == "" or matricula == "":
                        raise Exception
                    else:
                        self.cadastrar_funcionario(matricula, nome, data, telefone, Cargo(self.cadastrar_cargo(cargo)))
                except Exception:
                    print("Todos os campos devem ser preenchidos!")
                    self.__tela_cadastro.show_message("Erro", "Todos os campos devem ser preenchidos")
            else:
                raise Exception
        except Exception:
            print("Matrícula do funcionário deve ser um número inteiro")
            self.__tela_cadastro.show_message("Erro", "Matrícula do funcionário deve ser um número inteiro")

        self.abre_funcionario()

    def cadastrar_cargo(self, cargo):
        if cargo == "Diretoria":
            cargo = 1
        elif cargo == "Comercial":
            cargo = 2
        else:
            cargo = 3
        return cargo

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

    def dar_acesso_veiculo(self, num_matricula=None):
        veiculos = self.__controlador_principal.controlador_veiculo.veiculos
        if not num_matricula:
            matricula = input("Digite a matricula do funcionário a ser autorizado: ")
        else:
            matricula = num_matricula

        funcionario = self.__funcionarios[matricula]
        if funcionario.cargo == Cargo.DIRETORIA:
            print("Este funcionário já tem acesso a todos os veiculos da garagem")
            print("Funcionário tem acesso aos seguintes veículos: ")
            self.__tela_funcionario.show_message("Erro",
                                                 "Este funcionário já tem acesso a todos os veiculos da garagem")

        placa = self.__tela_funcionario.ask_verification("Digite a placa do veículo que este funcionário terá acesso",
                                                         "Info")
        if placa not in veiculos:
            print("Não existe veículo com placa '" + str(placa) + "' na garagem")
            self.__tela_funcionario.show_message("Erro",
                                                 "Não existe veículo com placa '"
                                                 + str(placa) + "' na garagem")
            return
        veiculo = veiculos[placa]
        if placa not in funcionario.veiculos:
            funcionario.veiculos[placa] = veiculo
        else:
            print("Funcionário já tem acesso a esse veículo")
            self.__tela_funcionario.show_message("Erro",
                                                 "Funcionário já tem acesso a esse veículo")
        print("Funcionário tem acesso aos seguintes carros: ")
        keys = []
        for placa in funcionario.veiculos:
            keys.append("Placa: " + str(funcionario.veiculos[placa].placa) + " Modelo: " + str(
                funcionario.veiculos[placa].modelo))
        self.__tela_funcionario.show_message("Carros do funcionário", str(keys))

    def veiculos_funcionario(self):
        while True:
            try:
                matricula = int(input("Digite o número de matrícula do funcionário que deseja verificar: "))
                if matricula:
                    if matricula not in self.__funcionarios:
                        print("Não existe funcionário com matrícula '" + str(matricula) + "' cadastrado no sistema")
                    else:
                        funcionario = self.__funcionarios[matricula]
                        print("Funcionário tem acesso aos seguintes carros: ")
                        for carro in funcionario.veiculos:
                            print("PLACA: %s MODELO: %s"
                                  % (funcionario.veiculos[carro].placa, funcionario.veiculos[carro].modelo))
                        return
                else:
                    raise ValueError
            except ValueError:
                print("Matrícula é um número inteiro")

    def deletar_funcionario(self):
        try:
            matricula = int(self.__tela_funcionario.ask_verification("Informe a matrícula do funcionário", "Matrícula"))
            if matricula:
                if matricula in self.__funcionarios:
                    del self.__funcionarios[matricula]
                    print("Funcionário demitido com sucesso >:)")
                    self.__tela_funcionario.show_message("Sucesso", "Funcionário demitido com sucesso")
                else:
                    print("Não existe funcionário com esse número de matrícula")
                    self.__tela_funcionario.show_message("Erro", "Não existe funcionário com matrícula "
                                                         + str(matricula) + " cadastrado")
            else:
                raise ValueError
        except ValueError:
            print("Matrícula é um número inteiro")
            self.__tela_funcionario.show_message("Erro", "Matrícula deve ser um número inteiro")

        self.abre_funcionario()

    def alterar_funcionario(self):
        try:
            matricula_anterior = self.__tela_funcionario.ask_verification("Matrícula","Digite a matrícula do funcionário: ")
            matricula_anterior = int(matricula_anterior)
            if matricula_anterior:
                if matricula_anterior in self.__funcionarios:
                    print("Informe os novos valores: ")
                    button, new_values = self.__tela_cadastro.open(self.__funcionarios[matricula_anterior])
                    try:
                        matricula = int(new_values[0])
                        if matricula:
                            if matricula in self.__funcionarios:
                                print("Essa matrícula já está sendo utilizada por outro funcionário")
                                self.__tela_cadastro.show_message("Erro",
                                                                  "Essa matrícula já está sendo utilizada por outro funcionário" )
                            else:
                                nome = new_values[1]
                                data = new_values[2]
                                telefone = new_values[3]
                                cargo = Cargo(self.cadastrar_cargo(new_values[4]))
                                self.__funcionarios[matricula_anterior].numero_matricula = matricula
                                self.__funcionarios[matricula_anterior].nome = nome
                                self.__funcionarios[matricula_anterior].data_nascimento = data
                                self.__funcionarios[matricula_anterior].telefone = telefone
                                self.__funcionarios[matricula_anterior].cargo = cargo
                                self.__funcionarios[matricula] = self.__funcionarios.pop(matricula_anterior)
                                print("Funcionário alterado com sucesso")
                                self.__tela_cadastro.show_message("Sucesso", "Funcionário alterado com sucesso")
                        else:
                            raise ValueError
                    except ValueError:
                        print("Matrícula deve ser um número inteiro")
                        self.__tela_cadastro.show_message("Erro", "Matrícula deve ser um número inteiro")
            else:
                raise ValueError
        except ValueError:
            print("Matrícula deve ser um número inteiro")
            self.__tela_cadastro.show_message("Erro", "Matrícula deve ser um número inteiro")

        self.abre_funcionario()

    def desbloquear_funcionario(self):
        try:
            matricula = int(input("Digite o número de matrícula do funcionário: "))
            if matricula:
                if matricula in self.__funcionarios:
                    if self.__funcionarios[matricula].bloqueado:
                        self.__funcionarios[matricula].bloqueado = False
                        print("Funcionário desbloqueado com sucesso")
                    else:
                        print("Este funcionário já está desbloqueado")
                else:
                    print("Não existe funcionário com esse número de matrícula")
                return
            else:
                raise ValueError
        except ValueError:
            print("Matrícula é um número inteiro")

    @property
    def funcionarios(self):
        return self.__funcionarios

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
