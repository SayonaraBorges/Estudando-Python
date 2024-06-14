import random
class DadoOitoLados:
    """Dado de 8 lados."""
    def __init__(self):
        self.lados = 8
    def rolar(self):
        """Rola o dado entre 1 a 8."""
        return random.randint(1, self.lados)

