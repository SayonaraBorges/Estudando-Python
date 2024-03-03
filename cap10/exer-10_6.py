try:
    first_number = int(input("Informe o primeiro número: "))
    second_number = int(input("Informe o segundo número: "))
except ValueError:
    print('Para realizar uma soma, é necessário que seja informado um número. ')
else:
    soma = first_number + second_number
    print(f"A soma do número {first_number} + {second_number} é = {soma}")