import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input('Guess a number between 1 to 100: '))

        if (guess < number_to_guess):
            print('Too low')
        
        elif guess > number_to_guess:
            print('Too High')
        else:
            print('Congratulations!! You have guessed the number')
        
    except ValueError: 
        print('Please enter a valid number')
