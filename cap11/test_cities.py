import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    def test_city_country(self):
        """Testes para Cidade, País funcionam?"""
        f_city = city_country('santiago', 'chile')
        self.assertEqual(f_city, 'Santiago, Chile')
    
    def test_city_country_population(self):
        """Testes para Cidade, País - população:xxx funcionam?"""
        f_city = city_country('santiago', 'chile', '500mil')
        self.assertEqual(f_city, 'Santiago, Chile - população: 500mil')

unittest.main()