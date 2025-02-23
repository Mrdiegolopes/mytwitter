# Exceções personalizadas para tratamento de erros específicos do sistema
class PIException(Exception):  # Exceção para Perfil Inexistente
    pass

class PDException(Exception):  # Exceção para Perfil Desativado
    pass

class PEException(Exception):  # Exceção para Perfil já Existente
    pass

class MFPException(Exception):  # Exceção para Mensagem Fora do Padrão
    pass

class SIException(Exception):  # Exceção para Seguidor Inválido
    pass

class MyTwitter:
    """
    Classe principal que gerencia todas as operações do sistema MyTwitter.
    Responsável por criar perfis, gerenciar tweets e relacionamentos entre usuários.
    """
    def __init__(self):
        """Inicializa o sistema com um repositório de usuários vazio"""
        self.__repositorio = RepositorioUsuarios()
    
    def criar_perfil(self, perfil):
        """
        Cadastra um novo perfil no sistema
        Args:
            perfil: Objeto da classe Perfil a ser cadastrado
        Raises:
            PEException: Se já existir um perfil com o mesmo nome de usuário
        """
        if self.__repositorio.buscar(perfil.get_usuario()) is not None:
            raise PEException("Perfil já existe")
        self.__repositorio.cadastrar(perfil)
    
    def cancelar_perfil(self, usuario):
        """
        Desativa um perfil existente
        Args:
            usuario: Nome do usuário a ser desativado
        Raises:
            PIException: Se o perfil não existir
            PDException: Se o perfil já estiver desativado
        """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil já está desativado")
        perfil.set_ativo(False)
    
    def tweetar(self, usuario, mensagem):
        """
        Cria um novo tweet para um usuário
        Args:
            usuario: Nome do usuário que está tweetando
            mensagem: Conteúdo do tweet
        Raises:
            MFPException: Se a mensagem não estiver entre 1 e 140 caracteres
            PIException: Se o perfil não existir
            PDException: Se o perfil estiver desativado
        """
        if len(mensagem) < 1 or len(mensagem) > 140:
            raise MFPException("Mensagem deve ter entre 1 e 140 caracteres")
        
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
            
        tweet = Tweet(usuario, mensagem)
        perfil.adicionar_tweet(tweet)
    
    def timeline(self, usuario):
        """
        Recupera a timeline de um usuário (tweets próprios e dos seguidos)
        Args:
            usuario: Nome do usuário
        Returns:
            Lista de tweets ordenados do mais recente ao mais antigo
        Raises:
            PIException: Se o perfil não existir
            PDException: Se o perfil estiver desativado
        """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
        return perfil.get_timeline()
    
    def tweets(self, usuario):
        """
        Recupera todos os tweets de um usuário específico
        Args:
            usuario: Nome do usuário
        Returns:
            Lista com todos os tweets do usuário
        Raises:
            PIException: Se o perfil não existir
            PDException: Se o perfil estiver desativado
        """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
        return perfil.get_tweets()
    
    def seguir(self, seguidor, seguido):
        """
        Estabelece uma relação de seguidor entre dois usuários
        Args:
            seguidor: Nome do usuário que vai seguir
            seguido: Nome do usuário a ser seguido
        Raises:
            SIException: Se tentar seguir a si mesmo
            PIException: Se algum dos perfis não existir
            PDException: Se algum dos perfis estiver desativado
        """
        if seguidor == seguido:
            raise SIException("Usuário não pode seguir a si mesmo")
            
        perfil_seguidor = self.__repositorio.buscar(seguidor)
        perfil_seguido = self.__repositorio.buscar(seguido)
        
        if perfil_seguidor is None or perfil_seguido is None:
            raise PIException("Perfil inexistente")
        if not perfil_seguidor.is_ativo() or not perfil_seguido.is_ativo():
            raise PDException("Perfil está desativado")
            
        perfil_seguidor.seguir(perfil_seguido)
        perfil_seguido.adicionar_seguidor(perfil_seguidor)
    
    def numero_seguidores(self, usuario):
        """
        Retorna o número de seguidores ativos de um usuário
        Args:
            usuario: Nome do usuário
        Returns:
            Número de seguidores ativos
        Raises:
            PIException: Se o perfil não existir
            PDException: Se o perfil estiver desativado
        """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
            
        seguidores_ativos = [s for s in perfil.get_seguidores() if s.is_ativo()]
        return len(seguidores_ativos)
    
    def seguidores(self, usuario):
        """
        Retorna a lista de seguidores ativos de um usuário
        Args:
            usuario: Nome do usuário
        Returns:
            Lista de perfis dos seguidores ativos
        Raises:
            PIException: Se o perfil não existir
            PDException: Se o perfil estiver desativado
        """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
            
        return [s for s in perfil.get_seguidores() if s.is_ativo()]
    
    def seguidos(self, usuario):
        """
        Retorna a lista de usuários ativos que são seguidos por um usuário
        Args:
            usuario: Nome do usuário
        Returns:
            Lista de perfis seguidos que estão ativos
        Raises:
            PIException: Se o perfil não existir
            PDException: Se o perfil estiver desativado
        """
        perfil = self.__repositorio.buscar(usuario)
        if perfil is None:
            raise PIException("Perfil inexistente")
        if not perfil.is_ativo():
            raise PDException("Perfil está desativado")
            
        return [s for s in perfil.get_seguidos() if s.is_ativo()]

