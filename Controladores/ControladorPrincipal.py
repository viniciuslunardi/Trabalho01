from Telas.TelaPrincipal import TelaPrincipal
from Telas.TelaLogin import TelaLogin
from Telas.TelaContabilidade import TelaContabilidade
from Controladores.ControladorFuncionario import ControladorFuncionario
from Controladores.ControladorAluno import ControladorAluno
from Controladores.ControladorConta import ControladorConta
from Controladores.ControladorMensalidade import ControladorMensalidade
from Entidades.Gerente import Gerente
from Entidades.Recepcionista import Recepcionista
from Entidades.Mensalidade import Mensalidade


class ControladorPrincipal:
    __instance = None

    def __init__(self):
        self.__tela_principal = TelaPrincipal(self)
        self.__tela_login = TelaLogin(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_conta = ControladorConta(self)
        self.__tela_contabilidade = TelaContabilidade(self)
        self.__controlador_mensalidade = ControladorMensalidade(self)
        self.__user_session = None

    def __new__(cls, *args, **kwargs):
        if ControladorPrincipal.__instance is None:
            ControladorPrincipal.__instance = object.__new__(cls)
            return ControladorPrincipal.__instance

    @property
    def user_session(self):
        return self.__user_session

    def inicia(self):
        self.abre_tela_login()

    def abre_tela_login(self):
        button, values = self.__tela_login.open()

        if button != 2:
            codigo = values[0]
            senha = values[1]
            if codigo and senha:
                if self.__controlador_funcionario.funcionarios_DAO.get(codigo):
                    rec_senha = self.__controlador_funcionario.funcionarios_DAO.get(codigo).senha
                    if rec_senha == senha:
                        self.__user_session = self.__controlador_funcionario.funcionarios_DAO.get(codigo)
                        return self.abre_tela_inicial()
                    else:
                        self.__tela_login.show_message("Erro",
                                                       "Senha incorreta")

                elif self.__controlador_aluno.alunos_DAO.get(codigo):
                    rec_senha = self.__controlador_aluno.alunos_DAO.get(codigo).senha
                    if rec_senha == senha:
                        self.__user_session = self.__controlador_aluno.alunos_DAO.get(codigo)
                        return self.abre_tela_inicial()
                    else:
                        self.__tela_login.show_message("Erro",
                                                       "Senha incorreta")
                else:
                    print("Não existe usuario com esse login cadastrado no sistema")
                    self.__tela_login.show_message("Erro",
                                                   "Não existe usuario com esse login cadastrado no sistema")
        return self.abre_tela_login()


    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario

    @property
    def controlador_aluno(self):
        return self.__controlador_aluno

    @property
    def controlador_mensalidade(self):
        return self.__controlador_mensalidade

    @property
    def controlador_gerente(self):
        return self.__controlador_gerente

    def abre_tela_inicial(self):
        options = {0: self.funcionario, 1: self.aluno, 2: self.cadastra_func, 3: self.cadastra_alu, 4: self.open_alunos_inadimplentes, 5: self.cadastra_conta, 6: self.cadastra_mensalidade, 888: self.contas, 78: self.salarios, 66: self.contabilidade}

        button, values = self.__tela_principal.open()
        return options[button]()

    def cadastra_conta(self):
        self.__controlador_conta.cadastra()

    def cadastra_func(self):
        self.__controlador_funcionario.cadastra()

    def cadastra_alu(self):
        self.__controlador_aluno.abre_tela_cadastro_aluno()

    def cadastra_mensalidade(self):
        self.__controlador_mensalidade.abre_mensalidade()

    def funcionario(self):
        self.__controlador_funcionario.abre_funcionario()

    def aluno(self):
        self.__controlador_aluno.abre_aluno()

    def open_alunos_inadimplentes(self):
        self.__controlador_aluno.listar_alunos_inadimplentes()

    def contas(self):
        self.__controlador_conta.abre_contas()

    def salarios(self):
        self.__controlador_funcionario.abre_salarios()

    def voltar(self):
        self.abre_tela_inicial()

    def contabilidade(self):
        fluxo_caixa = []
        user = self.__user_session
        if isinstance(user, Gerente) or isinstance(user, Recepcionista) and user is not None:
            for usuario in self.__controlador_funcionario.funcionarios_DAO.get_all():
                try:
                    if usuario.pagamentos:
                        for pagamento in usuario.pagamentos:
                            fluxo_caixa.append("Tipo: Salário - SAÍDA - " +
                                               "Valor: " + str(pagamento.valor) + '  -  ' +
                                               "Funcionário: " + str(usuario.codigo))
                except:
                    ValueError('Error')

            for mensalidade in self.__controlador_mensalidade.mensalidades_DAO.get_all():
                if mensalidade.pago == 'Sim' or mensalidade.pago == True:
                    fluxo_caixa.append("Tipo: Mensalidade - ENTRADA - " +
                                       "Valor: " + str(mensalidade.valor) + '  -  ' +
                                       "Identificador: " + str(mensalidade.identificador))

            for conta in self.__controlador_conta.contas_DAO.get_all():
                if not conta.paga:
                    fluxo_caixa.append("Tipo: Conta - SAÍDA - " +
                                       "Valor: " + str(conta.valor) + '  -  '
                                       "Nome: " + str(conta.nome))

        else:
            self.__tela_principal.show_message("Erro",
                                               "Você não tem permissão para verificar o relatório de fluxo de caixa.")
            return self.voltar()

        button, values = self.__tela_contabilidade.open(fluxo_caixa)
        options = {4: self.voltar}
        if button:
            return options[button]()