message = input("Tell me something, and I will repeat it back to you: ")
print(message.upper())

name = input("Please enter your name: ")
print("Hello, " + name.title() + "!")

prompt = 'If you tell us who you are, we can pernsonalize the messages tou see.'
prompt += '\nWhat ir your first name? '

name_= input(prompt)
print("Hello, " + name_.title() + "!!!")

age = input("How old are you? ")
print(age)
print(int(age) > 21)
