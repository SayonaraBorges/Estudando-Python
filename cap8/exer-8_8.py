def make_album(artista, titulo):
    albuns = {'Artista': artista.title(), 'Título': titulo.title()}
    return albuns

active = True
while active:
    artista = input("Digite o nome do artista: ")   
    titulo = input("Digite o título do album: ")
    out = input('Deseja continuar? Digite "s", ou para sair digite "n" ')
    if out == 'n':
        active = False
    registro = make_album(artista, titulo)
    print(registro)
    
