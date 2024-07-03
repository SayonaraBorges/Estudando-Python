import requests 
import pygal 

# Faz a chamada à API para Python
url_python = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r_python = requests.get(url_python) 
data_python = r_python.json()
repos_python = data_python['items']

# Faz a chamada à API para Java
url_java = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
r_java = requests.get(url_java) 
data_java = r_java.json() 
repos_java = data_java['items']

# Faz a chamada à API para JavaScript
url_javascript = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
r_javascript = requests.get(url_javascript) 
data_javascript = r_javascript.json() 
repos_javascript = data_javascript['items']

# Faz a chamada à API para Ruby
url_ruby = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars'
r_ruby = requests.get(url_ruby) 
data_ruby = r_ruby.json() 
repos_ruby = data_ruby['items']

# Faz a chamada à API para C
url_c = 'https://api.github.com/search/repositories?q=language:c&sort=stars'
r_c = requests.get(url_c) 
data_c = r_c.json() 
repos_c = data_c['items']

# Faz a chamada à API para Perl
url_perl = 'https://api.github.com/search/repositories?q=language:perl&sort=stars'
r_perl = requests.get(url_perl) 
data_perl = r_perl.json() 
repos_perl = data_perl['items']

# Obtém os dados relevantes (apenas o primeiro lugar Python)
repo_name_python = repos_python[0]['name']
stars_python = repos_python[0]['stargazers_count']

# Obtém os dados relevantes (apenas o primeiro lugar Java)
repo_name_java = repos_java[0]['name']
stars_java = repos_java[0]['stargazers_count']

# Obtém os dados relevantes (apenas o primeiro lugar JavaScript)
repo_name_javascript = repos_javascript[0]['name']
stars_javascript = repos_javascript[0]['stargazers_count']

# Obtém os dados relevantes (apenas o primeiro lugar Ruby)
repo_name_ruby = repos_ruby[0]['name']
stars_ruby = repos_ruby[0]['stargazers_count']

# Obtém os dados relevantes (apenas o primeiro lugar C)
repo_name_c = repos_c[0]['name']
stars_c = repos_c[0]['stargazers_count']

# Obtém os dados relevantes (apenas o primeiro lugar Perl)
repo_name_perl = repos_perl[0]['name']
stars_perl = repos_perl[0]['stargazers_count']

# Cria o gráfico com Pygal
bar_chart = pygal.Bar()
bar_chart.title = 'Projetos com Mais Estrelas no GitHub\n Por linguagem'
bar_chart.add('Python', [stars_python])
bar_chart.add('Java', [stars_java])
bar_chart.add('JavaScript', [stars_javascript])
bar_chart.add('Ruby', [stars_ruby])
bar_chart.add('C', [stars_c])
bar_chart.add('Perl', [stars_perl])
bar_chart.render_in_browser()