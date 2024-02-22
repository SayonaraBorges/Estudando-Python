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


class Admin(User):
    """Instanciando um administrador a partir da classe User."""
    def __init__(self, first_name, last_name, age, nacionality) -> None:
        super().__init__(first_name, last_name, age, nacionality)
        """Iniciando os atributos da classe-pai e em seguida inicia
        os atritbutos da classe instânciada."""
        self.privileges = Privileges()


class Privileges():
    """ """
    def __init__(self):
        """ """
        self.privileges = ['can add post', 'can delete post', 
                       'can ban user', 'can reset passaword',
                       'can alter ip config', 'can make config'] 
    
    
    def show_privileges(self):
        """Exibe uma lista dos privilégios concedidos ao Admin."""
        for privilege in self.privileges:
            print('>> ' + privilege.title())

admin = Admin('Administrador', ' ', 60, 'brasileiro')
admin.privileges.show_privileges()



