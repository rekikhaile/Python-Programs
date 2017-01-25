def number_guessing():
    user_input = input("What range is your number in ?\n")

    parts = user_input.split(',')

    if len(parts) != 2:
        print("Please enter a,b where a is the inclusive lower limit and b the exclusive upper limit")
        return

    lower_limit = int(parts[0])
    upper_limit = int(parts[1])

    current_guess_lower = lower_limit
    current_guess_upper = upper_limit

    while True:
        middle_point = int((current_guess_lower + current_guess_upper) / 2)
        user_input = input("Is your number " + str(middle_point) + "?\n")
        
        if user_input == "l":
            current_guess_upper = middle_point
        elif user_input == "h":
            current_guess_lower = middle_point + 1
        elif user_input == "y":
            print("Woah, that was tricky!")
            break
        else:
            print("Please answer l for lower, h for higher or y for equal")

        if current_guess_lower > current_guess_upper:
            print("Something went wrong")
            break

def number_guessing_game():
    number_guessing()

    user_input = input("Play again? y/n")

    while user_input == 'y':
        number_guessing()

        user_input = input("Play again? y/n")


