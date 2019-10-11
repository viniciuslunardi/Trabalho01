from Telas.TelaArmario import TelaArmario
from Entidades.Armario import Armario
from Controladores.ControladorVeiculo import ControladorVeiculo
from Controladores.ControladorFuncionario import ControladorFuncionario


class ControladorArmario:
    def __init__(self, controlador_principal):
        self.__tela_armario = TelaArmario(self)
        self.__chaves = {}
        self.__chaves_emprestadas = {}
        self.__chaves_disponiveis = []
        self.__controlador_principal = controlador_principal

    def abre_armario(self):
        self.abre_tela_inicial()

    def abre_tela_inicial(self):
        switcher = {1: self.veiculos_na_garagem, 2: self.pegar_veiculo}
        while True:
            opcao = self.__tela_armario.mostrar_opcoes()
            funcao_escolhida = switcher[opcao]
            funcao_escolhida()

    def lista__chaves(self):
        for chave in self.__chaves:
            print("CHAVE", chave.chave)

    def veiculos_na_garagem(self):
        veiculos = self.__controlador_principal.controlador_veiculo.veiculos
        print("--------------GARAGEM--------------")

        for veiculo in veiculos:
            if veiculo not in self.__chaves_emprestadas:
                print("MODELO: %s PLACA: %s" % (veiculos[veiculo].modelo, veiculos[veiculo].placa))

    def pegar_veiculo(self):
        self.veiculos_na_garagem()
        tentativas = 0
        while tentativas < 3:
            matricula = input("Digite o seu número de matrícula: ")
            if not self.__controlador_principal.controlador_funcionario.existe_funcionario(matricula):
                # EMITIR REGISTRO ACESSO NEGADO
                tentativas += 1
                print("Não existe funcionário com matrícula '" + str(matricula) + "' cadastrado no sistema")
            else:
                funcionario = self.__controlador_principal.controlador_funcionario.funcionarios
                veiculos_garagem = self.__controlador_principal.controlador_veiculo.veiculos
                veiculos_funcionario = funcionario[matricula].veiculos
                if len(veiculos_garagem) > 1:
                    if len(veiculos_funcionario) > 1:
                        placa = input("Digite a placa do veículo que deseja utilizar: ")
                        chave = veiculos_funcionario[placa].chave
                        if placa not in veiculos_garagem:
                            tentativas += 1
                            # EMITIR REGISTRO ACESSO NEGADO
                            print("Não existe veículo com placa '" + str(placa) + "' na garagem")
                        elif placa not in veiculos_funcionario:
                            # EMITIR REGISTRO ACESSO NEGADO
                            tentativas += 1
                            print("Funcionário não tem acesso a este veiculo")
                        elif placa not in self.__chaves_emprestadas[chave]:
                            # EIMITIR REGISTRO ACESSO PERMITIDO
                            self.__chaves_emprestadas[chave] = veiculos_funcionario[placa]
                            print("Pode pegar a chave %s do veículo %s"
                                  % (veiculos_garagem[placa].chave, veiculos_garagem[placa].modelo))
                            return
                        else:
                            # EMITIR REGISTRO ACESSO NEGADO
                            print("Esse veículo não está disponível no momento")
                    elif len(funcionario) == 1:
                        # EMITIR REGISTRO ACESSO PERMITIDO
                        print("Retire seu veiculo")
                    else:
                        print("Funcionário não tem acesso  nenhum carro")
                else:
                    print("Não existe nenhum veículo na garagem")
        if tentativas == 3:
            # EMITIR EVENTO ACESSO BLOQUEADO
            print("Acesso bloqueado")

def devolver_chave(self):
    pass


@property
def chaves(self):
    return self.__chaves


@property
def chaves_emprestadas(self):
    return self.__chaves_emprestadas


@property
def chaves_disponiveis(self):
    return self.__chaves_disponiveis


def voltar(self):
    self.__controlador_principal.abre_tela_inicial()
