import perfil

class UJCExpetion(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class UNCExpetion(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class RepositorioUsuarios():
    def __init__(self):
        self.__perfis = []

    def cadastrar(self, usuario):
        if self.buscar(usuario) is not None:
            raise UJCExpetion(f"Usuario {perfil.usuario} já está cadastrado!")
        self.__perfis.append(usuario)
         
    def buscar(self, name):
        for usuario in self.__perfis:
            if perfil.usuario == name:
                return usuario
        return None
    
    def atualizar(self, usuario):
        for i, u in enumerate(self.__perfis):
            if u.usuario == perfil.usuario:
                self.__perfis[i] == usuario
                return
        raise UNCExpetion(f"Usuario {perfil.usuario} não está cadastrado")