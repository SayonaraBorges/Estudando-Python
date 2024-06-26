import json
import pygal

arquivo = r"H:\Meu Drive\python_work\Estudando-Python\cap16\csvfiles\maiores_economias_2023.json"
with open(arquivo) as a:
    datajson = json.load(a)
    paises, pibs = [], []

    for info in datajson:
        pais = info['pais']
        paises.append(pais)
        pib = int(info['pib'])
        pibs.append(pib)

bar_chart = pygal.Bar()
bar_chart.title = 'Maiores economias do mundo em 2023\n(valores em trilhoes)'

for pais, pib in zip(paises, pibs):
    bar_chart.add(pais, pib)

bar_chart.render_in_browser()


