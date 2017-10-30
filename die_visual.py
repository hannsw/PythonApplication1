from die import Die
import pygal

#create a D6
die = Die()

#roll dices and store results
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#analyse the results
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#visualise results
hist = pygal.Bar()

hist.title = "Results of rolling"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

