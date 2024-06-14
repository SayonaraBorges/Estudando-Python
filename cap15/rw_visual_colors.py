import matplotlib.pyplot as plt
from random_walk import RandomWalk
# Cria um passeio aleatório e plota os pontos
rw = RandomWalk()
rw.fill_walk()
#Remove os eixos
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)
plt.axis('off')
#usamos range() para gerar uma lista de números igual ao número de pontos do passeio
# para ser usada como índice de cores.
point_numbers = list(range(rw.num_points)) 
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=15) 
# Enfatiza o primeiro e o último ponto 
plt.scatter(0, 0, c='green', edgecolors='none', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

plt.show()    