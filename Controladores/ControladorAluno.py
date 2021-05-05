from Telas.TelaAluno import TelaAluno
from Telas.TelaCadastroAluno import TelaCadastroAluno
from Entidades.Aluno import Aluno
from Entidades.src.AlunoDAO import AlunoDAO
from Exceptions import AlunoJahExisteException
import re


class ControladorAluno:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_aluno = TelaAluno(self)
        self.__tela_cadastro = TelaCadastroAluno(self)
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
        for aluno in self.__alunos_DAO.get_all():
            if aluno.mensalidade and aluno.mensalidade[0] and aluno.mensalidade[0].valor:
                mensalidade = str(aluno.mensalidade[0].valor)
            else:
                mensalidade = ''

            alunos.append("CPF: " + str(aluno.cpf) + '  -  ' +
                          "Email: " + str(aluno.email) + '  -  ' +
                          "Nome: " + str(aluno.nome) + '  -  ' +
                          "Mensalidade: " + mensalidade + '  -  ' +
                          "Vencimento da mensalidade: " + str(aluno.venc_mensalidade))

        button, values = self.__tela_aluno.open(alunos)
        options = {4: self.voltar_lista()}

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
                                 values['nome'],
                                 values['senha'], values['mensalidade'], values['venc_mensalidade'])
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

                if aluno.mensalidade and aluno.mensalidade[0] and aluno.mensalidade[0].valor:
                    mensalidade = str(aluno.mensalidade[0].valor)
                else:
                    mensalidade = ''

                new_values = [aluno.cpf, aluno.nome, aluno.data_nasc, aluno.email, aluno.codigo, aluno.senha,
                              mensalidade, aluno.venc_mensalidade or '']

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
        self.__tela_cadastro.show_message("Sucesso",
                                          "Aluno cadastrado com sucesso")
        return True

    def excluir_aluno(self, values):
        if values['cpf']:
            cpf = values['cpf']
            aluno_found = self.__alunos_DAO.getByCpf(cpf)
            if aluno_found:
                if aluno_found.mensalidade and len(aluno_found.mensalidade) > 0:
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

    @property
    def alunos(self):
        return self.__alunos

    def voltar(self):
        self.__tela_cadastro.close()
        self.__controlador_principal.abre_tela_inicial()

    def voltar_lista(self):
        self.__tela_aluno.close()
        self.__controlador_principal.abre_tela_inicial()
