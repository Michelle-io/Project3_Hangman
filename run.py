import random
from word_list import words
from hangman_graphic import HANGMAN_GRAPHIC


def get_random_word():
    """ Return a random word from the list of words"""
    game_word = random.choice(words)
    return game_word
