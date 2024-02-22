concursos = ['cnu', 'caixa', 'bnb', 'bacen', 'imd', 'fiocruz', 'mpo']
print(concursos[4].title())
print(concursos[-1].title())
concursos[1] = 'caixa econômica'
print('Escolhi estudar para o concurso da ' + concursos[1].title() +'.')
concursos.append('finep')
print(concursos)
concursos.insert(5,'emprel')
print(concursos)
del concursos[0]
print(concursos)
popped_concurso = concursos.pop()
print('Excluído: '+ popped_concurso)
concursos.remove('bnb')
print(concursos)
concursos.sort()
concursos.sort(reverse=True)
sorted(concursos)
concursos.reverse()
total = len(concursos)
print(total)

print(concursos)



