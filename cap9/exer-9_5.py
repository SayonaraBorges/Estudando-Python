class User():
    def __init__(self, first_name, last_name, age, nacionality) -> None:
        """Inicializa os atributos do usuário."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.nacionality = nacionality
        self.login_attempts = 0
        pass


    def describe_user(self):
        """Exibe a descrição das informações do usuário."""
        print(f"\nDescrição do usuário: {self.first_name.title()} {self.last_name.title()}, é {self.nacionality} e tem {str(self.age)} anos de idade.")
    

    def greet_user(self):
        """Exibe uma saudação personalizada ao usuário."""
        print(f"Usuário {self.first_name.title()}, seja bem vindo ao nosso site!")

    def increment_login_attempts(self, info):
        """Incrementa o valor de tentativas de login."""
        self.login_attempts += 1
        print(info)
    
    
    def reset_login_attempts(self):
        """Reseta o valor da variável 'login_attempts'."""
        self.login_attempts = 0


user001 = User('sayonara', 'borges', 32, 'brasileira')
user001.describe_user()
user001.greet_user()
user001.increment_login_attempts('Tentativa 1')
user001.increment_login_attempts('Tentativa 2')
user001.increment_login_attempts('Tentativa 3')
user001.increment_login_attempts('Tentativa 4')
user001.increment_login_attempts('Tentativa 5')
user001.increment_login_attempts('Tentativa 6')
user001.increment_login_attempts('Tentativa 7')
user001.increment_login_attempts('Tentativa 8')
user001.increment_login_attempts('Tentativa 9')
print(f"Quantidade de tentativas de login: {str(user001.login_attempts)}")
user001.reset_login_attempts()
print(f"Quantidade de tentativas de login: {str(user001.login_attempts)}")