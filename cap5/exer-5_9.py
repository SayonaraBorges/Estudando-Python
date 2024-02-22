current_users = ['Alexandre', 'Samara', 'Natã', 'Sabrina', 'Sandra', 'Júnior']
new_users = ['alexandre', 'Samara', 'Maria', 'Luana', 'João', 'Wagner']

for user in new_users:
    if user.lower() in [u.lower() for u in current_users]:
        print('O nome de ususário ' + user + ' já está em uso. Por favor escolha outro nome.')
    else:
        print('O nome de usuário ' + user + ' está disponível.')
