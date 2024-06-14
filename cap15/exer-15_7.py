from dadoOitoLados import DadoOitoLados
d8_1 = DadoOitoLados()
d8_2 = DadoOitoLados()
lancamentos = []
lancamentos2 = []
for jogada in range(10):
    resultado1 = d8_1.rolar()
    resultado2 = d8_2.rolar()
    jogo = resultado1 + resultado2
    lancamentos.append(jogo)
    lancamentos2.append((resultado1, resultado2))

print(lancamentos)
print(lancamentos2)
