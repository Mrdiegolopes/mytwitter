class PessoaJuridica(perfil):
    def __init__(self, nomeUsuario, cnpj):
        super()__init__(nomeUsuario)
        self.__cnpj = cnpj

    def get_cnpj(self):
        return self.__cnpj