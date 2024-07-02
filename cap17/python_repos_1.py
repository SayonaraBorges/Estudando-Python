import requests 

# Faz uma chamada de API e armazena a resposta 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url) 
print("Status code:", r.status_code) 

# Armazena a resposta da API em uma variável 
response_dict = r.json()
print("Total repositories:", response_dict['total_count']) 

# Explora informações sobre os repositórios
repo_dicts = response_dict['items'] 
print("Repositories returned:", len(repo_dicts)) 

# Analisa o primeiro repositório
repo_dict = repo_dicts[0]
print("\nKeys:", len(repo_dict))

for key in sorted(repo_dict.keys()): 
    print(key) 