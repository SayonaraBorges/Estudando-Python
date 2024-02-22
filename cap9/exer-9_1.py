class Restaurant():
    def __init__(self, restaurante_name, cuisine_type) -> None:
        """Inicializa os atributos nome do restaurante e tipo de cozinha."""
        self.restaurant_name = restaurante_name
        self.cuisine_type = cuisine_type
        pass


    def describe_restaurant(self):
        """Exibe o nome do restaurante e sua especialidade culinária."""
        print("O nome do restaurante é: " + self.restaurant_name.title() + ".")
        print("Especialidade: " + self.cuisine_type.title() + ".")


    def open_restaurant(self):
        """Informa que o restaurante está aberto."""
        print("O restaurante " + self.restaurant_name.title() + " está aberto!!")


restautant = Restaurant("farol bar", "churrasco")
print("Nome do restaurante: " + restautant.restaurant_name.title() + ".")
print("Tipo de comida: " + restautant.cuisine_type.title())
restautant.describe_restaurant()
restautant.open_restaurant()
