favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
} 

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'], 
}
for name, languages in fav_languages.items():
    if len(languages) <= 1:
        print("\n" + name.title() +
        "'s favorite language is: ")
    else:
        print("\n" + name.title() +
        "'s favorite languages are: ")
    for language in languages:
        print('\t' +
        language.title())


    