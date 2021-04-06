# -- coding: utf-8 --
from Telas.TelaFuncionario import TelaFuncionario
from Telas.TelaCadastroFuncionario import TelaCadastroFuncionario
from Entidades.Funcionario import Funcionario
from Entidades.Gerente import Gerente
from Entidades.Professor import Professor
from Entidades.Recepcionista import Recepcionista
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
            funcionarios.append("Codigo do usuário: " + usuario.codigo + '  -  ' +
                                "Nome: " + usuario.nome + '  -  ' +
                                "Data de Nascimento: " + usuario.data_nasc + '  -  ' +
                                "Email: " + usuario.email)

        button, values = self.__tela_funcionario.open(funcionarios)
        options = {9: self.voltar,
                   4: self.alterar_funcionario,
                   5: self.deletar_funcionario, }
        if button:
            return options[button]()

    def cadastrar_funcionario(self, codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria, salario,
                              cargo):
        try:
            if cargo == 'Gerente':
                funcionario = Gerente(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                      salario)
                
            elif cargo == 'Professor':
                funcionario = Professor(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                        salario)
            else:
                funcionario = Recepcionista(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                            salario)

            if self.__funcionarios_DAO.get(codigo):
                raise FuncionarioJahExisteException
            else:
                self.__funcionarios[codigo] = funcionario

                self.__funcionarios_DAO.add(codigo, funcionario)

            self.__tela_cadastro.show_message("Pronto.", "funcionario cadastrado")

        except Exception:
            print("-----------------ATENÇÃO----------------- \n * Funcionário já cadastrado * ")

            self.__tela_cadastro.show_message("Erro", "Funcionário já cadastrado com esse código")

    def cadastra(self):
        button, values = self.__tela_cadastro.open()

        codigo = values[0]
        if codigo:
            try:
                senha = values[1]
                nome = values[2]
                cpf = values[3]
                data_nasc = values[4]
                email = values[5]
                pix = values[6]
                cargo = values[9]
                carga_horaria = int(values[7])
                salario = int(values[8])

                if not senha or not cpf or not nome or not email or not data_nasc or not pix or not cargo or not carga_horaria or not salario:
                    raise Exception()
                else:
                    self.cadastrar_funcionario(codigo, senha, nome, cpf, data_nasc, email, pix,
                                               carga_horaria, salario, cargo)
            except ValueError:
                    self.__tela_cadastro.show_message("Erro", "Salario e carga horaria sao numeros inteiros")
            except Exception:
                print("Todos os campos devem ser preenchidos!")
                self.__tela_cadastro.show_message("Erro", "Todos os campos devem ser preenchidos")
        else:
            self.__tela_cadastro.show_message("Erro", "codigo nao pode ser vazio")
        self.voltar()

    def existe_funcionario(self, usuario):
        return usuario in self.__funcionarios

    def deletar_funcionario(self):
        codigo_usuario = (self.__tela_funcionario.ask_verification("Informe o codigo do usuario", "Codigo"))
        if codigo_usuario:
            try:
                codigo_usuario = codigo_usuario
                if self.__funcionarios_DAO.get(codigo_usuario):
                    self.__funcionarios_DAO.remove(codigo_usuario)
                    print("Funcionário deletado com sucesso >:)")
                    self.__tela_funcionario.show_message("Sucesso", "Funcionário deletado com sucesso")
                else:
                    print("Não existe esse codigo de usuario")
                    self.__tela_funcionario.show_message("Erro", "Não existe funcionário com esse codigo "
                                                         + codigo_usuario + " cadastrado")
            except Exception as e:
                print("error", e)

        self.abre_funcionario()

    def alterar_funcionario(self):
        codigo_usuario_anterior = self.__tela_funcionario.ask_verification("Digite o codigo do funcionario: ",
                                                                    "codigo")
        if codigo_usuario_anterior:
            try:
                codigo_usuario_anterior = codigo_usuario_anterior
                old = self.__funcionarios_DAO.get(codigo_usuario_anterior)
                if old:
                    print("Informe os novos valores: ")
                    # todo: bug estranhao q troca os valor tudo
                    button, new_values = self.__tela_cadastro.open(self.__funcionarios_DAO.get(codigo_usuario_anterior))
                    try:
                        codigo = new_values[0]
                        if codigo:
                            if self.__funcionarios_DAO.get(codigo) and codigo != codigo_usuario_anterior:
                                self.__tela_cadastro.show_message("Erro",
                                                                  "Esse codigo já está sendo utilizada por outro funcionário")
                            else:
                                nome = new_values[1]
                                senha = new_values[1]
                                nome = new_values[2]
                                cpf = new_values[3]
                                data_nasc = new_values[4]
                                email = new_values[5]
                                pix = new_values[6]
                                cargo = new_values[9]
                                carga_horaria = int(new_values[7])
                                salario = int(new_values[8])

                                msg = "Altera"
                                if cargo == 'Gerente':
                                    new = Gerente(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                      salario)
                                elif cargo == 'Professor':
                                    new = Professor(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                      salario)
                                else:
                                    new = Gerente(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                      salario)
                                
                                self.__funcionarios_DAO.remove(codigo_usuario_anterior)
                                self.__funcionarios_DAO.add(codigo, new)
                                self.__tela_cadastro.show_message("Sucesso", "Funcionário alterado com sucesso")
                    except Exception as e:
                        print("error", e)
                else:
                    self.__tela_cadastro.show_message("Erro", "Funcionario nao encontrado")
            except Exception as e:
                print("error", e)

        self.abre_funcionario()

    @property
    def funcionarios(self):
        return self.__funcionarios

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
