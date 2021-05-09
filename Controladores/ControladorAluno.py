from Telas.TelaAluno import TelaAluno
from Telas.TelaCadastroAluno import TelaCadastroAluno
from Telas.TelaAlunosInadimplentes import TelaAlunosInadimplentes
from Entidades.Aluno import Aluno
from Entidades.src.AlunoDAO import AlunoDAO
from Entidades.Gerente import Gerente
from Entidades.Recepcionista import Recepcionista

import re


class ControladorAluno:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_aluno = TelaAluno(self)
        self.__tela_cadastro = TelaCadastroAluno(self)
        self.__tela_alunos_inadimpletes = TelaAlunosInadimplentes(self)
        self.__alunos = {}
        self.__alunos_DAO = AlunoDAO()
        self.__controlador_principal = controlador_principal

    def __new__(cls, *args, **kwargs):
        if ControladorAluno.__instance is None:
            ControladorAluno.__instance = object.__new__(cls)
            return ControladorAluno.__instance

    def abre_aluno(self):
        self.abre_tela_inicial()

    @property
    def alunos_DAO(self):
        return self.__alunos_DAO

    @property
    def tela_aluno(self):
        return self.__tela_aluno

    def atualizar_alunos(self):
        return self.__alunos_DAO.get_all()

    def abre_tela_inicial(self):
        alunos = []
        for codigo in self.__alunos_DAO.get_all():
            alunos.append("CPF: " + str(codigo.cpf) + '  -  ' +
                          "Email: " + str(codigo.email) + '  -  ' +
                          "Nome: " + str(codigo.nome) + '  -  ' +
                          "Vencimento da mensalidade: Todo dia " + str(codigo.venc_mensalidade))

        button, values = self.__tela_aluno.open(alunos)
        options = {4: self.voltar, 11: self.pagar_mensalidade}

        return options[button]()

    def abre_tela_cadastro_aluno(self, pre_values=None, excluir_visible=False, disable_all_fields=False):
        button, values = self.__tela_cadastro.open(alunos=pre_values, excluir_visible=excluir_visible,
                                                   disable_all_fields=disable_all_fields)

        options = {'voltar': self.voltar,
                   'salvar': self.pre_cadastro_aluno,
                   'buscar': self.busca_aluno,
                   'excluir': self.excluir_aluno}

        values = {
            "cpf": values[0],
            "nome": values[1],
            "data_nasc": values[2] + '/' + values[3] + '/' + values[4],
            "email": values[5],
            "codigo": values[6],
            "senha": values[7],
            "mensalidade": values[8],
            "venc_mensalidade": values[9],
        }

        if button != 'voltar':
            return options[button](values)
        else:
            return options[button]()

    def valida_cpf_aluno(self, cpf):
        try:
            if len(cpf) != 11 or not cpf.isdigit():
                raise Exception('CPF inválido')
            aluno_cpf_utilizado = self.__alunos_DAO.getByCpf(cpf)
            if aluno_cpf_utilizado:
                raise Exception('Já existe um aluno com este CPF cadastrado no sistema')
        except Exception as err:
            raise Exception(err or 'CPF inválido')

    def valida_codigo_aluno(self, codigo):
        try:
            aluno_codigo_utilizado = self.__alunos_DAO.get(codigo)
            if aluno_codigo_utilizado:
                raise Exception('Código já utilizado por outro usuário')
        except Exception as err:
            raise Exception(err or 'Código inválido')

    def valida_data_nasc(self, data_nasc):
        try:
            [dia, mes, ano] = data_nasc.split('/')
            if (1 <= int(dia) <= 31) and (1 <= int(mes) <= 12) and (1900 <= int(ano) < 2021):
                return True
            else:
                raise Exception
        except Exception as err:
            raise Exception('Data de nascimento inválida')

    def valida_email(self, email):
        try:
            if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
                raise Exception('Email inválido')
            return True
        except Exception as err:
            raise Exception(err or 'Email inválido')

    def valida_venc_mensalidade(self, venc_mensalidade):
        try:
            if not (0 < int(venc_mensalidade) < 31):
                raise Exception
            return True
        except Exception:
            raise Exception('Dia de vencimento da mensalidade inválido')

    def valida_mensalidade(self, mensalidade):
        try:
            if not (0 <= float(mensalidade)):
                raise Exception
            return True
        except Exception:
            raise Exception('Mensalidade inválida')

    def valida_aluno(self, values):
        # try:
        self.valida_cpf_aluno(values['cpf'])
        self.valida_codigo_aluno(values['codigo'])
        self.valida_data_nasc(values['data_nasc'])
        self.valida_email(values['email'])
        if values['venc_mensalidade']:
            self.valida_venc_mensalidade(values['venc_mensalidade'])
        if values['mensalidade']:
            self.valida_mensalidade(values['mensalidade'])

        if not values['codigo']:
            raise Exception("Aluno deve possuir um código único")
        if not values['cpf']:
            raise Exception("Aluno deve possuir um CPF")
        if not values['nome']:
            raise Exception("Aluno deve possuir um nome")

    def pre_cadastro_aluno(self, values):
        try:
            self.valida_aluno(values)
            self.cadastrar_aluno(values['cpf'], values['data_nasc'], values['email'], values['codigo'],
                                 values['nome'], values['senha'], values['mensalidade'], values['venc_mensalidade'])
            self.voltar()

        except Exception as e:
            self.__tela_cadastro.show_message("Erro", e)
            self.__tela_cadastro.close()
            self.abre_tela_cadastro_aluno(list(values.values()))

    def busca_aluno(self, values):
        try:
            cpf = values['cpf']
            aluno = self.__alunos_DAO.getByCpf(cpf)
            if aluno:

                if aluno.valor_mensalidade:
                    valor_mensalidade = str(aluno.valor_mensalidade)
                else:
                    valor_mensalidade = ''

                new_values = [aluno.cpf, aluno.nome, aluno.data_nasc, aluno.email, aluno.codigo, aluno.senha,
                              valor_mensalidade, aluno.venc_mensalidade or '']

                self.__tela_cadastro.close()
                self.abre_tela_cadastro_aluno(new_values, True, disable_all_fields=True)
            else:
                self.__tela_cadastro.show_message("Aluno não encontrado",
                                                  "Não foi encontrado um aluno com o CPF informado")
                self.__tela_cadastro.close()
                self.abre_tela_cadastro_aluno(list(values.values()))


        except Exception as e:
            print(e)

    def cadastrar_aluno(self, cpf, data_nasc, email, codigo, nome, senha, mensalidade, venc_mensalidade):
        aluno = Aluno(cpf, data_nasc, email, codigo, nome, senha, mensalidade, venc_mensalidade)

        self.__alunos_DAO.add(codigo, aluno)
        new_mensalidade = aluno.mensalidades[0]
        self.__controlador_principal.controlador_mensalidade.mensalidades_DAO.add(new_mensalidade.identificador,
                                                                                  new_mensalidade)
        self.__tela_cadastro.show_message("Sucesso",
                                          "Aluno cadastrado com sucesso")
        return True

    def excluir_aluno(self, values):
        if values['cpf']:
            cpf = values['cpf']
            aluno_found = self.__alunos_DAO.getByCpf(cpf)
            if aluno_found:
                if aluno_found.mensalidades and len(aluno_found.mensalidades) > 0:
                    self.__tela_cadastro.show_message("Erro", "Aluno possui mensalidades em aberto")
                    self.voltar()
                else:
                    self.__alunos_DAO.remove(aluno_found.codigo)
                    self.__tela_cadastro.show_message("Sucesso", "Aluno excluído com sucesso")
                    self.voltar()
            else:
                self.__tela_cadastro.show_message("Erro", "Não existe um aluno com o CPF informado")
                self.__tela_cadastro.close()
                self.abre_tela_cadastro_aluno(list(values.values()))

    def listar_alunos_inadimplentes(self):
        todos_os_alunos = self.__alunos_DAO.get_all()
        alunos_inadimplentes = []
        for aluno in todos_os_alunos:
            atrasadas = aluno.tem_mensalidade_atrasada()
            if len(atrasadas) > 0:
                alunos_inadimplentes.append("Nome: " + str(aluno.nome) + '  -  ' +
                                            "Email: " + str(aluno.email) + '  -  ' +
                                            "cpf: " + str(aluno.cpf))

        button, values = self.__tela_alunos_inadimpletes.open(alunos_inadimplentes)
        options = {4: self.voltar}

        return options[button]()

    def pagar_mensalidade(self):
        user = self.__controlador_principal.user_session
        if isinstance(user, Gerente) or isinstance(user, Recepcionista) and user is not None:
            codigo_aluno = (self.__tela_aluno.ask_verification("Informe o codigo do aluno", "codigo"))

            if codigo_aluno:
                usuario = self.__alunos_DAO.get(codigo_aluno)
                if usuario:
                    identificador = (
                        self.__tela_aluno.ask_verification("Informe o identificador da mensalidade", "identificador"))
                    mensalidade_to_pay = None
                    for mensalidade in usuario.mensalidades:
                        if mensalidade.identificador == identificador:
                            mensalidade_to_pay = mensalidade
                            usuario.mensalidades.remove(mensalidade)
                    if mensalidade_to_pay:
                        if mensalidade_to_pay.pago:
                            self.__tela_aluno.show_message("Erro", "Essa mensalidade já foi marca como paga.")
                        else:
                            mensalidade_to_pay.pago = True
                            usuario.mensalidades.append(mensalidade_to_pay)
                            new_user = usuario
                            self.__alunos_DAO.remove(codigo_aluno)
                            self.__alunos_DAO.add(codigo_aluno, new_user)
                            self.__controlador_principal.controlador_mensalidade.mensalidades_DAO.remove(
                                mensalidade_to_pay.identificador)
                            self.__controlador_principal.controlador_mensalidade.mensalidades_DAO.add(
                                mensalidade_to_pay.identificador, mensalidade_to_pay)
                            self.__tela_aluno.show_message("Sucesso", "Mensalidade marcada como paga com sucesso")
                            self.voltar()
                    else:
                        self.__tela_aluno.show_message("Erro", "Não existe uma mensalidade com o identificador '" + str(
                            identificador) + "' cadastrada.")

                else:
                    self.__tela_aluno.show_message("Erro", "Não existe aluno(a) com esse codigo '" + str(
                        codigo_aluno) + "' cadastrado(a).")

            else:
                if codigo_aluno == "":
                    self.__tela_cadastro.show_message("Erro",
                                                      "Identificador deve ser informado.")
                else:
                    self.voltar()
                    return
        self.voltar()

    @property
    def alunos(self):
        return self.__alunos

    def voltar(self):
        self.__tela_cadastro.close()
        self.__controlador_principal.abre_tela_inicial()

    def voltar_lista(self):
        self.__tela_aluno.close()
        self.__controlador_principal.abre_tela_inicial()
