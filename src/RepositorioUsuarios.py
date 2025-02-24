from .perfil import *

class UJCExpetion(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class UNCExpetion(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class RepositorioUsuarios():
    def __init__(self):
        self.__usuarios = {}

    def cadastrar(self, usuario):
        if self.buscar(usuario.get_usuario()) is not None:  # Corrigido aqui
            raise UJCExpetion(f"Usuario {usuario.get_usuario()} já está cadastrado!")  # Corrigido aqui
        self.__usuarios[usuario.get_usuario()] = usuario
         
    def buscar(self, usuario):
        return self.__usuarios.get(usuario)
    
    def atualizar(self, usuario):
        for i, u in enumerate(self.__perfis):
            if u.usuario == usuario.usuario:  # Corrigido aqui
                self.__perfis[i] = usuario  # Corrigido aqui (substituição correta com =)
                return
        raise UNCExpetion(f"Usuario {usuario.usuario} não está cadastrado")  # Corrigido aqui
