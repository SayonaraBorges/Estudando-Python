import pygal
import matplotlib.pyplot as plt
from dadoSeisLados import DadoSeisLados
from random_walk import RandomWalk

#matplotlib
resultadosmultip = []
resultadossomados = []

for i in range(10):
    dado1 = DadoSeisLados()
    dado2 = DadoSeisLados()
    resultadossomados.append(dado1.rolar() + dado2.rolar())

plt.plot(resultadossomados, linewidth=5)
plt.title("Soma do lancamento de 2 dados", fontsize=24)
plt.tick_params(axis='both', labelsize=14)
plt.show()

#pygal
rw = RandomWalk()
rw.fill_walk()
line_chart = pygal.Line()
line_chart.title='Random Walk usando Paygal'
line_chart.add('Valores X', rw.x_values)
line_chart.add('Valores Y', rw.y_values)
line_chart.render_in_browser()





