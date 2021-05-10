# -- coding: utf-8 --
from Telas.TelaFuncionario import TelaFuncionario
from Telas.TelaCadastroFuncionario import TelaCadastroFuncionario
from Telas.TelaPagamentoFuncionarios import TelaMarcaPagamentoFuncionario
from Entidades.Funcionario import Funcionario
from Telas.TelaSalarios import TelaSalarios
from Entidades.Gerente import Gerente
from Entidades.Professor import Professor
from Entidades.Recepcionista import Recepcionista
from Entidades.PagamentoFuncionarios import PagamentoFuncionario
from Controladores.ControladorAluno import ControladorAluno
from Entidades.src.FuncionarioDAO import FuncionarioDAO
from Exceptions import FuncionarioJahExisteException


class ControladorFuncionario:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_funcionario = TelaFuncionario(self)
        self.__tela_cadastro = TelaCadastroFuncionario(self)
        self.__tela_add_pagamento = TelaMarcaPagamentoFuncionario(self)
        self.__funcionarios = {}
        self.__funcionarios_DAO = FuncionarioDAO()
        self.__controlador_aluno = ControladorAluno
        self.__controlador_principal = controlador_principal
        self.__tela_salarios = TelaSalarios(self)

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
                   5: self.deletar_funcionario,
                   10: self.open_add_pagamento_screen, }
        if button:
            return options[button]()

    def abre_salarios(self):
        salarios = []
        user = self.__controlador_principal.user_session
        if isinstance(user, Gerente) and user is not None:
            for usuario in self.__funcionarios_DAO.get_all():
                try:
                    if usuario.pagamentos:
                        for pagamento in usuario.pagamentos:
                            salarios.append("Funcionário: " + usuario.codigo + '  -  ' +
                                            "Data do pagamento: " + pagamento.data_pagamento + '  -  ' +
                                            "Descrição: " + pagamento.descricao + '  -  ' +
                                            "Valor: " + pagamento.valor + '  -  ' +
                                            "Identificador: " + pagamento.identificador)
                except:
                    ValueError('Error')
        elif isinstance(user, Professor) or isinstance(user, Recepcionista) and user is not None:
            usuario = self.__funcionarios_DAO.get(user.codigo)
            if usuario:
                try:
                    if usuario.pagamentos:
                        for pagamento in usuario.pagamentos:
                            salarios.append("Funcionário: " + usuario.codigo + '  -  ' +
                                            "Data do pagamento: " + pagamento.data_pagamento + '  -  ' +
                                            "Descrição: " + pagamento.descricao + '  -  ' +
                                            "Valor: " + pagamento.valor + '  -  ' +
                                            "Identificador: " + pagamento.identificador)
                except:
                    salarios.append('Nenhum pagamento registrado ainda.')
                    ValueError('Error')
        else:
            self.__tela_funcionario.show_message("Erro",
                                                 "Você não tem permissão para verificar o relatório de salários.")

        button, values = self.__tela_salarios.open(salarios)
        options = {4: self.voltar}
        if button:
            return options[button]()

    def cadastrar_funcionario(self, codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria, salario,
                              cargo, pagamentos):
        try:
            if cargo == 'Gerente':
                funcionario = Gerente(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                      salario, pagamentos)

            elif cargo == 'Professor':
                funcionario = Professor(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                        salario, pagamentos)
            else:
                funcionario = Recepcionista(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                            salario, pagamentos)

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
        user = self.__controlador_principal.user_session
        if isinstance(user, Gerente):
            button, values = self.__tela_cadastro.open()

            codigo = values[0]
            if codigo:
                try:
                    senha = values[1]
                    nome = values[2]
                    data_nasc = values[3]
                    email = values[4]
                    cpf = values[5]
                    pix = values[6]
                    carga_horaria = int(values[7])
                    salario = int(values[8])
                    cargo = values[9]

                    if not senha or not cpf or not nome or not email or not data_nasc or not pix or not cargo or not carga_horaria or not salario:
                        raise Exception()
                    else:
                        pagamentos = []
                        self.cadastrar_funcionario(codigo, senha, nome, cpf, data_nasc, email, pix,
                                                   carga_horaria, salario, cargo, pagamentos)
                except ValueError:
                    self.__tela_cadastro.show_message("Erro", "Salario e carga horaria sao numeros inteiros")
                except Exception:
                    print("Todos os campos devem ser preenchidos!")
                    self.__tela_cadastro.show_message("Erro", "Todos os campos devem ser preenchidos")
            else:
                self.__tela_cadastro.show_message("Erro", "codigo nao pode ser vazio")
        else:
            self.__tela_funcionario.show_message("Erro", "Você não tem permissão para adicionar um funcionário.")
        self.voltar()

    def existe_funcionario(self, usuario):
        return usuario in self.__funcionarios

    def deletar_funcionario(self):
        codigo_usuario = (self.__tela_funcionario.ask_verification("Informe o codigo do usuario", "Codigo"))
        if codigo_usuario:
            try:
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
                old = self.__funcionarios_DAO.get(codigo_usuario_anterior)
                if old:
                    print("Informe os novos valores: ")
                    button, new_values = self.__tela_cadastro.open(old)
                    try:
                        codigo = new_values[0]
                        if codigo:
                            if self.__funcionarios_DAO.get(codigo) and codigo != codigo_usuario_anterior:
                                self.__tela_cadastro.show_message("Erro",
                                                                  "Esse codigo já está sendo utilizada por outro funcionário")
                            else:

                                senha = new_values[1]
                                nome = new_values[2]
                                data_nasc = new_values[3]
                                email = new_values[4]
                                cpf = new_values[5]
                                pix = new_values[6]
                                carga_horaria = int(new_values[7])
                                salario = int(new_values[8])
                                cargo = new_values[9]

                                msg = "Altera"
                                if cargo == 'Gerente':
                                    new = Gerente(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                                  salario)
                                elif cargo == 'Professor':
                                    new = Professor(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
                                                    salario)
                                else:
                                    new = Recepcionista(codigo, senha, nome, cpf, data_nasc, email, pix, carga_horaria,
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

    def open_add_pagamento_screen(self):
        codigo_usuario = self.__tela_add_pagamento.ask_verification("Digite o codigo do funcionario: ",
                                                                    "codigo")
        if codigo_usuario:
            try:
                usuario = self.__funcionarios_DAO.get(codigo_usuario)
                if usuario:
                    button, values = self.__tela_add_pagamento.open()
                    options = {4: self.voltar, 5: self.add_pagamento(values, usuario, codigo_usuario)}
                    if button:
                        options[button]()
                else:
                    self.__tela_add_pagamento.show_message("Erro", "Funcionario nao encontrado")
            except Exception as e:
                print("error", e)
            self.voltar()

    def add_pagamento(self, values, usuario, codigo_usuario):
        try:
            codigo = values[0]
            if codigo:
                data_pag = str(values[1] + '/' + values[2] + '/' + values[3])
                valor = values[4]
                descricao = values[5]
                new = PagamentoFuncionario(codigo, data_pag, valor, descricao)
                usuario.pagamentos.append(new)

                self.__funcionarios_DAO.remove(codigo_usuario)
                self.__funcionarios_DAO.add(codigo_usuario, usuario)
                self.__tela_cadastro.show_message("Sucesso", "Pagamento adicionado")
        except Exception as e:
            print("error", e)
        self.voltar()

    @property
    def funcionarios(self):
        return self.__funcionarios

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
