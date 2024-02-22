user_0 = {
    'username': 'sayonborges',
    'first': 'sayon',
    'last': 'borges', 
}

for key, value in user_0.items():
    print("\nKey: "+ key)
    print('Value: ' + value)

#items() : devolve uma lista de pares chave-valor.
print(" ")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() +
        "'s favorite language is " +
        language.title() + ".")

#for name in favorite_languages:
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " +
        name.title() +
        ", I see your favorite language is " +
        favorite_languages[name].title() +
        "!")
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")
# .keys() não serve apenas para laços
# ele devolve uma lista de todas as chaves
# sroted() cria uma copia ordenada dos elementos

print(' ')
for name in sorted(favorite_languages.keys()):
    print(name.title() + " thank you for taking the poll.")

print(' ')
print('The following languages have been mentioned: ')

# for language in set(favorite_languages.values()):
# set() identifica os itens duplicados e remove
for language in favorite_languages.values():
    print(language.title())






    