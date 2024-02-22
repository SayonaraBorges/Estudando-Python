favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
} 

entrevistados = { 
    'alexandre': 'kotlin',
    'jen': 'python', 
    'sayon': 'java',
    'sarah': 'c', 
    'edward': 'ruby', 
    'alinne': 'c#',
    'phil': 'python', 
    'pedro': 'android',
}

for entrevistado in entrevistados.keys():
    if entrevistado in favorite_languages.keys():
        print(entrevistado.title() +
            ', obrigada por sua participação!\n')
    else:
        print('\t' + entrevistado.title() +
            ', participe da nossa pesquisa sobre linguagens de programação.')