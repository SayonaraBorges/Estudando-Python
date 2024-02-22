def show_magicians(magicians):
    for name in magicians:
        print("Conheça o famoso mágico " + name + ".")

def make_great(magicians):
    great_magicians = magicians.copy()
    for i in range(len(great_magicians)):
        great_magicians[i] = 'o Grande ' + great_magicians[i]
    return great_magicians

convidados = ['Mister M', 'Harry Houdini', 'Jasper Maskelyne', 'Dai Venon']

# Chamando a função make_great() para criar a nova lista
convidados_grandes = make_great(convidados)

# Mostrando a lista original
print("Lista original de nomes de mágicos:")
show_magicians(convidados)

# Mostrando a lista com a expressão "o Grande"
print("\nLista com a expressão 'o Grande' adicionada:")
show_magicians(convidados_grandes)