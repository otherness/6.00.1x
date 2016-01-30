# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "D:/Python/6.00.1x/pset3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    shadowWord = ''
    for letter in secretWord:
        if letter not in lettersGuessed:
            shadowWord += "_"
        else:
            shadowWord += letter
    return shadowWord



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availLetters = string.ascii_lowercase
    for letter in lettersGuessed:
        availLetters=availLetters.replace(letter, '')
    return availLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    
    guessedLetters = []
    attemptsLeft = 8
    
    while (not isWordGuessed(secretWord, guessedLetters)) and attemptsLeft > 0:
        guessIsSane = False
        while not guessIsSane:
            print "-------------"
            print "You have " + str(attemptsLeft) + " guesses left."
            print "Available letters: " + getAvailableLetters(guessedLetters)
            guess = raw_input("Please guess a letter: ")
            guess = guess.lower()
            if (len(guess) > 1) or (guess not in string.ascii_lowercase):
                print "Please provide a single letter."
            elif guess in guessedLetters:
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, guessedLetters)
            else:
                #len(guess) == 1 and guess not in guessedLetters:
                guessIsSane = True
                guessedLetters.append(guess)
                if guess in secretWord:
                    print "Good guess: " + getGuessedWord(secretWord, guessedLetters)
                else:
                    print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, guessedLetters)
                    attemptsLeft -= 1
    
    if isWordGuessed(secretWord, guessedLetters):
        print "-------------"
        print "Congratulations, you won!"
    if attemptsLeft < 1:
        print "-------------"
        print "Sorry, you ran out of guesses. The word was " + secretWord + "."
                


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = "falcon"
hangman(secretWord)
