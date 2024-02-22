favorite_numbers = {
    'Carlos': [5, 8, 9],
    'Felipe': [25, 43, 90],
    'Anderson': [22, 58, 87],
    'Sandro': [13, 38, 29],
    'Berg': [3, 98, 84],
}

for people in favorite_numbers:
    print("Os números favoritos de " +
    people.title() + " são: " +
    str(favorite_numbers[people]))

for people in favorite_numbers:
    print("Os números favoritos de " +
    people.title() + " são: " )
    for n in favorite_numbers[people]:
        print(str(n))
