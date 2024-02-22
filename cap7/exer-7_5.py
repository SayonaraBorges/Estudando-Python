while True:
    resposta = input("Digite a sua idade (ou 's' para sair): ")

    if resposta.lower() == 's':
        print("Encerrando programa...")
        break

    resposta = int(resposta)

    if resposta < 3:
        preco = 0
    elif 3 <= resposta <= 12:
        preco = 10
    else:
        preco = 15

    print(f"Seu ingresso custará ${preco} dólares! ")
    

