def describe_city(city, country='Brasil'):
    """Devolve uma frase completa formatada de modo elegante."""
    print(f"{city.title()} está localizada no {country.title()}. ")

describe_city('Natal')
describe_city('João Pessoa')
describe_city('Tokyo', 'Japão')

def get_formatted_name(first_name, last_name):
    """Devolve um nome completo formatado de modo elegante."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') 
print(musician)