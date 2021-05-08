from Telas.TelaMensalidades import TelaMensalidades
from Telas.TelaCadastroMensalidade import TelaCadastroMensalidade
from Entidades.src.AlunoDAO import AlunoDAO
from Entidades.src.MensalidadeDAO import MensalidadeDAO
from Entidades.Mensalidade import Mensalidade


class ControladorMensalidade:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_mensalidades = TelaMensalidades(self)
        self.__tela_cadastro = TelaCadastroMensalidade(self)
        self.__alunos = {}
        self.__alunos_DAO = AlunoDAO()
        self.__mensalidades_DAO = MensalidadeDAO()
        self.__controlador_principal = controlador_principal

    def __new__(cls, *args, **kwargs):
        if ControladorMensalidade.__instance is None:
            ControladorMensalidade.__instance = object.__new__(cls)
            return ControladorMensalidade.__instance

    def abre_mensalidade(self):
        self.abre_tela_inicial()

    @property
    def alunos_DAO(self):
        return self.__alunos_DAO

    @property
    def tela_mensalidades(self):
        return self.__tela_mensalidades

    def atualizar_alunos(self):
        return self.__alunos_DAO.get_all()

    def abre_tela_inicial(self):
        mensalidades = []
        for aluno in self.__alunos_DAO.get_all():
            for mensalidade in aluno.mensalidades:
                pago = "Não"
                if mensalidade.pago:
                    pago = "Sim"
                mensalidades.append("CPF: " + str(aluno.cpf) + '  -  ' +
                                    "Nome: " + str(aluno.nome) + '  -  ' +
                                    "Valor: " + str(mensalidade.valor) + '  -  ' +
                                    "Vencimento: " + str(mensalidade.vencimento) + '  -  ' +
                                    "Descricao: " + str(mensalidade.descricao) + '  -  ' +
                                    "Pago: " + pago + '  -  '
                                    )

        button, values = self.__tela_mensalidades.open(mensalidades)
        options = {4: self.voltar, 9: self.abre_tela_cadastro_mensalidade}

        return options[button]()

    def abre_tela_cadastro_mensalidade(self, mensalidade=None):
        button, values = self.__tela_cadastro.open(mensalidade)

        options = {'voltar': self.voltar_lista(),
                   'salvar': self.pre_cadastro_mensalidade}

        values = {
            "cpf": values[0],
            "descricao": values[1],
            "mes_vencimento": values[2],
            "ano_vencimento": values[3],
        }

        if button != 'voltar':
            return options[button](values)
        else:
            return options[button]()

    def valida_data_vencimento(self, data_nasc):
        try:
            [dia, mes, ano] = data_nasc.split('/')
            if (1 <= int(dia) <= 31) and (1 <= int(mes) <= 12) and (1900 <= int(ano) < 2021):
                return True
            else:
                raise Exception
        except Exception as err:
            raise Exception('Data de nascimento inválida')

    def valida_mensalidade(self, values):
        self.valida_data_vencimento(values['vencimento'])

    def pre_cadastro_mensalidade(self, values):
        try:
            self.valida_mensalidade(values)

            cpf = values['cpf']
            aluno = self.__alunos_DAO.getByCpf(cpf)

            if not aluno:
                self.__tela_cadastro.show_message("Aluno não encontrado",
                                                  "Não foi encontrado um aluno com o CPF informado")
                self.__tela_cadastro.close()
                self.abre_tela_cadastro_mensalidade(list(values.values()))

            self.cadastrar_mensalidade(values['descricao'], False, aluno['valor_mensalidade'], values['vencimento'],
                                       aluno)
            self.voltar()

        except Exception as e:
            self.__tela_cadastro.show_message("Erro", e)
            self.__tela_cadastro.close()
            self.abre_tela_cadastro_mensalidade(list(values.values()))

    def cadastrar_mensalidade(self, descricao, pago, valor, vencimento, aluno):
        mensalidade = Mensalidade(descricao, pago, valor, vencimento)

        self.__alunos_DAO.remove(aluno['codigo'])
        aluno['mensalidades'].append(mensalidade)
        self.__alunos_DAO.add(aluno['codigo'], aluno)
        self.__tela_cadastro.show_message("Sucesso", "Mensalidade cadastrada com sucesso")

    def listar_alunos_inadimplentes(self):
        todos_os_alunos = self.__alunos_DAO.get_all()
        alunos_inadimplentes = []
        for aluno in todos_os_alunos:
            if aluno.tem_mensalidade_atrasada():
                alunos_inadimplentes.append("Nome: " + str(aluno.nome) + '  -  ' +
                                            "Email: " + str(aluno.email) + '  -  ' +
                                            "cpf: " + str(aluno.cpf))

        button, values = self.__tela_alunos_inadimpletes.open(alunos_inadimplentes)
        options = {4: self.voltar}

        return options[button]()

    @property
    def alunos(self):
        return self.__alunos

    def voltar(self):
        self.__tela_mensalidades.close()
        self.__controlador_principal.abre_tela_inicial()

    def voltar_lista(self):
        self.__tela_cadastro.close()
        self.abre_tela_inicial()
