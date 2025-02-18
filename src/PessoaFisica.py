class PessoaFisica(perfil):
    def __init__(self, nomeUsuario, cpf):
        super().__init__(nomeUsuario)
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf