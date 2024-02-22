filename = 'text_files/guest_book.txt'

active = True
while active:
    user_name = input("Informe seu nome:  (Ou digite 'sair' para finalizar o programa.)  ")
    if user_name == 'sair':
        print('Programa encerrado.')
        active = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(user_name + "\n")

with open(filename) as file_object:
    guests = file_object.readlines()
    for guest in guests:
        print(f"Olá {guest.rstrip()}, seja bem-vindo!")