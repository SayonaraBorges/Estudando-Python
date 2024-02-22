def make_album(artista, titulo):
    albuns = {'Artista': artista.title(), 'Título': titulo.title()}
    return albuns

# Lista para armazenar os registros de álbuns
registros = []

while True:
    artista = input("Digite o nome do artista: ")
    titulo = input("Digite o título do álbum: ")
    registro = make_album(artista, titulo)
    registros.append(registro)

    continuar = input('Deseja continuar? Digite "s" para continuar ou "n" para sair: ')
    if continuar.lower() == 'n':
        break

# Imprimir todos os dicionários
for album in registros:
    print(album)
