cities = {
    'Natal': ['Nordeste do Brasil', 'Cidade do Sol', 'é a capital mundial do buggy'],
    'Rio': ['Sudeste do Brasil', 'Cidade Maravilhosa', 'tem a maior floresta urbana do mundo'],
    'Porto Alegre': ['Sul do Brasil', 'Capital dos Pampas', 'foi o 1º cinema da América Latina'],
}

cities['Natal'].append('é linda')
cities['Porto Alegre'].append('faz muito frio')
cities['Rio'].pop(2)
cities['Rio'].append('tem muitas montanhas')

for city, facts in cities.items():
    print(f"Conheça {city}!")
    localizacao = facts[0]
    conhecida = facts[1]
    curiosidade = facts[2]
    print(f"Localizada no {localizacao}, conhecida como {conhecida} e tem como fato curioso: {curiosidade}.")

print(cities['Natal'])
print(cities['Porto Alegre'])
print(cities['Rio'])

