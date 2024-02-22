def build_person(first_name, last_name, age=''):
    """Devolve um dicionário com informações sobre uma pessoa."""
    person = {'first': first_name, 'last': last_name}
    if age: 
        person['age'] = age 
        return person 
musician = build_person('jimi', 'hendrix', age=27) 
print(musician)

def criar_usuario(prim_nome, ultimo_nome, idade =" "):
    """Retorna um dicionário com as informações sobre o usuário."""
    usuario = {'primeiro_nome': prim_nome, 'ultimo_nome': ultimo_nome}
    if idade:
        usuario['idade'] = idade
        return usuario
    
dicionario = criar_usuario('Sayonara', 'Borges', 32)
print(dicionario)
