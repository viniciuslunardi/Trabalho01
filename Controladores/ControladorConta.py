# -- coding: utf-8 --
from Telas.TelaCadastraConta import TelaCadastraConta
from Telas.TelaContas import TelaContas
from Entidades.Conta import Conta
from Entidades.Gerente import Gerente
from Entidades.Recepcionista import Recepcionista
from Controladores.ControladorAluno import ControladorAluno
from Entidades.src.ContaDAO import ContaDAO
from Exceptions import ContaJahExisteException


class ControladorConta:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_contas = TelaContas(self)
        self.__tela_cadastro = TelaCadastraConta(self)
        self.__contas = {}
        self.__contas_DAO = ContaDAO()
        self.__controlador_aluno = ControladorAluno
        self.__controlador_principal = controlador_principal

    def __new__(cls, *args, **kwargs):
        if ControladorConta.__instance is None:
            ControladorConta.__instance = object.__new__(cls)
            return ControladorConta.__instance

    @property
    def contas_DAO(self):
        return self.__contas_DAO

    def abre_contas(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        contas = []
        for conta in self.__contas_DAO.get_all():
            text = 'Não'
            if conta.paga:
                text = 'Sim'
            contas.append("Idenfifcador: " + str(conta.identificador) + '  -  ' +
                                "Nome: " + conta.nome + '  -  ' +
                                "Data de Vencimento: " + conta.data_venc + '  -  ' +
                                "Valor (R$): " + str(conta.valor) + '  -  ' +
                                "Descrição: " + conta.descricao + '  -  ' +
                                "Paga: " + text)

        button, values = self.__tela_contas.open(contas)
        options = {4: self.voltar, 9: self.deletar_conta, 10: self.pagar_conta}
        if button:
            return options[button]()

    def cadatrar_conta(self, identificador, nome, data_venc, valor, descricao, paga):
        try:
            identificador = int(identificador)
            try:
                valor = float(valor)
            except ValueError:
                self.__tela_cadastro.show_message("Erro",
                                                  "Valor da conta deve ser numérico. (Utilize '.' para números não inteiros")
            try:
                if self.__contas_DAO.get(identificador):
                    raise ContaJahExisteException
                else:
                    conta = Conta(identificador, nome, data_venc, valor, descricao, paga)
                    self.__contas[identificador] = conta

                    self.__contas_DAO.add(identificador, conta)
                    self.__tela_cadastro.show_message("Sucesso",
                                                      "Conta cadastrada com sucesso")
            except:
                print("-----------------ATENÇÃO----------------- \n * Conta já cadastrada * ")
                self.__tela_cadastro.show_message("Erro", "Conta já cadastrada com esse identificador.")

        except ValueError:
            self.__tela_cadastro.show_message("Erro",
                                              "Identificador deve ser um valor numérico inteiro.")

    def cadastra(self):
        user = self.__controlador_principal.user_session
        if isinstance(user, Gerente) or isinstance(user, Recepcionista) and user is not None:
            button, values = self.__tela_cadastro.open()
            identificador = values[0]
            if identificador:
                try:
                    nome = values[1]
                    data_venc = values[2]
                    valor = values[3]
                    descricao = values[4]
                    paga = values[5]
                    if identificador == "" or nome == "" or data_venc == "" or valor == "" or descricao == "" or paga == "":
                        raise Exception
                    else:
                        p = False
                        if paga == 'Sim':
                            p = True

                        self.cadatrar_conta(identificador, nome, data_venc, valor, descricao, p)
                except Exception:
                    print("Todos os campos devem ser preenchidos!")
                    self.__tela_cadastro.show_message("Erro", "Todos os campos devem ser preenchidos")
        else:
            self.__tela_contas.show_message("Erro", "Você não tem permissão para adicionar uma conta.")
        self.voltar()

    def deletar_conta(self):
        user = self.__controlador_principal.user_session
        if isinstance(user, Gerente) and user is not None:
            identificador = (self.__tela_contas.ask_verification("Informe o identificador da conta", "Identificador"))

            if identificador:
                try:
                    identificador = int(identificador)
                    if self.__contas_DAO.get(identificador):
                        self.__contas_DAO.remove(identificador)
                        self.__tela_contas.show_message("Sucesso", "Conta removida com sucesso")
                    else:
                        self.__tela_contas.show_message("Erro", "Não existe uma conta com o identificador '" + str(identificador) + "' cadastrada.")
                except ValueError:
                    self.__tela_cadastro.show_message("Erro",
                                                  "Identificador deve ser um valor numérico inteiro.")
            else:
                self.__tela_cadastro.show_message("Erro",
                                                  "Identificador deve ser informado.")
        else:
            self.__tela_contas.show_message("Erro", "Você não tem permissão para remover uma conta.")
        self.abre_contas()

    def pagar_conta(self):
        user = self.__controlador_principal.user_session
        if isinstance(user, Gerente) or isinstance(user, Recepcionista) and user is not None:
            identificador = (self.__tela_contas.ask_verification("Informe o identificador da conta", "Identificador"))

            if identificador:
                try:
                    identificador = int(identificador)
                    if self.__contas_DAO.get(identificador):
                        conta = self.__contas[identificador]
                        if conta.paga:
                            self.__tela_contas.show_message("Erro", "Essa conta já foi marca como paga.")
                        else:
                            conta.paga = True
                            self.__contas[identificador] = conta
                            self.__contas_DAO.remove(identificador)
                            self.__contas_DAO.add(identificador, conta)
                            self.__tela_contas.show_message("Sucesso", "Conta paga com sucesso")
                    else:
                        self.__tela_contas.show_message("Erro", "Não existe uma conta com o identificador '" + str(
                            identificador) + "' cadastrada.")
                except ValueError:
                    self.__tela_cadastro.show_message("Erro",
                                                      "Identificador deve ser um valor numérico inteiro.")
            else:
                self.__tela_cadastro.show_message("Erro",
                                                  "Identificador deve ser informado.")

        else:
            self.__tela_contas.show_message("Erro", "Você não tem permissão para marcar uma conta como paga.")
        self.abre_contas()

    @property
    def contas(self):
        return self.__contas

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
