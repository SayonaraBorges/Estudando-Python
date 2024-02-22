alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print(alien_0)
print('Original x-position: ' + str(alien_0['x_position']))
if alien_0['speed'] == 'slow': 
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: ' + str(alien_0['x_position']))


pessoa_1 = {}
pessoa_1['altura'] = 175
pessoa_1['nome'] = 'Sayonara'
pessoa_1['origem'] = 'Brasileira'
pessoa_1['idade'] = 32

print(pessoa_1)

pessoa_1['idade'] = 33
del pessoa_1['origem']

print(pessoa_1)
