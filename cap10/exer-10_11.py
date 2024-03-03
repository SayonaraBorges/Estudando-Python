import json

def get_number():
    """Pede ao usuário um numero."""
    number = input("Qual seu numero favorito?")
    filename = 'favorite_numbers.json'
    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
        return number

def show_number():
    """Apresenta o numero favorito do usuario."""
    usernumber = get_stored_usernumber()
    if usernumber:
        print(f"Eu sei qual é seu numero favorito! É {usernumber}.")
    else:
        get_number()

def get_stored_usernumber(): 
    """Obtém o numero fornecido pelo usuário já armazenado se estiver disponível."""
    filename = 'favorite_numbers.json'
    try: 
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None 
    else: 
        return number
    
show_number()




