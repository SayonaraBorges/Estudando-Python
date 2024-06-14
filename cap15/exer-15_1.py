import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]
plt.plot(x_values, y_values, marker='o', label='Primeiros 5')

x_values_large = list(range(1, 5001))
y_values_large = [x**3 for x in x_values_large]
plt.plot(x_values_large, y_values_large, linestyle='--', color='gray', label='Primeiros 5000')

plt.title('Exercício Cap15', fontsize=12)
plt.xlabel('Valores')
plt.ylabel('Valores ao Cubo')
plt.tick_params(axis='both', labelsize=15)
plt.legend()
plt.show()



