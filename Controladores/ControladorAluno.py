from Telas.TelaAluno import TelaAluno
from Telas.TelaCadastroAluno import TelaCadastroAluno
from Telas.TelaAlunosInadimplentes import TelaAlunosInadimplentes
from Entidades.Aluno import Aluno
from Entidades.src.AlunoDAO import AlunoDAO
from Entidades.Mensalidade import Mensalidade
from Exceptions import AlunoJahExisteException
import datetime
import random
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
        # alunos = []
        # for codigo in self.__alunos_DAO.get_all():
        #     alunos.append("CPF: " + str(codigo.data_nasc) + '  -  ' +
        #                   "Email: " + str(codigo.email) + '  -  ' +
        #                   "Nome: " + str(codigo.nome) + '  -  ' +
        #                   "Mensalidade: " + str(codigo.mensalidade) + '  -  ' +
        #                   "Vencimento da mensalidade: " + str(codigo.venc_mensalidade))
        #
        # button, values = self.__tela_aluno.open(alunos)
        # options = {4: self.voltar,
        #            1: self.cadastra,
        #            5: self.add_mensalidade}
        #
        # return options[button]()
        return False

    def abre_tela_cadastro_aluno(self):
        button, values = self.__tela_cadastro.open()

        options = {4: self.voltar,
                   'salvar': self.pre_cadastro_aluno,
                   'buscar': self.busca_aluno}

        values = {
            "cpf": values[0],
            "nome": values[1],
            "data_nasc": values[2] + '/' + values[3] + '/' + values[4],
            "email": values[5],
            "codigo": values[6],
            "senha": values[7],
            "venc_mensalidade": values[8],
        }

        return options[button](values)

    def valida_cpf_aluno(self, cpf):
        try:
            if len(cpf) != 11 or not cpf.isdigit():
                raise Exception('CPF inválido')
            aluno_cpf_utilizado = self.__alunos_DAO.get(cpf)
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
            raise Exception('Código inválido')

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

    def valida_aluno(self, values):
        # try:
        self.valida_cpf_aluno(values['cpf'])
        self.valida_codigo_aluno(values['codigo'])
        self.valida_data_nasc(values['data_nasc'])
        self.valida_email(values['email'])
        self.valida_venc_mensalidade(values['venc_mensalidade'])

        if not values['codigo']:
            raise Exception("Aluno deve possuir um código único")
        if not values['cpf']:
            raise Exception("Aluno deve possuir um CPF")
        if not values['nome']:
            raise Exception("Aluno deve possuir um nome")

        if values['venc_mensalidade']:
            self.cadastrar_aluno(values['cpf'], values['data_nasc'], values['email'], values['codigo'], values['nome'],
                                 values['senha'], values['venc_mensalidade'])

        else:
            raise ValueError

    # except ValueError:
    #     self.__tela_cadastro.show_message("Erro",
    #                                       "Mensalidade e vencimento da mensalidade devem ser informados em número "
    #                                       " (utilize '.' para números não inteiros)")
    # except Exception as e:
    #     self.__tela_cadastro.show_message("Erro", e)

    def pre_cadastro_aluno(self, values):
        try:
            self.valida_aluno(values)

            if not values['codigo']:
                raise Exception("Aluno deve possuir um código único")
            if not values['cpf']:
                raise Exception("Aluno deve possuir um CPF")
            if not values['nome']:
                raise Exception("Aluno deve possuir um nome")

            if values['venc_mensalidade']:

                if values["venc_mensalidade"] and 0 < values["venc_mensalidade"] < 30:
                    self.cadastrar_aluno(values)
                elif mensalidade:
                    raise Exception("Data de vencimento da mensalidade deve ser entre 1 e 30")
            else:
                raise ValueError

        except ValueError:
            self.__tela_cadastro.show_message("Erro",
                                              "Vencimento da mensalidade deve ser informados em número "
                                              " (utilize '.' para números não inteiros)")
        except Exception as e:
            self.__tela_cadastro.show_message("Erro", e)

    def busca_aluno(self, values):
        try:
            cpf = values['cpf']
            if not self.__alunos_DAO.getByCpf(cpf):
                self.__tela_cadastro.show_message("Aluno não encontrado",
                                                  "Não foi encontrado um aluno com o CPF informado")
            return True
        except Exception:
            return False

    def cadastrar_aluno(self, cpf, data_nasc, email, codigo, nome, senha, venc_mensalidade,
                        msg=None):
        try:
            # mensalidades hardcode
            random_int_dia =  random.randint(1, 30)
            random_int_mes =  random.randint(1, 12)
            random_int_ano =  random.randint(2019, 2021)
            vencimento = datetime.datetime(random_int_ano, random_int_mes,random_int_dia)

            random_pago = random.randint(0,1)
            random_valor = random.randint(50, 300)
            mensalidades = []
            new_mensalidade = Mensalidade("descricao hardcoded", bool(random_pago),random_valor, vencimento)
            mensalidades.append(new_mensalidade)
            
            aluno = Aluno(cpf, data_nasc, email, codigo, nome, senha, mensalidades, venc_mensalidade)

            if self.__alunos_DAO.get(codigo):
                raise AlunoJahExisteException

            else:
                self.__alunos_DAO.add(codigo, aluno)
                if not msg:
                    self.__tela_cadastro.show_message("Sucesso",
                                                      "Aluno cadastrado com sucesso")
                return True
        except Exception:
            print("---------------ATENÇÃO--------------- \n * Aluno já cadastrado *")
            self.__tela_cadastro.show_message("Erro",
                                              "Já existe um aluno com codigo " + codigo + " cadastrada")
            return False

    # def add_mensalidade(self, descricao, pago, valor, vencimento):
        # cpf = self.__tela_funcionario.ask_verification("Digite o cpf do aluno: ",
        #                                                             "cpf")
        # aluno = self.__alunos_DAO.get(cpf)
        # new_mensalidade = Mensalidade(descricao, pago, valor, vencimento)
        # aluno.mensalidades.append(new_mensalidade)

    def listar_alunos_inadimplentes(self):
        todos_os_alunos = self.__alunos_DAO.get_all()
        alunos_inadimplentes = []
        for aluno in todos_os_alunos:
            if aluno.tem_mensalidade_atrasada():
                alunos_inadimplentes.append("Nome: " + str(aluno.senha) + '  -  ' +
                          "Email: " + str(aluno.nome) + '  -  ' +
                          "cpf: " + str(aluno.codigo))

        button, values = self.__tela_alunos_inadimpletes.open(alunos_inadimplentes)
        options = {4: self.voltar} 

        return options[button]()

    @property
    def alunos(self):
        return self.__alunos

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
