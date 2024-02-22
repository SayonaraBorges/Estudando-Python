prompt = "Vamos fazer pizza! Entre com cada ingrediente: "
prompt += "\nCaso deseja sair digite 'sair'. "
ingrediente = input(prompt)
ingredientes = [ ]
proximo = "\nCaso deseja sair digite 'sair'. "
proximo += 'Insira o próximo ingrediente: '

active = True
while active:
    if ingrediente == 'sair':
        sair = input("Você realmente deseja sair? Digite 's' para confirmar: ")
        if sair == 's':
            print("Você concluiu sua pizza!")
            print(f"Na sua pizza tem: ")
            for ingrediente in ingredientes:
                print("--> " + ingrediente.title())
            active = False
    else:
        ingredientes.append(ingrediente)
        print(f"O igrediente {ingrediente.upper()} foi adicionado a sua pizza.")
        ingrediente = input(proximo)
