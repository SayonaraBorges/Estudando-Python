def make_album(artista, titulo, faixas='', ano=''):
    album = {'Artista': artista.title(), 'Título': titulo.title()}
    if ano:
        album['Ano'] = ano
    if faixas:
        album['Faixas'] = faixas
    return album
   
    
registro1 = make_album('marcos almeida', 'casa', 12, 2020)
print(registro1)

registro2 = make_album('gabriella rocha', 'leve', faixas= 9)
print(registro2)

registro3 = make_album('kim sola', "it's sola bebê", ano= 2021)
print(registro3)