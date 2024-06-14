import csv
arquivo = 'h:\Meu Drive\python_work\Estudando-Python\cap16\csvfiles\sitka_weather_07-2014.csv'
with open(arquivo) as a:
    reader = csv.reader(a)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index, column_header)
