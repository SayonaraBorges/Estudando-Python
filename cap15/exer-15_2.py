import matplotlib.pyplot as plt

x_values = list(range(1, 50))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, 
            edgecolors='none', s=40)
plt.title('Exercício 2 Cap15', fontsize=12)
plt.xlabel('X')
plt.ylabel('Y')
plt.tick_params(axis='both', labelsize=15)

plt.show()
