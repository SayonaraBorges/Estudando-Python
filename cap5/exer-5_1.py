car = 'subaru'
print("Is car =='subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

cidade = 'Recife'
print('O melhor carnaval é o de Recife? Eu acredito que sim!')
print(cidade =='Recife')
print('\nO melhor carnaval é o de Natal? Eu acredito que não.')
print(cidade == 'Natal')

numero = 20
print('Eu aposto que o número é 20.')
print(numero == 20)
print('\nEu aposto que o número é 10.')
print(numero != 20)

user_age = 32
if user_age != 32:
    print(False)
else:
    print(True)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

requested_toppings = ['mushrooms', 'onions', 'pineaple']
if 'mushrooms' in requested_toppings:
    print(True)
else:
    print(False)

cup = 'empty'
if cup == 'full':
    print('Good morging!')
else:
    print('I need coffee rigth now!')

destino = 'Recife'
if destino == 'Recife':
    print('Folia garantida no Carnaval original!')
else:
    print('Socorro meu prefeito!')

user_name = 'Sayonara Borges'
if user_name.lower() == 'sayonara borges':
    print("That's her name.")


