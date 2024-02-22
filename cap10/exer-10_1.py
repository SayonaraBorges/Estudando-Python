filepath = "text_files/aprendendo_python.txt"

with open(filepath) as file_object:
    contents = file_object.read()
    print(contents)

with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filepath) as file_object:
    lines = file_object.readlines()
    text_string = ''

    for line in lines:
        text_string += line.strip()

print(">>" + text_string[:55])