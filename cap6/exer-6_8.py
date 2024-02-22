elvis = {
    'tipo': 'amfíbio',
    'dono': 'sabrina',
    'é': 'gagado',
    'nome': 'elvis',
}
zeh = {
    'tipo': 'mamífero',
    'dono': 'mônica',
    'é': 'cachorro',
    'nome': 'zeh',
}
chico = {
    'tipo': 'aquático',
    'dono': 'alex',
    'é': 'peixe',
    'nome': 'chico',
}

pets = [ ]

pets.append(elvis)
pets.append(zeh)
pets.append(chico)

for pet in pets:
   dono = pet.get('dono')
   nome = pet.get('nome')
   tipo = pet.get('tipo')
   especie = pet.get('é')
   print(f"O animal de estimação de {dono.title()} é um {especie} {tipo}, seu nome é {nome.title()}.")
