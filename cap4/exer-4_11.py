pizzas = ['portuguesa', 'camarão', 'nordestina', 'frango']
friend_pizzas = pizzas[:]
friend_pizzas.append('calabresa')
pizzas.append('italiana')

print('Minhas pizzas favoritas são: ')
for piz in pizzas:
    print(piz.title())

print('As pizzas favoritas do meu amigo são: ')
for pizz in friend_pizzas:
    print(pizz.title())

