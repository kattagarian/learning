import random

randnum = random.randint(1, 5)
guess = 0
count = 0
while randnum != guess:
    count += 1
    guess = int(input('Guess a number between 1 and 5:'))
else:
    print(f'You guessed it in {count} times')
