## Recursive implementation of the Guess The Number game(computer POV)


def guess_the_number_recursive(a, b):
    if a >= b:
        print ('Some of the instructions were incorrect'
                ' or the number is not in a given range')
        return

    mid = (a + b) // 2
    answer = input('Is your number {}?\n'.format(mid))
    while answer not in 'l h c'.split():
        answer = input('Please enter a valid command: h for higher,'
            ' l for lower, c for correct\n')
    if answer == 'c':
        print('I want a cake.')
        return

    elif answer == 'l':
        return guess_the_number_recursive(a, mid)

    return guess_the_number_recursive(mid+1, b)


## Iterative implementation of the Guess The Number game(computer POV)


def guess_the_number_iterative(a, b):
    while True:
        mid = (a + b) // 2
        answer = input('Is your number {}?\n'.format(mid))
        while answer not in 'l h c'.split():
            answer = input('Please enter a valid command: h for higher,'
                ' l for lower, c for correct\n')

        if answer == 'h':
            a = mid + 1
        elif answer == 'l':
            b = mid
        elif answer == 'c':
            break
        if a >= b:
            print ('Some of the instructions were incorrect'
                    ' or the number is not in a given range')
            return 

    print('I want a cake.')


## Wrapper function for the game


def guess_the_number_wrapper(game_function):
    print('Welcome to the Guess the number game!')
    print('Please enter 2 numbers separated by a space and I"ll guess any number in-between.')
    a, b = map(int, input().split())

    assert(a < b), 'Invalid range.'
    assert(a >= 0 and b > 0), 'Only positive integers or 0 allowed.'

    print('Use h for higher, l for lower and c for correct to answer my questions.')

    game_function(a, b)
    play_again = input('Would you like to play again? y/n\n')
    while play_again not in 'y n'.split():
        print('Invalid choice, enter y for yes or n for no.')
        play_again = input('Would you like to play again? y/n\n')
    
    if play_again == 'y':
        guess_the_number_wrapper(game_function)
    elif play_again == 'n':
        return





## Uncomment next line to play the game using recursive function
# guess_the_number_wrapper(guess_the_number_recursive)


## Uncomment next line to play the game using iterative function
guess_the_number_wrapper(guess_the_number_iterative)
