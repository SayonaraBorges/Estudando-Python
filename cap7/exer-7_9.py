sandwich_orders = ['x-tudo', 'hotdog', 'bigmac', 'mclanchefeliz', 'x-tudão', 'x-calabresa']
finished_sandwhiches = []
sandwich_orders.append('pastrami')
sandwich_orders.insert(3, 'pastrami')
sandwich_orders.insert(5, 'pastrami')

print("Aviso: Excepcionalmente hoje não teremos sanduíche de PASTRAMI.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    finished_sandwhiches.append(sandwich)
    print("Estamos preparando seu pedido: " + sandwich)

print('Pedidos prontos: ')
ordem = 1
for finished in finished_sandwhiches:
    print("Pedido nº:" + str(ordem) + " - " + finished)
    ordem += 1
