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
    pass


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

    # replace the pass statement with your code
    pass


# If you want to test the game, you can use the following line
# Feel free to change the words in the list to check against
# different kind of input.
initialize(['Melkor','Beethoven','Harry Potter','Alladin'])