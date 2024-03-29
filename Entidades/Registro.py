from enum import Enum


class EventoRegistro(Enum):
    ACESSO_PERMITIDO = 1
    ACESSO_NEGADO = 2
    ACESSO_BLOQUEADO = 3
    VEICULO_DEVOLVIDO = 4


class Registro:
    def __init__(self, data, matricula_funcionario, motivo, placa_veiculo, evento: EventoRegistro):
        self.__data = data
        self.__matricula_funcionario = matricula_funcionario
        self.__motivo = motivo
        self.__placa_veiculo = placa_veiculo
        self.__evento = evento

    def __str__(self):
        evento = self.__evento
        if evento == evento.ACESSO_PERMITIDO:
            evento = "ACESSO PERMITIDO"
        elif evento == evento.ACESSO_NEGADO:
            evento = "ACESSO NEGADO"
        elif evento == evento.ACESSO_BLOQUEADO:
            evento = "ACESSO BLOQUEADO"
        elif evento == evento.VEICULO_DEVOLVIDO:
            evento = "VEICULO DEVOLVIDO"

        matricula = "NÃO EXISTE"
        if self.__matricula_funcionario is not None:
            matricula = str(self.__matricula_funcionario)

        placa = "NÃO EXISTE"
        if self.__placa_veiculo is not None:
            placa = str(self.__placa_veiculo)
        s = "-------------REGISTRO-------------"
        s += "\nEVENTO: " + evento
        s += "\nDATA: " + str(self.__data)
        s += "\nMOTIVO: " + str(self.__motivo)
        s += "\nFUNCIONÁRIO COM MATRÍCULA: " + matricula
        s += "\nVEÍCULO COM PLACA: " + placa
        return s

    @property
    def matricula_funcionario(self):
        return self.__matricula_funcionario

    @property
    def placa_veiculo(self):
        return self.__placa_veiculo

    @property
    def motivo(self):
        return self.__motivo

    def __eq__(self, other):
        return self.__matricula_funcionario == other.matricula_funcionario or self.__placa_veiculo == other.placa_veiculo