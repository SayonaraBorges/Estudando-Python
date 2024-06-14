import random

class DadoSeisLados:
    def __init__(self):
        self.lados = 6
        
    def rolar(self):
        """Rola o dado entre 1 a 6."""
        return random.randint(1, self.lados)