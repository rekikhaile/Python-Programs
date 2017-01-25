import math
import random

def number_guessing():
    user_input = input("Please enter 2 values for range:\n")

    parts = user_input.split(',')

    if len(parts) != 2:
        print("Please enter a,b where a is the inclusive lower limit and b the exclusive upper limit")
        return

    lower_limit = int(parts[0])
    upper_limit = int(parts[1])

    maximum_tries = math.ceil(math.log2(upper_limit - lower_limit))

    picked_number = random.randint(lower_limit, upper_limit - 1)

    tries_left = maximum_tries

    print("I have picked a number between " + str(lower_limit) + " and " + str(upper_limit) + ", what's your guess?")
    print("You have " + str(maximum_tries) + " left.")

    while tries_left > 0:
        user_input = input("")

        player_guess = int(user_input)

        tries_left -= 1

        if player_guess < picked_number:
            print("This number is lower than the number I have in mind! Next try?")
            print("You have " + str(tries_left) + " left.")
        elif player_guess > picked_number:
            print("This number is higher than the number I have in mind! Another guess?")
            print("You have " + str(tries_left) + " left.")
        else:
            print("Thaat's right! That was my number!")
            break

def number_guessing_game():
    number_guessing()

    user_input = input("Play again? y/n")

    while user_input == 'y':
        number_guessing()

        user_input = input("Play again? y/n")
