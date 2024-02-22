convidados = ['jeffeson', 'andré', 'adriana']
message = 'Oi '+ convidados[0].title()+', vamos sair para jantar?'
print(message)
message1 = 'Oi '+ convidados[1].title()+', vamos sair para jantar?'
print(message1)
message2 = 'Oi '+ convidados[2].title()+', vamos sair para jantar?'
print(message2)

nao_vem = convidados.pop(0)
print('Informou que não poderá comparecer: '+nao_vem.title())
convidados.append('Monnyssy')

message = 'Oi '+ convidados[0].title()+', vamos sair para jantar?'
print(message)
message1 = 'Oi '+ convidados[1].title()+', vamos sair para jantar?'
print(message1)
message2 = 'Oi '+ convidados[2].title()+', vamos sair para jantar?'
print(message2)

convidados.insert(0,'tatinha')
convidados.insert(3,'samara')
convidados.insert(5,'tayane')
print('Oi '+ convidados[0].title()+', '+convidados[3].title()+' e '+convidados[-1].title()+', venham jantar comigo também!')

print(convidados)
