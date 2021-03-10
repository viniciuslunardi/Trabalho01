class Usuario:
    def __init__(self, cpf, data_nasc, email, matricula, nome, senha, conta):
        self.__nome = nome
        self.__email = email
        self.__data_nasc = data_nasc
        self.__senha = senha
        self.__cpf = cpf
        self.__matricula = matricula
        self.__conta = None


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nasc(self):
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, data_nasc):
        self.__data_nasc = data_nasc

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def __eq__(self, other):
        return self.matricula == other.matricula
