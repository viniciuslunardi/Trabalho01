from Telas.TelaArmario import TelaArmario
from Entidades.Registro import Registro, EventoRegistro
from datetime import datetime


class ControladorArmario:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_armario = TelaArmario(self)
        self.__chaves_emprestadas = {}
        self.__controlador_principal = controlador_principal

    def __new__(cls, *args, **kwargs):
        if ControladorArmario.__instance is None:
            ControladorArmario.__instance = object.__new__(cls)
            return ControladorArmario.__instance

    def abre_armario(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):

        self.__tela_armario.open()
        # switcher = {0: self.voltar,
        #             1: self.veiculos_na_garagem,
        #             2: self.pegar_veiculo,
        #             3: self.devolver_chave,
        #             4: self.veiculos_emprestados}
        # while True:
        #     opcao = self.__tela_armario.mostrar_opcoes()
        #     funcao_escolhida = switcher[opcao]
        #     funcao_escolhida()

    def veiculos_na_garagem(self):
        veiculos = self.__controlador_principal.controlador_veiculo.veiculos
        print("---------------GARAGEM---------------")
        if len(self.__chaves_emprestadas) == len(veiculos):
            print("Nenhum veículo na garagem no momento")
        else:
            for veiculo in veiculos:
                if veiculo not in self.__chaves_emprestadas:
                    print("MODELO: %s PLACA: %s" % (veiculos[veiculo].modelo, veiculos[veiculo].placa))

    def pegar_veiculo(self):
        self.veiculos_na_garagem()
        tentativas = 0
        veiculos_garagem = self.__controlador_principal.controlador_veiculo.veiculos
        while tentativas < 3:
            if len(veiculos_garagem) == 0:
                return
            try:
                matricula = int(input("Digite o seu número de matrícula: "))
                if matricula:
                    if not self.__controlador_principal.controlador_funcionario.existe_funcionario(matricula):
                        # EMITIR REGISTRO ACESSO NEGADO
                        evento = EventoRegistro(2)
                        data = datetime.now().strftime('%d/%m/%Y %H:%M')
                        motivo = "Tentou acessar uma matrícula de funcionário não cadastrado no sistema"
                        registro = Registro(data, None, motivo, None, evento)
                        self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                        self.__controlador_principal.controlador_registro.imprime_registro(registro)
                        print("Não existe funcionário com matrícula '" + str(matricula) + "' cadastrado no sistema")
                        return
                    else:
                        funcionario = self.__controlador_principal.controlador_funcionario.funcionarios
                        veiculos_funcionario = funcionario[matricula].veiculos
                        if not funcionario[matricula].bloqueado:
                            if len(veiculos_funcionario) > 1:
                                placa = input("Digite a placa do veículo que deseja utilizar: ")
                                if placa not in veiculos_garagem:
                                    # EMITIR REGISTRO ACESSO NEGADO
                                    evento = EventoRegistro(2)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Não existe veículo com esta placa cadastrado no sistema"
                                    registro = Registro(data, matricula, motivo, None, evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    print("Não existe veículo com placa '" + str(placa) + "' na garagem")
                                    return
                                elif placa not in veiculos_funcionario:
                                    # EMITIR REGISTRO ACESSO NEGADO
                                    evento = EventoRegistro(2)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Tentou acessar um veículo que não tem permissão"
                                    registro = Registro(data, matricula, motivo, placa, evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    print("Funcionário não tem acesso a este veiculo")
                                    if tentativas == 1:
                                        print("----------------CUIDADO!----------------"
                                              "\nMais uma tentativa de acesso a veículo "
                                              "não permitido irá bloquear seu acesso")
                                    tentativas += 1
                                    if tentativas > 2:
                                        evento = EventoRegistro(3)
                                        data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                        motivo = "Tentou acessar veículo que não tem permissão por 3 vezes"
                                        registro = Registro(data, matricula, motivo, placa, evento)
                                        self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                        self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                        funcionario[matricula].bloqueado = True
                                elif placa not in self.__chaves_emprestadas or len(self.__chaves_emprestadas) == 0:
                                    # EIMITIR REGISTRO ACESSO PERMITIDO
                                    evento = EventoRegistro(1)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Funcionário tem acesso ao veículo que tentou retirar"
                                    registro = Registro(data, matricula, motivo, placa, evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    chave = veiculos_funcionario[placa].placa
                                    self.__chaves_emprestadas[chave] = veiculos_funcionario[placa]
                                    funcionario[matricula].veiculo_usado[placa] = veiculos_funcionario[placa]
                                    print("Pode pegar a chave do veículo %s"
                                          % (veiculos_garagem[placa].modelo))
                                    return
                                else:
                                    # EMITIR REGISTRO ACESSO NEGADO
                                    evento = EventoRegistro(2)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Tentou acessar veículo que não está disponível no momento"
                                    registro = Registro(data, matricula, motivo, placa, evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    print("Esse veículo não está disponível no momento")
                                    return
                            elif len(veiculos_funcionario) == 1:
                                placa = list(veiculos_funcionario)
                                if placa[0] not in self.__chaves_emprestadas:
                                    # EMITIR REGISTRO ACESSO PERMITIDO
                                    evento = EventoRegistro(1)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Funcionário tem acesso ao veículo que tentou retirar"
                                    registro = Registro(data, matricula, motivo, placa[0], evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    chave = veiculos_funcionario[placa[0]].placa
                                    self.__chaves_emprestadas[chave] = veiculos_funcionario[placa[0]]
                                    funcionario[matricula].veiculo_usado[chave] = veiculos_funcionario[placa[0]]
                                    print("Retire seu veiculo")
                                    return
                                else:
                                    # EVENTO ACESSO NEGADO
                                    evento = EventoRegistro(2)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Tentou acessar veículo que não está disponível no momento"
                                    registro = Registro(data, matricula, motivo, placa, evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    print("O único veículo que este funcionário tem acesso está indisponível")
                                    return
                            else:
                                evento = EventoRegistro(2)
                                data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                motivo = "Funcionário não tem acesso a nenhum veículo"
                                registro = Registro(data, matricula, motivo, None, evento)
                                self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                print("Funcionário não tem acesso a nenhum carro")
                                if len(funcionario) == 1:
                                    return
                        else:
                            evento = EventoRegistro(2)
                            data = datetime.now().strftime('%d/%m/%Y %H:%M')
                            motivo = "Funcionário está com o acesso bloqueado"
                            registro = Registro(data, matricula, motivo, None, evento)
                            self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                            self.__controlador_principal.controlador_registro.imprime_registro(registro)
                            return
                else:
                    raise ValueError
            except ValueError:
                print("Matrícula deve ser um número inteiro")
        if tentativas == 3:
            print("Acesso bloqueado")

    def veiculos_emprestados(self):
        veiculos = self.__controlador_principal.controlador_veiculo.veiculos
        print("---------VEÍCULOS EMPRESTADOS--------")
        for veiculo in veiculos:
            if veiculo in self.__chaves_emprestadas:
                print("MODELO: %s PLACA: %s" % (veiculos[veiculo].modelo, veiculos[veiculo].placa))

    def devolver_chave(self):
        veiculos = self.__controlador_principal.controlador_veiculo.veiculos
        if len(self.__chaves_emprestadas) == 0:
            print("----------------------------------------------")
            print("Todos os veículos da garagem estão disponíveis")
            return
        while True:
            try:
                matricula = int(input("Digite seu número de matrícula: "))
                if matricula:
                    if not self.__controlador_principal.controlador_funcionario.existe_funcionario(matricula):
                        print("Não existe funcionário com matrícula '" + str(matricula) + "' cadastrado no sistema")
                    else:
                        funcionario = self.__controlador_principal.controlador_funcionario.funcionarios[matricula]
                        if len(funcionario.veiculo_usado) >= 1:
                            placa = input("Digite a placa do veículo que vai devolver: ")
                            if not self.__controlador_principal.controlador_veiculo.existe_veiculo(placa):
                                print("Não existe veículo com placa '" + str(placa) + "' na garagem")
                            else:
                                if placa not in funcionario.veiculo_usado:
                                    print("Funcionário não está utilizando veículo com placa igual a " + str(placa))
                                else:
                                    try:
                                        km_andado = float(input("Informe o número de quilometros andados: "))
                                        if km_andado:
                                            chave = veiculos[placa].placa
                                            del self.__chaves_emprestadas[chave]
                                            del funcionario.veiculo_usado[placa]
                                            # EMITIR EVENTO VEICULO DEVOLVIDO
                                            evento = EventoRegistro(4)
                                            data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                            motivo = "Devolveu o veículo"
                                            registro = Registro(data, matricula, motivo, placa, evento)
                                            self.__controlador_principal.controlador_registro.cadastrar_registro(
                                                registro)
                                            self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                            self.__controlador_principal.controlador_veiculo\
                                                .atualiza_quilometragem(placa, km_andado)
                                            print("Veículo devolvido com sucesso")
                                            return
                                    except ValueError:
                                        print("Quilometros andados devem ser informados com números "
                                              "(usando '.' para  números não inteiros)")
                        else:
                            print("Este funcionário não está usando nenhum veículo")
                else:
                    raise ValueError
            except ValueError:
                print("Matricula deve ser um número inteiro")

    @property
    def chaves_emprestadas(self):
        return self.__chaves_emprestadas

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
