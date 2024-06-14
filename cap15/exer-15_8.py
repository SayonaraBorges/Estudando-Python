import pygal
from dadoSeisLados import DadoSeisLados

d3_1 = DadoSeisLados()
d3_2 = DadoSeisLados()
d3_3 = DadoSeisLados()

resultado1 = d3_1.rolar()
resultado2 = d3_2.rolar()
resultado3 = d3_3.rolar()

pie_chart = pygal.Pie(inner_radius=.4)
pie_chart._title = 'Exercício 15-8'
pie_chart.add('Dado 1', resultado1)
pie_chart.add('Dado 2', resultado2)
pie_chart.add('Dado 3', resultado3)
pie_chart.render_to_file('pie_chart_exer15_8.svg')
