import csv
from matplotlib import pyplot as plt
from datetime import datetime
# Obtém as datas e as temperaturas máximas do arquivo
filename = r"H:\\Meu Drive\python_work\Estudando-Python\cap16\csvfiles\sitka_weather_07-2014.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, highs = [], []
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
    #print(highs)

    #Faz a plotagem dos dados 
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs, c='red')
    #Formata o gráfico
    plt.title("Daily high temperatures, July 2014", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

