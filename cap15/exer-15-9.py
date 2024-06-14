import pygal
from dadoSeisLados import DadoSeisLados

resultadosmultip = []
resultadossomados = []

for jogo in range(10):
    dado1 = DadoSeisLados()
    dado2 = DadoSeisLados()
    resultadosmultip.append(dado1.rolar() * dado2.rolar())
    resultadossomados.append(dado1.rolar() + dado2.rolar())

bar_chart = pygal.HorizontalBar()
bar_chart.title = '10 Lancamentos de dois dados com 6 lados'
bar_chart.add('Somados', resultadossomados)
bar_chart.add('Multiplicados',resultadosmultip)
bar_chart.render_in_browser()

