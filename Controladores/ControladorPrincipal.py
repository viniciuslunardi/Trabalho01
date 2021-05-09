from Telas.TelaPrincipal import TelaPrincipal
from Telas.TelaLogin import TelaLogin
from Controladores.ControladorFuncionario import ControladorFuncionario
from Controladores.ControladorAluno import ControladorAluno
from Controladores.ControladorConta import ControladorConta
from Controladores.ControladorMensalidade import ControladorMensalidade

class ControladorPrincipal:
    __instance = None

    def __init__(self):
        self.__tela_principal = TelaPrincipal(self)
        self.__tela_login = TelaLogin(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_mensalidade = ControladorMensalidade(self)
        self.__controlador_conta = ControladorConta(self)
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
        options = {0: self.funcionario, 1: self.aluno, 2: self.cadastra_func, 3: self.cadastra_alu, 4: self.open_alunos_inadimplentes, 5: self.cadastra_conta, 6: self.cadastra_mensalidade, 888: self.contas}

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