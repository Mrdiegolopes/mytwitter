# Importa a classe base Perfil do módulo mytwitter
from .mytwitter import Perfil

class PessoaFisica(Perfil):
    """
    Classe que representa um perfil de pessoa física no sistema.
    Herda todas as funcionalidades da classe Perfil e adiciona
    características específicas de uma pessoa física, como CPF.
    
    Attributes:
        __cpf (str): CPF da pessoa física (privado)
        Além dos atributos herdados da classe Perfil:
        - __usuario (str): nome do usuário
        - __seguidores (list): lista de perfis que seguem este usuário
        - __seguidos (list): lista de perfis que este usuário segue
        - __tweets (list): lista de tweets do usuário
        - __ativo (bool): estado do perfil
    """
    def __init__(self, usuario, cpf):
        """
        Inicializa um novo perfil de pessoa física.
        
        Args:
            usuario (str): Nome do usuário do perfil (deve começar com @)
            cpf (str): CPF da pessoa física (apenas números)
            
        Note:
            O construtor da classe pai (Perfil) é chamado para inicializar
            os atributos básicos do perfil
        """
        super().__init__(usuario)
        self.__cpf = cpf
    
    def get_cpf(self):
        """
        Recupera o CPF da pessoa física.
        
        Returns:
            str: CPF da pessoa física
            
        Note:
            O CPF é um atributo privado, então este método
            é a única forma de acessá-lo externamente
        """
        return self.__cpf

class PessoaJuridica(Perfil):
    """
    Classe que representa um perfil de pessoa jurídica no sistema.
    Herda todas as funcionalidades da classe Perfil e adiciona
    características específicas de uma pessoa jurídica, como CNPJ.
    
    Attributes:
        __cnpj (str): CNPJ da pessoa jurídica (privado)
        Além dos atributos herdados da classe Perfil:
        - __usuario (str): nome do usuário
        - __seguidores (list): lista de perfis que seguem este usuário
        - __seguidos (list): lista de perfis que este usuário segue
        - __tweets (list): lista de tweets do usuário
        - __ativo (bool): estado do perfil
    """
    def __init__(self, usuario, cnpj):
        """
        Inicializa um novo perfil de pessoa jurídica.
        
        Args:
            usuario (str): Nome do usuário do perfil (deve começar com @)
            cnpj (str): CNPJ da pessoa jurídica (apenas números)
            
        Note:
            O construtor da classe pai (Perfil) é chamado para inicializar
            os atributos básicos do perfil
        """
        super().__init__(usuario)
        self.__cnpj = cnpj
    
    def get_cnpj(self):
        """
        Recupera o CNPJ da pessoa jurídica.
        
        Returns:
            str: CNPJ da pessoa jurídica
            
        Note:
            O CNPJ é um atributo privado, então este método
            é a única forma de acessá-lo externamente
        """
        return self.__cnpj