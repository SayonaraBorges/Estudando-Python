def formata_nome_cidade_pais(cidade, pais, populacao=''):
    """Devolve o nome da cidade e seu respectivo país de forma elegante."""
    if populacao:
        cidadepais = cidade.title() + ", " + pais.title() + ' - população: ' + populacao
    else:
        cidadepais = cidade.title() + ", " + pais.title()
    return cidadepais

