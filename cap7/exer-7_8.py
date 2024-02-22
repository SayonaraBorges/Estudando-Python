sandwich_orders = ['x-tudo', 'hotdog', 'bigmac', 'mclanchefeliz', 'x-tudão', 'x-calabresa']
finished_sandwhiches = [ ]
for sandwich in sandwich_orders:
    finished_sandwhiches.append(sandwich)
    print("Preparei seu sanduíche: " + sandwich + ".")

print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
ordem = 1 
print("Preparamos todos esses sanduíches: ")
for finished in finished_sandwhiches:
    print(str(ordem) + " - " + finished)
    ordem += 1

