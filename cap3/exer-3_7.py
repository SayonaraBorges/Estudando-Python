convidados = ['tatinha', 'andré', 'adriana', 'samara', 'Monnyssy', 'tayane']
print('Infelizmente, só poderei convidar duas pessoas.')
desconvidado = convidados.pop(0)
print('Desculpe ' + desconvidado.title()+', você não poderá mais vir para o jantar.')
desconvidado = convidados.pop(0)
print('Desculpe ' + desconvidado.title()+', você não poderá mais vir para o jantar.')
desconvidado = convidados.pop(0)
print('Desculpe ' + desconvidado.title()+', você não poderá mais vir para o jantar.')
desconvidado = convidados.pop(0)
print('Desculpe ' + desconvidado.title()+', você não poderá mais vir para o jantar.')

print('Permanecem convidados: '+convidados[0].title()+' e ' +convidados[1].title()+'.')

del convidados[1]
del convidados[0]

print(convidados)