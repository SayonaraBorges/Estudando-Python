user_names = ['Alexandre', 'Samara', 'Natã', 'Sabrina', 'Sandra', 'Júnior', 'admin']
user_names.clear()
if user_names:
    for user_name in user_names:
        if user_name != 'admin':
            print('Olá ' + user_name + ', obrigada por faze login novamente!')
        else:
            print('Olá admin, gostaria de ver um relatório de status?')
else: 
    print('Precisamos encontrar alguns usuários.')
