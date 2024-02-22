carros = ['bmw', 'audi', 'toyota', 'subaru']
print(carros)

carros.sort()
print(carros)

carros.sort(reverse=True)
#reserve=True, exibe uma lista em ordem alfabética inversa
print(carros)

print('\n\tHere is the original list: ') 
print(carros)
print('\n\tHere is the sorted list: ')
print(sorted(carros))
print('\n\tHere is the original list again: ')
print(carros)

carros.reverse()
print(carros)
#reverse() : ordena a lista de tras pra frente
carros.reverse()
print(carros)
#reverse() : usado novamente, retorna a lista a forma origial, de frente pra trás

contador = len(carros)
print(contador)
