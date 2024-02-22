rios = {
    'amazonas': 'amazonense',
    'potengi': 'norte riograndense',
    'capibaribe': 'pernambucano',
}

for k, v in rios.items():
    print(f"O rio {k.title()} corta todo o estado {v.title()}.\n")

print('Os rios que estão na lista são:')
for keys in rios.keys():
    print(keys.title())

print('Os povos contemplados por esses rios são os:')
for v in rios.values():
    print(v)




