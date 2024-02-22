filepath = "text_files/aprendendo_python.txt"

with open(filepath) as file_object:
    lines = file_object.readlines()
    text_string = ''

    for line in lines:
        maiscula = line.replace('python', 'Python')
        text_string += maiscula.replace('Python', 'C#')
        
print(text_string)