import matplotlib.pyplot as plt
x_values = list(range(1, 1000))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
            edgecolors='none', s=40)
#Define o intervalo para cada eixo
#A função axis() exige quatro valores: os valores mínimo e máximo para
# o eixo x e para o eixo y
plt.axis([0, 1100, 0, 1100000])
plt.show()
#plt.savefig('squares_plot.png', bbox_inches='tight')


