import unittest
import python_repos_7

class ReposTestCase(unittest.TestCase):
    def test_chamada_api(self):
        """Testes para o valor de status_code é 200"""
        if python_repos_7.s_code == 200:
            print('\n --->A chamada da API esta funcionando corretamente.')
        else:
            print('\n --->Erro na chamada da API!')

unittest.main()