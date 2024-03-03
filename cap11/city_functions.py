def city_country(cidade, pais, populacao=''):
    """Retorna ao usuário o nome da cidade e o país."""
    if populacao:
        cidadepais = cidade.title() + ", " + pais.title() + ' - população: ' + populacao
    else:
        cidadepais = cidade.title() + ", " + pais.title()
    return cidadepais
