gato_0 = {
    'cor': 'preto',
    'tamanho': 'pequeno',
}
gato_1 = {
    'cor': 'mesclado cinza',
    'tamanho': 'médio',
}
gato_2 = {
    'cor': 'mesclado laranja',
    'tamanho': 'grande',
}

gatos = [gato_0, gato_1, gato_2]

for gato in gatos:
    print(gato)

for numero_gato in range(30):
    novo_gato = {
        'cor': 'mesclado 3 cores',
        'tamanho': 'médio'
    }
    gatos.append(novo_gato)

for gato in gatos[:5]:
    print(gato)
    print('...')

print('Foram criados um total de ' +
    str(len(gatos)) +
    '.')
# range() funciona como variável contatdor para criar cópidas de dicionários
# usar as fatias para modificação agrupada e em massa




    
