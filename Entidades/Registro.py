from enum import Enum


class EventoRegistro(Enum):
    ACESSO_PERMITIDO = 1
    ACESSO_NEGADO = 2
    ACESSO_BLOQUEADO = 3
    VEICULO_DEVOLVIDO = 4
    VEICULO_EMPRESTADO = 5


class Registro:
    def __init__(self, data, matricula_funcionario, motivo, placa_veiculo, evento: EventoRegistro):
        self.__data = data
        self.__matricula_funcionario = matricula_funcionario
        self.__motivo = motivo
        self.__placa_veiculo = placa_veiculo
        self.__evento = evento
