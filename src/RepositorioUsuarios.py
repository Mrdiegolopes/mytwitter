from .perfil import *
from excecoes import *

class RepositorioUsuarios():
    def __init__(self):
        self.__usuarios = []

    def cadastrar(self, usuario):
        if self.buscar(usuario.usuario) is not None:
            raise UJCException(f"Usuario {usuario.usuario} já está cadastrado!")
        self.__usuarios[usuario.usuario] = usuario
         
    def buscar(self, usuario):
        return Perfil.get_usuario(usuario)
    
    def atualizar(self, usuario):
        for i, u in enumerate(self.__usuarios):
            if u.usuario == usuario.usuario:  
                self.__perfis[i] = usuario 
                return
        raise UNCException(f"Usuario {usuario.usuario} não está cadastrado")