class Tweet:
    """
    Classe que representa um tweet no sistema
    Armazena o usuário que criou o tweet e seu conteúdo
    """
    def __init__(self, usuario, mensagem):
        """
        Inicializa um novo tweet
        Args:
            usuario: Nome do usuário que criou o tweet
            mensagem: Conteúdo do tweet
        """
        self.__usuario = usuario
        self.__mensagem = mensagem
    
    def get_usuario(self):
        """Retorna o nome do usuário que criou o tweet"""
        return self.__usuario
    
    def get_mensagem(self):
        """Retorna o conteúdo do tweet"""
        return self.__mensagem

class Perfil:
    """
    Classe que representa um perfil de usuário no sistema
    Gerencia informações como tweets, seguidores e seguidos
    """
    def __init__(self, usuario):
        """
        Inicializa um novo perfil
        Args:
            usuario: Nome do usuário do perfil
        """
        self.__usuario = usuario
        self.__seguidores = []  # Lista de perfis que seguem este usuário
        self.__seguidos = []    # Lista de perfis que este usuário segue
        self.__tweets = []      # Lista de tweets deste usuário
        self.__ativo = True     # Estado do perfil (ativo/inativo)
    
    def get_usuario(self):
        """Retorna o nome do usuário"""
        return self.__usuario
    
    def is_ativo(self):
        """Retorna se o perfil está ativo"""
        return self.__ativo
    
    def set_ativo(self, ativo):
        """Define o estado do perfil (ativo/inativo)"""
        self.__ativo = ativo
    
    def adicionar_seguidor(self, seguidor):
        """
        Adiciona um novo seguidor ao perfil
        Args:
            seguidor: Perfil que irá seguir este usuário
        """
        if seguidor not in self.__seguidores:
            self.__seguidores.append(seguidor)
    
    def seguir(self, seguido):
        """
        Adiciona um novo perfil à lista de seguidos
        Args:
            seguido: Perfil que será seguido por este usuário
        """
        if seguido not in self.__seguidos:
            self.__seguidos.append(seguido)
    
    def adicionar_tweet(self, tweet):
        """
        Adiciona um novo tweet à lista de tweets do usuário
        Args:
            tweet: Objeto Tweet a ser adicionado
        """
        self.__tweets.append(tweet)
    
    def get_tweets(self):
        """Retorna uma cópia da lista de tweets do usuário"""
        return self.__tweets.copy()
    
    def get_timeline(self):
        """
        Retorna a timeline do usuário (tweets próprios e dos seguidos)
        Returns:
            Lista de tweets ordenados do mais recente ao mais antigo
        """
        timeline = []
        # Adiciona tweets próprios
        timeline.extend(self.__tweets)
        
        # Adiciona tweets dos perfis seguidos
        for seguido in self.__seguidos:
            if seguido.is_ativo():
                timeline.extend(seguido.get_tweets())
        
        # Ordena a timeline do tweet mais recente para o mais antigo
        timeline.sort(key=lambda x: timeline.index(x), reverse=True)
        return timeline
    
    def get_seguidores(self):
        """Retorna uma cópia da lista de seguidores"""
        return self.__seguidores.copy()
    
    def get_seguidos(self):
        """Retorna uma cópia da lista de seguidos"""
        return self.__seguidos.copy()

class RepositorioUsuarios:
    """
    Classe responsável por armazenar e gerenciar todos os perfis do sistema
    Utiliza um dicionário para mapear nomes de usuários para seus respectivos perfis
    """
    def __init__(self):
        """Inicializa o repositório com um dicionário vazio"""
        self.__perfis = {}
    
    def cadastrar(self, perfil):
        """
        Cadastra um novo perfil no repositório
        Args:
            perfil: Objeto Perfil a ser cadastrado
        """
        self.__perfis[perfil.get_usuario()] = perfil
    
    def buscar(self, usuario):
        """
        Busca um perfil pelo nome de usuário
        Args:
            usuario: Nome do usuário a ser buscado
        Returns:
            Objeto Perfil se encontrado, None caso contrário
        """
        return self.__perfis.get(usuario)
