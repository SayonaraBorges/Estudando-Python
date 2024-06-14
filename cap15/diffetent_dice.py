import pygal
from die import Die
#Cria um D6 e um D10
die_1 = Die()
die_2 = Die(10)
#Faz lançamentos e armazena os resultados em uma lista
results = []
for roll_num in range(500):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    #Analisa os resultados
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequency = results.count(value)
        frequencies.append(frequency)
    #Visualiza os resultados
    hist = pygal.Bar()
    hist.title = 'Results of rolling a D6 and D10 50.000 times.'
    #hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '12', '13','14', '15', '16']
    hist.x_labels = [str(x) for x in range(1, 17)]
    hist.x_title = 'Result'
    hist.y_title = 'Frequency od Result'
    hist.add('D6 + D10', frequencies)
    hist.render_to_file('dice_visual_d6d10.svg')
    

