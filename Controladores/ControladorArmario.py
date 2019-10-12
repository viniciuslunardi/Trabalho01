from Telas.TelaArmario import TelaArmario
from Entidades.Registro import Registro, EventoRegistro
from datetime import datetime


class ControladorArmario:
    def __init__(self, controlador_principal):
        self.__tela_armario = TelaArmario(self)
        self.__chaves = {}
        self.__chaves_emprestadas = {}
        self.__controlador_principal = controlador_principal

    def abre_armario(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {0: self.voltar,
                    1: self.veiculos_na_garagem,
                    2: self.pegar_veiculo,
                    3: self.devolver_chave,
                    4: self.veiculos_emprestados}
        while True:
            opcao = self.__tela_armario.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

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
            matricula = input("Digite o seu número de matrícula: ")
            if not self.__controlador_principal.controlador_funcionario.existe_funcionario(matricula):
                # EMITIR REGISTRO ACESSO NEGADO
                evento = EventoRegistro(2)
                data = datetime.now().strftime('%d/%m/%Y %H:%M')
                motivo = "Tentou acessar uma matrícula de funcionário não cadastrada no sistema"
                registro = Registro(data, "Não existe", motivo, None, evento)
                self.__controlador_principal.controlador_registro.imprime_registro(registro)
                print("Não existe funcionário com matrícula '" + str(matricula) + "' cadastrado no sistema")
            else:
                funcionario = self.__controlador_principal.controlador_funcionario.funcionarios
                veiculos_funcionario = funcionario[matricula].veiculos

                if len(veiculos_funcionario) > 1:
                    placa = input("Digite a placa do veículo que deseja utilizar: ")
                    if placa not in veiculos_garagem:
                        # EMITIR REGISTRO ACESSO NEGADO
                        print("Não existe veículo com placa '" + str(placa) + "' na garagem")
                    elif placa not in veiculos_funcionario:
                        # EMITIR REGISTRO ACESSO NEGADO
                        print("Funcionário não tem acesso a este veiculo")
                        if tentativas == 1:
                            print("----------------CUIDADO!----------------"
                                  " \n Mais uma tentativa de acesso a veículo não permitido irá bloquear seu acesso")
                        tentativas += 1
                    elif placa not in self.__chaves_emprestadas or len(self.__chaves_emprestadas) == 0:
                        # EIMITIR REGISTRO ACESSO PERMITIDO
                        chave = veiculos_funcionario[placa].placa
                        self.__chaves_emprestadas[chave] = veiculos_funcionario[placa]
                        funcionario[matricula].veiculo_usado[placa] = veiculos_funcionario[placa]
                        print("Pode pegar a chave do veículo %s"
                              % (veiculos_garagem[placa].modelo))
                        return
                    else:
                        # EMITIR REGISTRO ACESSO NEGADO
                        print("Esse veículo não está disponível no momento")
                elif len(veiculos_funcionario) == 1:
                    placa = list(veiculos_funcionario)
                    if placa[0] not in self.__chaves_emprestadas:
                        # EMITIR REGISTRO ACESSO PERMITIDO
                        chave = veiculos_funcionario[placa[0]].placa
                        self.__chaves_emprestadas[chave] = veiculos_funcionario[placa[0]]
                        funcionario[matricula].veiculo_usado[chave] = veiculos_funcionario[placa[0]]
                        print("Retire seu veiculo")
                        return
                    else:
                        # EVENTO ACESSO NEGADO
                        print("O único veículo que este funcionário tem acesso está indisponível")
                        return
                else:
                    print("Funcionário não tem acesso a nenhum carro")
                    if len(funcionario) == 1:
                        return

        if tentativas == 3:
            # EMITIR EVENTO ACESSO BLOQUEADO
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
            matricula = input("Digite seu número de matrícula: ")
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
                                    self.__controlador_principal.controlador_veiculo\
                                        .atualiza_quilometragem(placa, km_andado)
                                    print("Veículo devolvido com sucesso")
                                    return
                            except ValueError:
                                print("Quilometros andados devem ser informados com números "
                                      "(usando '.' para  números não inteiros)")
                else:
                    print("Este funcionário não está usando nenhum veículo")

    @property
    def chaves(self):
        return self.__chaves

    @property
    def chaves_emprestadas(self):
        return self.__chaves_emprestadas

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
