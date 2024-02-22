class Restaurant():
    def __init__(self, restaurante_name, cuisine_type) -> None:
        """Inicializa os atributos nome do restaurante e tipo de cozinha."""
        self.restaurant_name = restaurante_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        pass


    def describe_restaurant(self):
        """Exibe o nome do restaurante e sua especialidade culinária."""
        print("O nome do restaurante é: " + self.restaurant_name.title() + ".")
        print("Especialidade: " + self.cuisine_type.title() + ".")


    def open_restaurant(self):
        """Informa que o restaurante está aberto."""
        print("O restaurante " + self.restaurant_name.title() + " está aberto!!")

    def people_served(self):
        """Exibe a quantidade de clientes atendidos pelo restaurante."""
        print(f"Foram atendidas {str(self.number_served)} pessoas.")

    
    def set_number_served(self, customers):
        """Permite definir o número de clientes atendindos."""
        if customers >= 1:
            self.number_served = customers
        else:
            print("O número informado deve ser maior que 1.")


    def increment_number_served(self, qtd_client):
        """Atualiza o número de clientes atendidos."""
        if qtd_client > 0:
            self.number_served += qtd_client
        else:
            print("O número informado não pode ser negativo.")
    

restautant = Restaurant("farol bar", "churrasco")
print("Nome do restaurante: " + restautant.restaurant_name.title() + ".")
print("Tipo de comida: " + restautant.cuisine_type.title())
restautant.describe_restaurant()
restautant.set_number_served(589)
restautant.people_served()
restautant.increment_number_served(129)
restautant.increment_number_served(-15)
restautant.people_served()