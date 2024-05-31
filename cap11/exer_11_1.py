def formata_nome_cidade_pais(cidade, pais, populacao=''):
    """Devolve o nome da cidade e seu respectivo país de forma elegante."""
    if populacao:
        print(cidade.title() +', '+pais.title() + ' - população: ' + populacao)
    else:
        print(cidade.title() +', '+pais.title())

#formata_nome_cidade_pais('santiago', 'chile', '180.000')


