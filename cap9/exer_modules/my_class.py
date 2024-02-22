from user_class import User

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



