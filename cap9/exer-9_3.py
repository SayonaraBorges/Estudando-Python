class User():
    def __init__(self, first_name, last_name, age, nacionality) -> None:
        """Inicializa os atributos do usuário."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nacionality = nacionality
        pass


    def describe_user(self):
        """Exibe a descrição das informações do usuário."""
        print(f"\nDescrição do usuário: {self.first_name.title()} {self.last_name.title()}, é {self.nacionality} e tem {str(self.age)} anos de idade.")
    

    def greet_user(self):
        """Exibe uma saudação personalizada ao usuário."""
        print(f"Usuário {self.first_name.title()}, seja bem vindo ao nosso site!")


user001 = User('sayonara', 'borges', 32, 'brasileira')
user001.describe_user()
user001.greet_user()

user002 = User('alexandre', 'silva', 45, 'alemão')
user002.describe_user()
user002.greet_user()

user003 = User('testando', 'classes', 90, 'estadunidense')
user003.describe_user()
user003.greet_user()

