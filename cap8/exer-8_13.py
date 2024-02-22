def build_profile(first, last, **user_info):
    """Constrói um dicionário contendo tudo que sabemos sobre um usuário."""
    profile = { }
    profile['1º_nome'] = first
    profile['ultimo_nome'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('Sayonara', 'Borges', cor_do_cabelo='vermelho', altura='175', profissao='estudante', )
print(user_profile)

user_profile1 = build_profile('Sandra', 'Marilene', cor_do_cabelo='castanho', altura='165', profissao='médica', )
print(user_profile1)