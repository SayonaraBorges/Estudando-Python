nome = input("Informe seu nome: ")

filename = 'text_files/guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(nome)
