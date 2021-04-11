from Telas.TelaAlunosInadimplentes import TelaAlunosInadimplentes
from Entidades.Aluno import Aluno
from Entidades.Gerente import Gerente
from Entidades.src.AlunoDAO import AlunoDAO

class ControladorGerente:
    __instance = None

    def __init__(self, controlador_principal):
        self.__tela_alunos_inadimpletes = TelaAlunosInadimplentes(self)
        self.__alunos_DAO = AlunoDAO()
        self.__controlador_principal = controlador_principal


    @property
    def alunos_DAO(self):
        return self.__alunos_DAO

    def abre_tela(self):
        self.listar_alunos_inadimplentes()

    def listar_alunos_inadimplentes(self):
        todos_os_alunos = self.__alunos_DAO.get_all()
        alunos_lista = []
        for aluno in todos_os_alunos:
            if aluno.tem_mensalidade_atrasada:
                __alunos_inadimplentes.append(aluno)
                alunos.append("CPF: " + str(aluno.data_nasc) + '  -  ' +
                          "Email: " + str(aluno.email) + '  -  ' +
                          "Nome: " + str(aluno.nome))

        button, values = self.__tela_alunos_inadimpletes.open(alunos)
        options = {4: self.voltar} 

        return options[button]()

    @property
    def alunos_inadimplentes(self):
        return self.__alunos_inadimplentes

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()