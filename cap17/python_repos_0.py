# Importamos o módulo requests
import requests
# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# Usamos requests para fazer a chamada get() e
# armazenamos o objeto com a resposta na variável r
r = requests.get(url)
# O bjeto com a resposta tem um atributo chamado status_code, 
# que nos informa se a requisição foi bem-sucedida
print("Status code:", r.status_code) 
# A API devolve as informações em formato JSON, portanto usamos o método json()
# para convertê-las em um dicionário Python
# Armazena a resposta da API em uma variável: response_dict
response_dict = r.json() 
# Processa o resultado 
# Por fim, exibimos as chaves de response_dict
print(response_dict.keys())