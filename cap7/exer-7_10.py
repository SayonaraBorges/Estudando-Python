respostas = { }

continuar = 'sim'
while continuar == 'sim':
    name = input("Qual seu nome? ")
    place = input("Se pudesse visitar um lugar do mundo, para onde você iria? ")
    respostas[name] = place

    continuar = input("Digite 'sim' para continuar a pesquisa ou 'parar' para sair. ")

for name, place in respostas.items():
    print(f"Para {name.title()} visitar {place.title()} é seu maior sonho. " )

