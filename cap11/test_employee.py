import unittest
from Employee import Employee

class testEmployee(unittest.TestCase):
    """Testes para classe Employee."""
    def setUp(self):
        """Cria uma instância de funcionário para realizar os testes."""
        self.empregado = Employee('Sandra', 'Borges', 60000)

    def test_give_default_raise(self):
        """Testa o aumento padrão."""
        self.empregado.give_raise()
        self.assertEqual(self.empregado.salario_anual, 65000)

    def test_give_custom_raise(self):
        """Testa o aumento personalizado."""
        self.empregado.give_raise(3000)
        self.assertEqual(self.empregado.salario_anual, 63000)

unittest.main()
    