players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
print(players[:2])
print(players[2:])

print(players[-3:]) 
#Esse código exibe os nomes dos três últimos jogadores e continuaria a funcionar à medida que a lista de jogadores mudar de tamanho. 

print("Here are the first three players on my team: ")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are: ')
print(my_foods)
print("\nMy friend's favorite foods are: ")
print(friend_foods)
