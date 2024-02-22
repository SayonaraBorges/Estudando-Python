conhecido_1 = {
    'primeiro_nome': 'Sandra',
    'idade': 55,
    'profissão': 'professora',
    'comida_favorita': 'doces',
    'esporte': 'caminhada',
    'cidade': 'Natal/RN',
    'ultimo_nome': 'Borges',
    'sexo': 'F',
}
conhecido_2 = {
    'primeiro_nome': 'Alice',
    'idade': 7,
    'profissão': 'estudante',
    'comida_favorita': 'pizza',
    'esporte': 'ginástica',
    'cidade': 'Natal/RN',
    'ultimo_nome':'Sucar',
    'sexo': 'F',
}
conhecido_3 = {
    'primeiro_nome': 'Bibiane',
    'idade': 57,
    'profissão': 'dona de casa',
    'comida_favorita': 'lasanha',
    'esporte': 'nenhum',
    'cidade': 'Recife/PE',
    'ultimo_nome':'Borges',
    'sexo': 'F',
}

people = [ ]
people.append(conhecido_1)
people.append(conhecido_2)
people.append(conhecido_3)

for info in people:
    full_name = info['primeiro_nome'] + " " + info['ultimo_nome']
    print("\nA " + info['profissão']+ " de " +
    "nome " + full_name.title() + ", " +
    "reside em " + info['cidade'] +
    " e gosta de " + info['comida_favorita'] + ".")
    if info['sexo'] == 'F':
        print('Ela tem ' + str(info['idade']) + ' anos de idade.')    
    else:
        print('Ele tem ' + str(info['idade']) + ' anos de idade.')    
        
