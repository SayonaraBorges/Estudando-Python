class Restaurant():
    def __init__(self, name, type) -> None:
        """Inicializa os atributos nome do restaurante e tipo de cozinha."""
        self.name = name
        self.type = type
        pass


    def describe_restaurant(self):
        """Exibe o nome do restaurante."""
        print(f"O nome do restaurante é: {self.name.title()}.")
        print(f"Especialidade: Cozinha {self.type.title()}.")
    

    def open_restaurante(self):
        """Informa que o restaurante está aberto."""
        print(f"O restaurante {self.name.title()} está aberto!")


filial_Candelária = Restaurant('la cachett - candelária', 'Piauiense')
unid_Ponta_Negra = Restaurant('la cachett - ponta negra', 'Mineira')
unid_Capim_Macio = Restaurant('la cachett - capim macio', 'Baiana')
unid_Petropolis = Restaurant('la cachett - Petrópolis', 'Gaúcha')

filial_Candelária.describe_restaurant()
unid_Ponta_Negra.describe_restaurant()
unid_Capim_Macio.describe_restaurant()
unid_Petropolis.describe_restaurant()

