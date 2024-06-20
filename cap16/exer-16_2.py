import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Função para ler os dados do arquivo
def ler_dados(arquivo):
    with open(arquivo) as a:
        leitor = csv.reader(a)
        leitor_linha = next(leitor)
        datas, altas, baixas = [], [], []

        for linha in leitor:
            try:
                data_atual = datetime.strptime(linha[0], "%Y-%m-%d")
                alta = int(linha[1])
                baixa = int(linha[3])
            except ValueError:
                print(data_atual, 'Dados nao encontrados.')
            else:
                datas.append(data_atual)
                altas.append(alta)
                baixas.append(baixa)
    return datas, altas, baixas

# Caminhos dos arquivos
arquivo_dv = r"H:\\Meu Drive\\python_work\\Estudando-Python\\cap16\\csvfiles\\death_valley_2014.csv"
arquivo_sitka = r"H:\\Meu Drive\\python_work\\Estudando-Python\\cap16\\csvfiles\\sitka_weather_2014.csv"

# Ler os dados de cada arquivo
datas_dv, altas_dv, baixas_dv = ler_dados(arquivo_dv)
datas_sitka, altas_sitka, baixas_sitka = ler_dados(arquivo_sitka)

# Configuração da figura do gráfico
figura = plt.figure(dpi=128, figsize=(10,6))

# Plot Death Valley
plt.plot(datas_dv, altas_dv, c='red', alpha=0.5)
plt.plot(datas_dv, baixas_dv, c='blue', alpha=0.5)
plt.fill_between(datas_dv, altas_dv, baixas_dv, facecolor='blue', alpha=0.1)

# Plot Sitka
plt.plot(datas_sitka, altas_sitka, c='green', alpha=0.5)
plt.plot(datas_sitka, baixas_sitka, c='orange', alpha=0.5)
plt.fill_between(datas_sitka, altas_sitka, baixas_sitka, facecolor='orange', alpha=0.1)

# Formatação do gráfico
plt.title('Comparativo das temperaturas min/max diárias - 2014\nDeath Valley e Sitka', fontsize=18)
plt.xlabel('', fontsize=16)
figura.autofmt_xdate()
plt.ylabel('Temperatura (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# Exibir o gráfico
plt.show()


