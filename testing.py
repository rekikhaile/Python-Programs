TRIES = 10

def initialize(word_list, user_input=None):
	"""
	Takes a list of words as a parameter.
	Starting with the word in the word_list,
	starts a new game using the word.
	If the user wants to play again, starts the next
	game with the next word.
	Runs until user doesn't want to play or
	until it runs out of new words.
	"""
	if user_input:import sys;sys.stdin = user_input # some hacky manipulations for automated testing
	current_word_index = 0
	while start_new_game(word_list[current_word_index], TRIES) and current_word_index <= len(word_list):
		current_word_index += 1

def obfuscate(word, letters_guessed):
    """
    Takes the current word being guessed and
    a string containing letters, that user has
    tried to guess during current playthrough.

    Returns a string, that only shows letters
    that the user has guessed correctly. Return
    the guessed letter in uppercase. The letters,
    that user still has to guess are replaced with
    underscores.


    Example:
        input: 'claire','abcd'
        ouput: 'C_A___'
    Example:
        input: 'Amanda','etai'
        output: 'A_A__A'
    Example:
        input: 'Obi-Wan KENOBI','oteai'
        output: 'O_I-_A_ _E_O_I'
    """
    # replace the pass statement with your code
    i = 0
    j = 0
    output = ''
    for i in range(len(word)):
        for j in range(len(letters_guessed)):
            if word[i].lower() == letters_guessed[j] or word[i].isalpha() == False:
                output += word[i].upper()
                break
        else:
            output += '_'

    return output

def start_new_game(word, max_tries):
    """
    # Arguments
    Takes a word (string) that the user has to guess,
    and max_tries (int) - the number of tries user has
    before he loses the game.


    # Description
    Before prompting the user always show the letters he still hasn't tried to guess.
    This function should prompt user for a letter, and
    check, whether the letter guessed is in the word.
    If user guessed correctly, reveal the letter to him.
    If user guessed wrong, decrease the number of tries and show the amount of tries remaining.

    Keep asking user for more letters, until he wins or loses.
    When the game ends, ask user to choose, whether they want
    to play the game again.
    If the user types 'n', return False.
    If the user types 'y', return True.
    User will only input 'n' or 'y', so don't return anything

    # Return
    Returns a boolean, stating whether user
    wants to have another game.

    Example:
        input: 'Obi-Wan Kenobi',
        execution: user wins, wants to play again,
                    types 'y' when prompted
        output: True
    Example:
        input: 'GANDALF',
        execution: user wins, doesn't want to play again,
                    types 'n' when prompted
        output: False

    """

    player_won = False
    tries_left = max_tries
    untried_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    correct_letters = ""

    print(obfuscate(word, ""))

    while tries_left > 0:
            output = ""

            for l in untried_letters:
                output += l

            print(output)

            guess = input('Your guess:')

            while not (len(guess) == 1 and guess.isalpha()):
                print("Please input a single letter")
                guess = input('Your guess:')

            guess = guess.lower()

            found = False

            for l in word:
                if guess == l.lower():
                    found = True
                    break

            if found == True:
                correct_letters += guess

                index = 0

                for i in range(len(untried_letters)):
                    if untried_letters[i] == guess:
                        index = i
                        break

                del untried_letters[index]
            else:
                tries_left -= 1
                print(str(tries_left) + " tries left")

            display_word = obfuscate(word, correct_letters)

            found = False

            for l in display_word:
                if l == '_':
                    found = True
                    break

            print(display_word)

            if found == False:
                player_won = True
                break

    if player_won == True:
        print("You win !")
    else:
        print("You lose")

    play_again = input("Play again [y/n] ? ")

    if play_again == 'y':
        return True
    else:
        return False

initialize(['Melkor','Beethoven','Harry Potter','Alladin'])
