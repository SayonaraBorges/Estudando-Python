# Começa com os usuários que precisam ser verificados, 
unconfirmed_users = ['alice', 'brian', 'candace']
# e com uma lista vazia para armazenar os usuários confirmados
confirmed_users = []

# Verifica cada usuário até que não haja mais usuários não confirmados 
while unconfirmed_users:
# Transfere cada usuário verificado para a lista de usuários confirmados 
    current_user = unconfirmed_users.pop() 
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    # Exibe todos os usuários confirmados
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())