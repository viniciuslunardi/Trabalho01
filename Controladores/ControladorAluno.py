from Telas.TelaAluno import TelaAluno
from Telas.TelaCadastroAluno import TelaCadastroAluno
from Entidades.Aluno import Aluno
from Entidades.src.AlunoDAO import AlunoDAO
from Exceptions import AlunoJahExisteException


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
        for matricula in self.__alunos_DAO.get_all():
            alunos.append("CPF: " + str(matricula.data_nasc) + '  -  ' +
                          "Email: " + str(matricula.email) + '  -  ' +
                          "Nome: " + str(matricula.nome) + '  -  ' +
                          "Mensalidade: " + str(matricula.mensalidade) + '  -  ' +
                          "Vencimento da mensalidade: " + str(matricula.venc_mensalidade))

        button, values = self.__tela_aluno.open(alunos)
        options = {4: self.voltar,
                   1: self.cadastra}

        return options[button]()

    def cadastra(self):
        button, values = self.__tela_cadastro.open()
        try:
            nome = values[0]
            cpf = values[1]
            data_nasc = values[2]
            email = values[3]
            matricula = values[4]
            senha = values[5]
            mensalidade = float(values[6])
            venc_mensalidade = int(values[7])
            conta = None

            if not matricula:
                raise Exception("Aluno deve possuir uma matrícula única")
            if not cpf:
                raise Exception("Aluno deve possuir um CPF")
            if not nome:
                raise Exception("Aluno deve possuir um nome")

            if venc_mensalidade:
                mensalidade = int(mensalidade)
                if venc_mensalidade and 0 < venc_mensalidade < 30:
                    self.cadastrar_aluno(cpf, data_nasc, email, matricula, nome, senha, conta, mensalidade,
                                         venc_mensalidade)
                elif mensalidade:
                    raise Exception("Data de vencimento da mensalidade deve ser entre 1 e 30")
                else:
                    raise Exception("Deve ser informado um valor de mensalidade")

            else:
                raise ValueError
        except ValueError:
            self.__tela_cadastro.show_message("Erro", "Mensalidade e vencimento da mensalidade devem ser informados em número "
                                                      " (utilize '.' para números não inteiros)")
        except Exception as e:
            self.__tela_cadastro.show_message("Erro",e)


        self.voltar()

    def cadastrar_aluno(self, cpf, data_nasc, email, matricula, nome, senha, conta, mensalidade, venc_mensalidade,
                        msg=None):
        try:
            aluno = Aluno(cpf, data_nasc, email, matricula, nome, senha, conta, mensalidade, venc_mensalidade)

            if self.__alunos_DAO.get(matricula):
                raise AlunoJahExisteException

            else:
                self.__alunos_DAO.add(matricula, aluno)
                if not msg:
                    self.__tela_cadastro.show_message("Sucesso",
                                                      "Aluno cadastrado com sucesso")
                return True
        except Exception:
            print("---------------ATENÇÃO--------------- \n * Aluno já cadastrado *")
            self.__tela_cadastro.show_message("Erro",
                                              "Já existe um aluno com matrícula " + matricula + " cadastrada")
            return False

    @property
    def alunos(self):
        return self.__alunos

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
