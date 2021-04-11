from Telas.TelaPrincipal import TelaPrincipal
from Telas.TelaLogin import TelaLogin
from Controladores.ControladorFuncionario import ControladorFuncionario
from Controladores.ControladorAluno import ControladorAluno

class ControladorPrincipal:
    __instance = None

    def __init__(self):
        self.__tela_principal = TelaPrincipal(self)
        self.__tela_login = TelaLogin(self)
        self.__controlador_funcionario = ControladorFuncionario(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__user_session = None

    def __new__(cls, *args, **kwargs):
        if ControladorPrincipal.__instance is None:
            ControladorPrincipal.__instance = object.__new__(cls)
            return ControladorPrincipal.__instance

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

    def abre_tela_inicial(self):
        options = {0: self.funcionario, 1: self.aluno, 2: self.cadastra_func, 3: self.cadastra_alu}
        button, values = self.__tela_principal.open()
        return options[button]()

    def cadastra_func(self):
        self.__controlador_funcionario.cadastra()

    def cadastra_alu(self):
        self.__controlador_aluno.abre_tela_cadastro_aluno()

    def funcionario(self):
        self.__controlador_funcionario.abre_funcionario()

    def aluno(self):
        self.__controlador_aluno.abre_aluno()