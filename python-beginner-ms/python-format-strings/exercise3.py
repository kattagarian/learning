'''
#step 2
medicine = 'Coughussin'
dosage = 5
duration = 4.5
instructions = '{} - Take {} ML by mouth every {} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{2} - Take {1} ML by mouth every {0} hours'.format(medicine, dosage, duration)
print(instructions)

instructions = '{medicine} - Take {dosage} ML by mouth every {duration} hours'.format(medicine = 'Sneerzergen', dosage = 10, duration = 6)

print(instructions)

#step 3
#Com o f-string, podemos pular passos desnecessários que usamos no .format()
name = 'World'
message = f'Hello, {name}'
print(message)

count = 10
value = 3.14
message = f'Count to {count}. Multiply by {value}.'
print(message)

#step 4
width = 5
height = 10

print(f'The perimeter is {(2 * width) + (2 * height)} and the area is {width*height}.')
'''
#step 5
value = 'hi'

print(f'.{value:<25}.')
print(f'.{value:>25}.')
print(f'.{value:^25}.')
print(f'.{value:-^25}.')
