import unittest
from exer_11_1 import formata_nome_cidade_pais

class CidadesTestCase(unittest.TestCase):
    def test_formata_nome_cidade_pais(self):
        """Testa a função formata nome cidade e país."""
        f_cidade = formata_nome_cidade_pais('natal', 'brasil')
        self.assertEqual(f_cidade, 'Natal, Brasil')

    def test_formata_nome_cidade_pais(self):
        """Testa a função formata nome cidade e país + população."""
        f_cidade = formata_nome_cidade_pais('natal', 'brasil', '180.000')
        self.assertEqual(f_cidade, 'Natal, Brasil - população: 180.000')

unittest.main()