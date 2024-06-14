import matplotlib.pyplot as plt
from random_walk import RandomWalk
# Cria uma instância de RandomWalk
rw = RandomWalk(5000)
rw.fill_walk()
# Oculta os eixos
plt.axis('off')
# Plota o percurso com plt.plot()
plt.plot(rw.x_values, rw.y_values, linewidth=1) 
# Enfatiza o primeiro e o último ponto 
plt.scatter(0, 0, c='pink', edgecolors='none', s=50)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

# Configurações do gráfico
plt.title("Movimento molecular")
plt.xlabel("Posição X")
plt.ylabel("Posição Y")

plt.show()  