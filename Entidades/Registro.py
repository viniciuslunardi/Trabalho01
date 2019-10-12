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
        s = "-------------REGISTRO-------------"
        s += "\nEVENTO: " + evento
        s += "\nDATA: " + str(self.__data)
        s += "\nMOTIVO: " + str(self.__motivo)
        return s
