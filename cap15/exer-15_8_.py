#GERADO PELO COPILOT
import random
import pygal

class DadoSeisLados:
    def __init__(self):
        self.lados = 6

    def rolar(self):
        return random.randint(1, self.lados)

# Lançar três dados D6
resultados = []
for _ in range(3):
    dado = DadoSeisLados()
    resultados.append(dado.rolar())

# Calcular a soma dos resultados
soma_resultados = sum(resultados)

# Criar um gráfico de pizza com os resultados
pie_chart = pygal.Pie()
for i in range(1, 7):
    count = resultados.count(i)
    pie_chart.add(f"Face {i}", count)

# Exibir o gráfico
pie_chart.title = "Resultados do lancamento de 3 dados D6"
pie_chart.render_in_browser()
