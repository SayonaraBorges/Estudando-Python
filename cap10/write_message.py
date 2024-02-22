filepath = "text_files/programming.txt"

#with open(filepath, 'w') as file_object: 
#    file_object.write("I love programming.\n")
#    file_object.write("I love creating new games.\n")

#O primeiro argumento ainda é o nome do arquivo que queremos abrir. O segundo argumento, 'w', diz a Python que queremos abrir o arquivo em modo de escrita. Podemos abrir um arquivo em modo de leitura ('r'), em modo de escrita ('w'), em modo de concatenação ('a') ou em um modo que permita ler e escrever no arquivo ('r+').
    
with open(filepath, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")