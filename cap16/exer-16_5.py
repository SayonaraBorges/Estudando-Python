import json
import pygal
from datetime import datetime

arquivo = r"H:\Meu Drive\python_work\Estudando-Python\cap16\csvfiles\cartoes_ativos_bc.json"
with open(arquivo) as a:
    datajson = json.load(a)

    datas, quantidades = [], []

    for info in datajson:
        data_atual = datetime.strptime(info['data'], "%d/%m/%Y")
        datas.append(data_atual)
        qtd = int(info['valor'])
        quantidades.append(qtd)

pie_chart = pygal.Pie(half_pie=True)
pie_chart.title = 'Quantidade de cartoes de credito ativos por ano\n Dados: Banco Central'

# Adicionando as fatias com rótulos de ano
for data, qtd in zip(datas, quantidades):
    ano = data.year
    pie_chart.add(str(ano), qtd)
    
pie_chart.render_in_browser()