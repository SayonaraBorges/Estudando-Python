from collections import OrderedDict

glossario = OrderedDict()

glossario = {
    'laço': 'repetição',
    'del()': 'deletar',
    'for': 'para percorrer',
    'clear': 'limpar lista',
    'title': '1ª letra maiscula',
    'keys()': 'gera lista das chaves',
    'sorted()': 'gera uma cópia ordenada dos elementos',
    'str()': 'converte em String',
}

for key, value in glossario.items():
    print(f"{key}: {value}\n")


