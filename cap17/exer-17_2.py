import requests
from operator import itemgetter
import pygal

# Faz uma chamada de API e armazena a resposta
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Processa informações sobre cada artigo submetido
# convertemos o texto da resposta em uma lista Python
submission_ids = r.json()
submission_dicts = [] 

for submission_id in submission_ids[:30]: 
    # Cria uma chamada de API separada para cada artigo submetido
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json') 
    submission_r = requests.get(url) 
    response_dict = submission_r.json()
    submission_dict = {'title': response_dict['title'],
                        'link': 'http://news.ycombinator.com/item?id='+ str(submission_id),
                        'comments': response_dict.get('descendants', 0)} 
    submission_dicts.append(submission_dict)
    # itemgetter: ordenar a lista de dicionários de acordo com o número de comentários.
    submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Cria o gráfico com Pygal
bar_chart = pygal.Bar()
bar_chart.title = 'Discussões Mais Enthusiastas no Hacker News'
for submission_dict in submission_dicts: 
    bar_chart.add(submission_dict['title'], 
                  submission_dict['comments'], 
                  href=submission_dict['link'])     

bar_chart.render_in_browser()