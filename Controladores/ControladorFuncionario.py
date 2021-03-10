# -- coding: utf-8 --
from Telas.TelaFuncionario import TelaFuncionario
from Telas.TelaCadastroFuncionario import TelaCadastroFuncionario
from Entidades.Funcionario import Funcionario
from Entidades.Funcionario import Funcao
from Controladores.ControladorAluno import ControladorAluno
from Entidades.src.FuncionarioDAO import FuncionarioDAO
from Exceptions import FuncionarioJahExisteException


class ControladorFuncionario:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_funcionario = TelaFuncionario(self)
        self.__tela_cadastro = TelaCadastroFuncionario(self)
        self.__funcionarios = {}
        self.__funcionarios_DAO = FuncionarioDAO()
        self.__funcao = None
        self.__controlador_aluno = ControladorAluno
        self.__controlador_principal = controlador_principal

    def __new__(cls, *args, **kwargs):
        if ControladorFuncionario.__instance is None:
            ControladorFuncionario.__instance = object.__new__(cls)
            return ControladorFuncionario.__instance

    @property
    def funcionarios_DAO(self):
        return self.__funcionarios_DAO

    def abre_funcionario(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        funcionarios = []
        for usuario in self.__funcionarios_DAO.get_all():
            funcionarios.append("Usuário: " + str(usuario.usuario) + '  -  ' +
                                "Nome: " + usuario.nome + '  -  ' +
                                "Data de Nascimento: " + usuario.data_nascimento + '  -  ' +
                                "Telefone: " + usuario.email + '  -  ' +
                                "Função: " + str(usuario))

        button, values = self.__tela_funcionario.open(funcionarios)
        options = {9: self.voltar,
                   1: self.cadastra,
                   4: self.alterar_funcionario,
                   5: self.deletar_funcionario, }
        if button:
            return options[button]()

    def cadastrar_funcionario(self, usuario, senha, nome, cpf, data_nascimento, email,
                              conta_bancaria, carga_horaria, salario, funcao: Funcao, msg=None):
        try:
            funcionario = Funcionario(usuario, senha, nome, cpf, data_nascimento, email, conta_bancaria, carga_horaria, salario, funcao)
            if self.__funcionarios_DAO.get(usuario):
                raise FuncionarioJahExisteException
            else:
                self.__funcionarios[usuario] = funcionario
                if not msg:
                    self.__tela_cadastro.show_message("Sucesso", "Funcionário cadastrado com sucesso")
                self.__funcionarios_DAO.add(usuario, funcionario)

        except Exception:
            print("-----------------ATENÇÃO----------------- \n * Funcionário já cadastrado * ")

            self.__tela_cadastro.show_message("Erro", "Funcionário já cadastrado com essa matrícula")


    def cadastra(self):
        button, values = self.__tela_cadastro.open()
        try:
            usuario = values[0]
            if usuario:
                try:
                    senha = values[1]
                    nome = values[2]
                    data_nascimento = values[3]
                    email = values[4]
                    funcao = values[5]
                    cpf = values[6]
                    conta = values[7]
                    carga_horaria = values[8]
                    salario = values[9]
                    if senha == "" or nome == "" or data_nascimento == "" or email == "" or usuario == "" or funcao == "" or cpf == "" or conta == "" or carga_horaria == "" or salario == "":
                        raise Exception
                    else:
                        self.cadastrar_funcionario(usuario, senha, nome, cpf, data_nascimento, email, conta, carga_horaria, salario, Funcao(self.cadastrar_funcao(funcao)))
                except Exception:
                    print("Todos os campos devem ser preenchidos!")
                    self.__tela_cadastro.show_message("Erro", "Todos os campos devem ser preenchidos")
            else:
                raise Exception
        except Exception:
            print("Matrícula do funcionário deve ser um número inteiro")
            self.__tela_cadastro.show_message("Erro", "Matrícula do funcionário deve ser um número inteiro")

        self.abre_funcionario()

    def cadastrar_funcao(self, funcao):
        if funcao == "Gerente":
            funcao = 1
        elif funcao == "Professor":
            funcao = 2
        else:
            funcao = 3
        return funcao

    def lista_funcionario(self):
        if len(self.__funcionarios) > 0:
            for funcionario in self.__funcionarios:
                funcao = self.__funcionarios[funcionario].funcao
                if funcao == funcao.RECEPCIONISTA:
                    funcao = "Recepcionista"
                elif funcao == funcao.GERENTE:
                    funcao = "Gerente"
                else:
                    funcao = "Professor"
                print("NOME: ", str(self.__funcionarios[funcionario].nome),
                      "TELEFONE: ", str(self.__funcionarios[funcionario].telefone),
                      "FUNÇÃO: ", funcao)
                print("")
        else:
            print("Nenhum funcionário cadastrado")

    def existe_funcionario(self, usuario):
        return usuario in self.__funcionarios

    def get_alunos(self):
        return self.__controlador_principal.controlador_aluno.alunos_DAO

    def deletar_funcionario(self):
        usuario = (self.__tela_funcionario.ask_verification("Informe o usuario", "Usuario"))
        if usuario:
            try:
                usuario = int(usuario)
                if self.__funcionarios_DAO.get(usuario):
                    self.__funcionarios_DAO.remove(usuario)
                    print("Funcionário demitido com sucesso >:)")
                    self.__tela_funcionario.show_message("Sucesso", "Funcionário demitido com sucesso")
                else:
                    print("Não existe esse usuário")
                    self.__tela_funcionario.show_message("Erro", "Não existe funcionário com matrícula "
                                                         + str(usuario) + " cadastrado")
            except ValueError:
                print("Matrícula é um número inteiro")
                self.__tela_funcionario.show_message("Erro", "Matrícula deve ser um número inteiro")

        self.abre_funcionario()

    def alterar_funcionario(self):
        usuario_anterior = self.__tela_funcionario.ask_verification("Digite o usuario: ",
                                                                      "Usuario")
        if usuario_anterior:
            try:
                usuario_anterior = int(usuario_anterior)
                old = self.__funcionarios_DAO.get(usuario_anterior)
                if old:
                    alunos = old.alunos
                    print("Informe os novos valores: ")
                    button, new_values = self.__tela_cadastro.open(self.__funcionarios_DAO.get(usuario_anterior))
                    try:
                        usuario = int(new_values[0])
                        if usuario:
                            if self.__funcionarios_DAO.get(usuario) and usuario != usuario_anterior:
                                print("Essa matrícula já está sendo utilizada por outro funcionário")
                                self.__tela_cadastro.show_message("Erro",
                                                                  "Essa matrícula já está sendo utilizada por outro funcionário")
                            else:
                                nome = new_values[1]
                                data = new_values[2]
                                telefone = new_values[3]
                                msg = "Altera"
                                self.__funcionarios_DAO.remove(usuario_anterior)
                                new = Funcionario(usuario, nome, data, telefone,
                                                           Funcao(self.cadastrar_funcao(new_values[4])))
                                self.__funcionarios_DAO.add(usuario, new)
                                print("Funcionário alterado com sucesso")
                                self.__tela_cadastro.show_message("Sucesso", "Funcionário alterado com sucesso")

                        else:
                            raise ValueError
                    except ValueError:
                        print("Usuário deve ser um número inteiro")
                        self.__tela_cadastro.show_message("Erro", "Usuário deve ser um número inteiro")
                else:
                    raise ValueError
            except ValueError:
                print("Usuário deve ser um número inteiro")
                self.__tela_cadastro.show_message("Erro", "Usuário deve ser um número inteiro")

        self.abre_funcionario()

    @property
    def funcionarios(self):
        return self.__funcionarios

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
