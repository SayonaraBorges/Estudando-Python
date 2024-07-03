import requests
import matplotlib.pyplot as plt

# Faz a chamada à API para Python
url_python = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response_python = requests.get(url_python)
data_python = response_python.json()
repos_python = data_python['items']

# Faz a chamada à API para Java
url_java = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
response_java = requests.get(url_java)
data_java = response_java.json()
repos_java = data_java['items']

# Obtém os dados relevantes (apenas o primeiro lugar)
repo_name_python = repos_python[0]['name']
stars_python = repos_python[0]['stargazers_count']

repo_name_java = repos_java[0]['name']
stars_java = repos_java[0]['stargazers_count']

# Cria o gráfico
plt.figure(figsize=(8, 6))
plt.bar(['Python', 'Java'], [stars_python, stars_java], color=['b', 'r'], alpha=0.7)
plt.xlabel('Linguagem')
plt.ylabel('Estrelas')
plt.title('Projeto com Mais Estrelas no GitHub (Python vs Java)')
plt.tight_layout()
plt.show()
