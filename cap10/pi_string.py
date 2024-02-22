filename = 'text_files/pi_thousand_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''

    for line in lines:
        pi_string += line.strip()

birthday = input("Enter your bitchday, in the form mmddyy: ")
if birthday in pi_string: 
    print("Your birthday appears in the first thousand digits of pi! ")
else:
    print("Your birthday dos not appear in the first thousand digits os pi.")

print(pi_string[:52] + "...")
print(len(pi_string))
