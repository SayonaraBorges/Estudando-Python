motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)
motorcycles[0]= 'ducati'
print(motorcycles)

motorcycles.append('honda')
print (motorcycles)

motorcycles.insert(0,'cinquentinha')
motorcycles.insert(2, 'pop100')
print(motorcycles)

del motorcycles[2]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print('popada: '+popped_motorcycles)

print(motorcycles)
last_owned = motorcycles.pop(0)
print('The last motorcycle I owned was a ' + last_owned.title() +'.')

motorcycles.remove('ducati')
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA '+ too_expensive.title()+' is too expensive for me.')



