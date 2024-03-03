while True:
    first_number = input("Informe o primeiro número: (Ou 's' para sair) ")
    if first_number == 's': 
        break
    second_number = input("Informe o segundo número: (Ou 's' para sair) ")
    if second_number == 's': 
        break
    try:
        soma = int(first_number) + int(second_number)
    except ValueError:
        print('Para realizar uma soma, é necessário que sejam informados números. ')
    else:
        print(f"A soma do número {first_number} + {second_number} é = {soma}")