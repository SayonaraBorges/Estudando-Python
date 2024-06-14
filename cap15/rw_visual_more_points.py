import matplotlib.pyplot as plt
from random_walk import RandomWalk
rw = RandomWalk(50000)
rw.fill_walk()
# Define o tamanho da janela de plotagem 
plt.figure(figsize=(10, 6))

# Oculta os eixos
plt.axis('off')

# Oculta os eixos, mas mantém a moldura
#plt.box(False)

# Plota os pontos e mostra o gráfico
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=2) 
# Enfatiza o primeiro e o último ponto 
plt.scatter(0, 0, c='green', edgecolors='none', s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

plt.show()    