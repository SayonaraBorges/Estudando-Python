def greet_users(names):
    """Exibe uma saudação simples a cada usuário da lista."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot', 'sayonara']
greet_users(usernames)

