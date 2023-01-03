import random
from word_list import words
from hangman_graphic import HANGMAN_GRAPHIC


def get_random_word():
    """ Return a random word from the list of words"""
    game_word = random.choice(words)
    return game_word


def player_name():
    """ Ask player for their name"""
    user_name = input('What is your name? ')
    return user_name


def show_game_board(incorrect_guesses, correct_guesses, game_word):
    """ Display the game board """

    print(HANGMAN_GRAPHIC[len(incorrect_guesses)], '\n')
    print('Incorrect guesses:', end=' ')

    # Display incorrect guesses
    for letter in incorrect_guesses:
        print(letter, end=' ')
    print()

    # create word space for the letters not yet guessed
    word_space = '_' * len(game_word)

    # replace the underscores with correctly guessed letters
    for index, letter in enumerate(game_word):
        if letter in correct_guesses:
            word_space = word_space[:index] + letter + word_space[index + 1:]

    # add spaces between each letter of game word
    for space in word_space:
        print(space, end=' ')
    print()


def get_guess(previous_guesses):
    """ Return players guess"""
    while True:
        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Please enter a single letter.')
        elif guess in previous_guesses:
            print("You've already guessed that letter. Choose again.")
        else:
            return guess


player_name = player_name()
print('Hello', player_name, 'Time to play hangman!')
incorrect_guesses = ''
correct_guesses = ''
game_word = get_random_word()
game_over = False


def play_again():
    """ Ask player if they want to play again"""

    user_input = input('Do you want to play again? (y/n) ')
    while user_input.lower() not in ('y', 'n'):
        user_input = input(
            "Please enter y to play again or n to quit: "
        )

    if user_input == 'y':
        return True


