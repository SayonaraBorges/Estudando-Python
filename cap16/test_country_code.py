import unittest
from country_codes import get_country_code

class TestCountryCodeCase(unittest.TestCase):
    def test_country_code(self):
        """Testa se o código devolve duas letras para um país, dado o seu nome. """
        country_code = get_country_code('Canada')
        self.assertEqual(country_code, 'CA')

unittest.main()