from random import randint

class Die():
    """Classe criada para o exercício 9_14"""
    def __init__(self, sides) -> None:
        self.sides = sides
        pass


    def roll_die(self):
        """Exibe um número aleatório de 1-x."""
        x = randint(1, self.sides)
        print(x)


