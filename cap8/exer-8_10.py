def show_magicians(magicians):
    for name in magicians:
        print("Conheça o famoso mágico " + name + ".")

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = 'o Grande ' + magicians[i]


convidados = ['Mister M', 'Harry Houdini', 'Jasper Maskelyne', 'Dai Venon']

make_great(convidados)

show_magicians(convidados)

