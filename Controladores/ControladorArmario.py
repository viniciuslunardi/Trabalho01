from Telas.TelaArmario import TelaArmario
from Entidades.Registro import Registro, EventoRegistro
from Entidades.src.ArmarioDAO import ArmarioDAO
from datetime import datetime


class ControladorArmario:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_armario = TelaArmario(self)
        self.__chaves_emprestadas = {}
        self.__armario_DAO = ArmarioDAO()
        self.__controlador_principal = controlador_principal


    def __new__(cls, *args, **kwargs):
        if ControladorArmario.__instance is None:
            ControladorArmario.__instance = object.__new__(cls)
            return ControladorArmario.__instance

    def abre_armario(self):
        self.abre_tela_inicial()


    def abre_tela_inicial(self):
        veiculos_garagem = self.veiculos_na_garagem()
        button, values = self.__tela_armario.open(veiculos_garagem)
        options = {9: self.voltar,
                   2: self.pegar_veiculo,
                   3: self.devolver_chave,
                   4: self.veiculos_emprestados}

        return options[button]()
        # while True:
        #     opcao = self.__tela_armario.mostrar_opcoes()
        #     funcao_escolhida = switcher[opcao]
        #     funcao_escolhida()

    def veiculos_na_garagem(self):
        veiculos = self.__controlador_principal.controlador_veiculo.veiculos_DAO.get_all()
        print(self.__armario_DAO.get_all(), "armarioo")
        veiculos_garagem = []
        for veiculo in veiculos:
            if not self.__armario_DAO.get(veiculo.placa):
                veiculos_garagem.append("Placa: " + veiculo.placa + '  -  ' +
                                        "Modelo: " + veiculo.modelo)
                print("MODELO: %s PLACA: %s" % (veiculo.modelo, veiculo.placa))
        return veiculos_garagem

    def get_veiculos(self):
        return self.__controlador_principal.controlador_veiculo.veiculos_DAO

    def get_funcionarios(self):
        return self.__controlador_principal.controlador_funcionario.funcionarios_DAO

    def pegar_veiculo(self):
        self.veiculos_na_garagem()
        veiculos_disp = []
        veiculos_garagem = self.get_veiculos()
        for plate in veiculos_garagem.get_all():
            veiculos_disp.append(plate)

        if len(veiculos_disp) == 0:
            self.__tela_armario.show_message("Erro", "Não existem veículos na garagem.")
        else:
            matricula = (self.__tela_armario.ask_verification("Digite o seu número de matrícula", "Info"))
            if matricula:
                try:
                    matricula = int(matricula)
                    funcionarios = self.get_funcionarios()
                    if not funcionarios.get(matricula):
                        # EMITIR REGISTRO ACESSO NEGADO
                        evento = EventoRegistro(2)
                        data = datetime.now().strftime('%d/%m/%Y %H:%M')
                        motivo = "Tentou acessar uma matrícula de funcionário não cadastrado no sistema"
                        registro = Registro(data, None, motivo, None, evento)
                        self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                        self.__controlador_principal.controlador_registro.imprime_registro(registro)
                        self.__tela_armario.show_message("ACESSO NEGADO", "Não existe funcionário com matrícula '"
                                                         + str(matricula) + "' cadastrado no sistema")
                        print("Não existe funcionário com matrícula '" + str(matricula) + "' cadastrado no sistema")
                    else:
                        funcionario = funcionarios.get(matricula)
                        veic_func = []
                        veiculos_funcionario = funcionario.veiculos
                        print(veiculos_funcionario)
                        for p in veiculos_funcionario:
                            veic_func.append(p)
                        print(veic_func)
                        if not funcionario.bloqueado:
                            if len(veiculos_funcionario) > 1:
                                placa = self.__tela_armario.ask_verification("Digite a placa do veículo que deseja utilizar: ", "Info")
                                if not veiculos_garagem.get(placa):
                                    # EMITIR REGISTRO ACESSO NEGADO
                                    evento = EventoRegistro(2)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Não existe veículo com esta placa cadastrado no sistema"
                                    self.__tela_armario.show_message("ACESSO NEGADO", motivo)
                                    registro = Registro(data, matricula, motivo, None, evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    print("Não existe veículo com placa '" + str(placa) + "' na garagem")
                                elif placa not in veiculos_funcionario:
                                    # EMITIR REGISTRO ACESSO NEGADO
                                    evento = EventoRegistro(2)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Tentou acessar um veículo que não tem permissão"
                                    self.__tela_armario.show_message("ACESSO NEGADO", motivo)
                                    registro = Registro(data, matricula, motivo, placa, evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    print("Funcionário não tem acesso a este veiculo")
                                    if funcionario.tentativas == 1:
                                        print("----------------CUIDADO!----------------"
                                              "\nMais uma tentativa de acesso a veículo "
                                              "não permitido irá bloquear seu acesso")
                                    funcionario.tentativas += 1
                                    if funcionario.tentativas > 2:
                                        self.get_funcionarios().remove(funcionario.numero_matricula)
                                        evento = EventoRegistro(3)
                                        data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                        motivo = "Tentou acessar veículo que não tem permissão por 3 vezes"
                                        self.__tela_armario.show_message("BLOQUEADO",
                                                                         "Tentou acessar veículo que não tem permissão por 3 vezes")
                                        registro = Registro(data, matricula, motivo, placa, evento)
                                        self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                        self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                        funcionario.bloqueado = True
                                        self.get_funcionarios().add(funcionario.numero_matricula, funcionario)
                                elif not self.__armario_DAO.get(placa):
                                    # EIMITIR REGISTRO ACESSO PERMITIDO
                                    evento = EventoRegistro(1)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Funcionário tem acesso ao veículo que tentou retirar."
                                    registro = Registro(data, matricula, motivo, placa, evento)
                                    self.__tela_armario.show_message("ACESSO PERMITIDO", motivo + " "
                                                                                                  " Retire o veículo")
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    chave = veiculos_funcionario[placa].placa
                                    self.__armario_DAO.add(placa, veiculos_funcionario[placa])
                                    self.get_funcionarios().remove(funcionario.numero_matricula)
                                    self.__chaves_emprestadas[chave] = veiculos_funcionario[placa]
                                    funcionario.veiculo_usado[placa] = veiculos_funcionario[placa]
                                    self.get_funcionarios().add(funcionario.numero_matricula, funcionario)

                                else:
                                    # EMITIR REGISTRO ACESSO NEGADO
                                    evento = EventoRegistro(2)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Tentou acessar veículo que não está disponível no momento"
                                    self.__tela_armario.show_message("ACESSO NEGADO", motivo)
                                    registro = Registro(data, matricula, motivo, placa, evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    print("Esse veículo não está disponível no momento")

                            elif len(veiculos_funcionario) == 1:
                                placa = list(veiculos_funcionario.keys())
                                if not self.__armario_DAO.get(placa[0]):
                                    # EMITIR REGISTRO ACESSO PERMITIDO
                                    evento = EventoRegistro(1)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Funcionário tem acesso ao veículo que tentou retirar"
                                    registro = Registro(data, matricula, motivo, placa[0], evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    chave = veiculos_funcionario[placa[0]].placa
                                   # veiculo = self.get_veiculos().get(placa[0])
                                    self.__armario_DAO.add(chave, veiculos_funcionario[placa[0]])
                                    self.get_funcionarios().remove(matricula)
                                    funcionario.veiculo_usado[chave] = veiculos_funcionario[placa[0]]
                                    self.get_funcionarios().add(funcionario.numero_matricula, funcionario)
                                    self.__tela_armario.show_message("ACESSO PERMITIDO", "Funcionário pode retirar o veículo")
                                    print("Retire seu veiculo")

                                else:
                                    # EVENTO ACESSO NEGADO
                                    evento = EventoRegistro(2)
                                    data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                    motivo = "Tentou acessar veículo que não está disponível no momento"
                                    registro = Registro(data, matricula, motivo, placa, evento)
                                    self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                    self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                    self.__tela_armario.show_message("ACESSO NEGADO", motivo)
                                    print("O único veículo que este funcionário tem acesso está indisponível")

                            else:
                                evento = EventoRegistro(2)
                                data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                motivo = "Funcionário não tem acesso a nenhum veículo"
                                registro = Registro(data, matricula, motivo, None, evento)
                                self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                                self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                self.__tela_armario.show_message("ACESSO NEGADO", motivo)
                                print("Funcionário não tem acesso a nenhum carro")


                        else:
                            evento = EventoRegistro(2)
                            data = datetime.now().strftime('%d/%m/%Y %H:%M')
                            motivo = "Funcionário está com o acesso bloqueado"
                            registro = Registro(data, matricula, motivo, None, evento)
                            self.__controlador_principal.controlador_registro.cadastrar_registro(registro)
                            self.__controlador_principal.controlador_registro.imprime_registro(registro)
                            self.__tela_armario.show_message("ACESSO NEGADO", motivo)
                except ValueError:
                    print("Matrícula deve ser um número inteiro")
        self.abre_armario()


    def veiculos_emprestados(self):
        veiculos_emprestados = []
        for placa in self.__armario_DAO.get_all():
            veiculos_emprestados.append("Placa: " + placa.placa + '  -  ' +
                                        "Modelo: " + placa.modelo)
        self.__tela_armario.show_message("Veículos emprestados", str(veiculos_emprestados))
        self.abre_armario()

    def devolver_chave(self):
        veiculos = self.get_veiculos()
        matricula = (self.__tela_armario.ask_verification("Digite seu número de matrícula", "Info"))
        if matricula:
            try:
                matricula = int(matricula)
                if not self.get_funcionarios().get(matricula):
                    print("Não existe funcionário com matrícula '" + str(matricula) + "' cadastrado no sistema")
                    self.__tela_armario.show_message("Erro", "Não existe funcionário"
                                                             " com matrícula '" + str(matricula) + "' cadastrado no sistema")
                else:
                    funcionario = self.get_funcionarios().get(matricula)
                    if len(funcionario.veiculo_usado) >= 1:
                        placa = self.__tela_armario.ask_verification("Digite a placa do veículo que vai devolver: ","Info")
                        if not veiculos.get(placa):
                            print("Não existe veículo com placa '" + str(placa) + "' na garagem")
                            self.__tela_armario.show_message("Erro", "Não existe veículo com placa '" + str(placa) + "' na garagem")
                            self.abre_armario()
                        else:
                            if placa not in funcionario.veiculo_usado:
                                print("Funcionário não está utilizando veículo com placa igual a " + str(placa))
                                self.__tela_armario.show_message("Erro",
                                                                 "Funcionário não está utilizando veículo com placa igual a " + str(placa) )
                            else:
                                km_andado = (
                                    self.__tela_armario.ask_verification("Informe o número de quilometros andados",
                                                                         "Info"))
                                if km_andado:
                                    km_andado = float(km_andado)
                                    try:
                                        del funcionario.veiculo_usado[placa]
                                        # EMITIR EVENTO VEICULO DEVOLVIDO
                                        evento = EventoRegistro(4)
                                        data = datetime.now().strftime('%d/%m/%Y %H:%M')
                                        motivo = "Devolveu o veículo"
                                        registro = Registro(data, matricula, motivo, placa, evento)
                                        self.__controlador_principal.controlador_registro.cadastrar_registro(
                                            registro)
                                        self.__controlador_principal.controlador_registro.imprime_registro(registro)
                                        self.__controlador_principal.controlador_veiculo \
                                            .atualiza_quilometragem(placa, km_andado)
                                        print("Veículo devolvido com sucesso")

                                        atualiza = self.get_veiculos().get(placa)
                                        self.get_veiculos().remove(placa)
                                        self.get_funcionarios().remove(funcionario.numero_matricula)
                                        self.__armario_DAO.remove(placa)
                                        self.get_funcionarios().add(funcionario.numero_matricula, funcionario)
                                        self.get_veiculos().add(placa, atualiza)
                                        self.__tela_armario.show_message("Sucesso", "Veiculo devolvido com sucesso")
                                    except ValueError:
                                        print("Quilometros andados devem ser informados com números "
                                        "(usando '.' para  números não inteiros)")
                                        self.__tela_armario.show_message("Erro", "Quilometros andados devem ser informados com números "
                                        "(usando '.' para  números não inteiros)")
                    else:
                        print("Este funcionário não está usando nenhum veículo")
                        self.__tela_armario.show_message("Erro",
                                                         "Este funcionário não está usando nenhum veículo")

            except ValueError:
                print("Matricula deve ser um número inteiro")
                self.__tela_armario.show_message("Erro", "Matricula deve ser um número inteiro")
        self.abre_armario()

    @property
    def chaves_emprestadas(self):
        return self.__chaves_emprestadas

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
