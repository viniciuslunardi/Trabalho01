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
        for placa in self.__alunos_DAO.get_all():
            alunos.append("Placa: " + placa.placa + '  -  ' +
                            "Marca: " + placa.marca + '  -  ' +
                            "Modelo: " + placa.modelo + '  -  ' +
                            "Ano: " + placa.ano + '  -  ' +
                            "KM Atual: " + str(placa.quilometragem_atual))

        button, values = self.__tela_aluno.open(alunos)
        options = {4: self.voltar,
                   1: self.cadastra,
                   2: self.alterar_carro,
                   3: self.deletar_carro}

        return options[button]()

    def cadastra(self):
        button, values = self.__tela_cadastro.open()
        try:
            placa = values[0]
            modelo = values[1]
            marca = values[2]
            ano = values[3]
            km = float(values[4])
            if km:
                self.cadastrar_aluno(placa, modelo, marca, ano, km)
            else:
                raise ValueError
        except ValueError:
            print("Quilometragem atual deve ser informada em números "
                  " (utilize '.' para números não inteiros)")
            self.__tela_cadastro.show_message("Erro",
                                              "Quilometragem atual deve ser informada em números "
                                              " (utilize '.' para números não inteiros)")
        self.abre_aluno()

    def cadastrar_aluno(self, placa, modelo, marca, ano, quilometragem_atual, msg=None):
        try:
            aluno = Aluno(placa, modelo, marca, ano, quilometragem_atual)
            if self.__alunos_DAO.get(placa):
                raise AlunoJahExisteException
            else:
                self.__alunos_DAO.add(placa, aluno)
                if not msg:
                    self.__tela_cadastro.show_message("Sucesso",
                                                    "Veículo cadastrado com sucesso")
                return True
        except Exception:
            print("---------------ATENÇÃO--------------- \n * Veículo já cadastrado *")
            self.__tela_cadastro.show_message("Erro",
                                              "Já existe um veículo com placa " + placa + " cadastrado")
            return False

    def existe_aluno(self, placa):
        return placa in self.__alunos

    def lista_aluno(self):
        if len(self.__alunos) > 0:
            for placa in self.__alunos:
                return self.__alunos[placa]
        else:
            print("Nenhum veículo cadastrado")

    def mostrar_alunos(self):
        print("MODELO: PLACA: ")
        for placa in self.__alunos:
            print("%s: %s:", self.__alunos[placa].modelo, self.__alunos[placa].placa)

    @property
    def alunos(self):
        return self.__alunos

    def atualiza_quilometragem(self, placa, km_andado):
        km_atual = float(self.__alunos_DAO.get(placa).quilometragem_atual)
        float(km_atual)
        km_atual += km_andado
        self.__alunos_DAO.get(placa).quilometragem_atual = km_atual

    def deletar_carro(self):
        placa = self.__tela_aluno.ask_verification("Digite o valor da placa do carro que será deletado", "Placa")
        if self.__alunos_DAO.get(placa):
            self.__alunos_DAO.remove(placa)
            print("Veículo excluido com sucesso")
            self.__tela_aluno.show_message("Sucesso",
                                             "Veículo deletado com sucesso")
        else:
            print("Não existe veículo com essa placa cadastrado no sistema")
            self.__tela_aluno.show_message("Erro",
                                             "Erro ao deletar veículo")
        self.abre_aluno()

    def alterar_carro(self):
        placa_anterior = self.__tela_aluno.ask_verification("Digite o valor da placa do carro que será alterado",
                                                              "Placa")

        if self.__alunos_DAO.get(placa_anterior):
            button, new_values = self.__tela_cadastro.open(self.__alunos_DAO.get(placa_anterior))
            try:
                placa = new_values[0]
                modelo = new_values[1]
                marca = new_values[2]
                ano = new_values[3]
                km = float(new_values[4])
                if km:
                    msg = "Altera"
                    self.__alunos_DAO.remove(placa_anterior)
                    self.cadastrar_aluno(placa, modelo, marca, ano, km, msg)
                    print("Veículo alterado com sucesso")
                    self.__tela_cadastro.show_message("Sucesso",
                                                      "Veículo alterado com sucesso")

                else:
                    raise ValueError
            except ValueError:
                print("Quilometragem atual deve ser informada em números "
                      " (utilize '.' para números não inteiros)")
                self.__tela_cadastro.show_message("Erro",
                                                  "Quilometragem atual deve ser informada em números "
                                                  " (utilize '.' para números não inteiros)")
        else:
            if placa_anterior:
                self.__tela_aluno.show_message("Erro", "Não existe veículo com placa " + placa_anterior +
                                                " na garagem")
        self.abre_aluno()

    def voltar(self):
        self.__controlador_principal.abre_tela_inicial()
