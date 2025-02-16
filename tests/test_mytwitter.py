import unittest
from src.mytwitter import MyTwitter
from src.usuarios import PessoaFisica, PessoaJuridica
from src.excecoes import PIException, PDException, UJCException

class TestMyTwitter(unittest.TestCase):
    def setUp(self):
        # metodo executado antes de cada teste
        self.twitter = MyTwitter()
        self.usuario1 = PessoaFisica("@usuario1", "12345678900")
        self.usuario2 = PessoaJuridica("@empresa1", "12345678000199")
        self.twitter.criar_perfil(self.usuario1)
        self.twitter.criar_perfil(self.usuario2)

    def test_criar_usuario(self):
        #testando a criação de um usuario.
        self.assertEqual(self.usuario1.get_usuario(), "@usuario1")
        self.assertEqual(self.usuario2.get_cnpj(), "12345678000199")

    def test_cadastrar_usuario_existente(self):
        #testando a tentativa de cadastrar um usuario ja existente.
        with self.assertRaises(UJCException):
            self.twitter.criar_perfil(PessoaFisica("@usuario1", "11111111111"))

    def test_tweetar_e_timeline(self):
        ## Testa a criação de tweets e a recuperação da timeline.
        self.twitter.tweetar("@usuario1", "Meu primeiro tweet!")
        self.twitter.tweetar("@usuario1", "Segundo tweet!")
        tweets = self.usuario1.get_tweets()
        self.assertEqual(len(tweets), 2)
        self.assertEqual(tweets[0].get_mensagem(), "Meu primeiro tweet!")
        self.assertEqual(tweets[1].get_mensagem(), "Segundo tweet!")

    def test_cancelar_perfil(self):
        # Testa o cancelamento de um perfil e a tentativa de tweetar após o cancelamento.
        self.twitter.cancelar_perfil("@usuario1")
        with self.assertRaises(PDException):
            self.twitter.tweetar("@usuario1", "Teste de tweet bloqueado!")

    def test_perfil_inexistente(self):
        # Testa a tentativa de recuperar a timeline de um perfil inexistente.
        with self.assertRaises(PIException):
            self.twitter.timeline("@usuarioInexistente")

if __name__ == '__main__':
    unittest.main()
