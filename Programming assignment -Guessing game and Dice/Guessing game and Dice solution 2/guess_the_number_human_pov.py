import random, math

## Iterative implementation of the Guess The Number game(human POV)


def guess_the_number_iterative(a, b):
    attempts = math.ceil(math.log(b-a, 2))
    secret_number = random.randrange(a, b)
    messages = ['Another guess?', 'Next try?', 'Next guess?']
    print('I have picked a number between {} and {}.'.format(a, b))
        
    for i in range(attempts):
        print('You have {} attempt(s) left.'.format(attempts - i))
        guess = input('What"s your guess?\n')
        while not guess.isdigit():
            guess = input('Please enter a valid integer.\n')

        guess = int(guess)
        if guess == secret_number:
            print('Thaat"s right, that was my number!')
            return
        if i < attempts - 1:
            if guess > secret_number:
                msg = 'Your number is higher than my number. '
            else:
                msg = 'Your number is lower than my number. '

            print(msg + random.choice(messages))

    print('Game over, you"re out of attempts.')


## Wrapper function for the game


def guess_the_number_wrapper(game_function):
    print('Welcome to the Guess the number game!')
    print('Please enter 2 numbers separated by a space and I"m gonna think of a number in-between.')
    a, b = map(int, input().split())

    assert(a < b), 'Invalid range.'
    assert(a >= 0 and b > 0), 'Only positive integers or 0 allowed.'

    game_function(a, b)
    play_again = input('Would you like to play again? y/n\n')
    while play_again not in 'y n'.split():
        print('Invalid choice, enter y for yes or n for no.')
        play_again = input('Would you like to play again? y/n\n')
    
    if play_again == 'y':
        guess_the_number_wrapper(game_function)
    elif play_again == 'n':
        return


## Uncomment next line to play the game using iterative function
guess_the_number_wrapper(guess_the_number_iterative)