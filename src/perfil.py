class Perfil:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__seguidos = set()
        self.__seguidores = set()
        self.__tweets = []
        self.__ativo = True
        self.__lock = Lock()

    def add_seguidor(self, perfil): #Adiciona um perfil à lista de seguidores.
        self.__seguidores.add(perfil)

    def add_seguidos(self, perfil):
        self.__seguidos.add(perfil)

    def add_tweet(self, tweet):
        with self.__lock:
            self.__tweets.append(tweet)

    def get_tweets(self):
        return sorted(self.__tweets, key=lambda t: t.get_data_postagem())

    def get_tweet(self, tweet_id):
        return next((t for t in self.__tweets if t.get_id() == tweet_id), None)

    def get_timeline(self):
        timeline = self.__tweets.copy()
        for seguido in self.__seguidos:
            timeline.extend(seguido.get_tweets())
        return sorted(timeline, key=lambda t: t.get_data_postagem())

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_usuario(self):
        return self.__usuario

    def set_ativo(self, ativo):
        self.__ativo = ativo

    def is_ativo(self):
        return self.__ativo
