favorite_places = {
    'luana' : ['Ponta Negra', 'Praia de Miami', 'Ponte Newton Navarro'],
    'pirscilla' : ['Praia dos Artistas', 'Praia do Forte', 'Via Costeira'],
    'cynthia': ['Pinheiros', 'Forte dos Reis Magos', 'Bosque dos Namorados']
}

for people in favorite_places:
    print("\nApresento --> " + people.title())
    print('Ela já visitou: ')
    for places in favorite_places[people]:
        print('\t #' + places)