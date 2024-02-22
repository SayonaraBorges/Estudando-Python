filename='text_files/respostas.txt'

while True:
    resposta = input('Responda: por que você gosta de programação? (Ou digite "sair") ')
    if resposta == 'sair':
        print('Você saiu.')
        break
    else:
        with open(filename, 'a') as file_object:
                file_object.write(resposta + "\n")

with open(filename) as file_object:
    respostas = file_object.readlines()