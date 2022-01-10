import random

roll = 0
count = 0

print('First person to roll a 5 wins!')

while roll != 5:

    name = input('Enter a name, or \'q\' to quit: ' )
    if name.strip() == '':
        continue #skip to top

    if name.strip() == 'q':
        break #ends the loop

    count = count + 1
    roll = random.randint(1, 5)
    print(f'{name} rolled {roll}')
else: #runs when while is false
        print(f'{name} Wins!!!')

print(f'You rolled the dice {count} times.')