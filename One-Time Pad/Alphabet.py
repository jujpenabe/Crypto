# Class definition for Alphabet class

import random


class Alphabet:
    # Constructor passing a list of characters
    def __init__(self, alphabet):
        self.alphabet = alphabet
        self.binaryOrder = True
    # Set binary order flag
    def setBinaryOrder(self, binaryOrder = True):
        self.binaryOrder = binaryOrder
    # get all the alphabet
    def getAlphabet(self):
        return self.alphabet
    # get the letter at the specified index
    def getLetterByIndex(self, index):
        # Apply modulo to the index to avoid out of bounds
        return self.alphabet[index % len(self.alphabet)]
    # get a random letter from the alphabet
    def getRandomLetter(self):
        return self.alphabet[random.randint(0, len(self.alphabet) - 1)]
    # get the index of the specified letter
    def getIndexOfLetter(self, letter):
        return self.alphabet.index(letter)
    # get the length of the alphabet
    def getLength(self):
        return len(self.alphabet)
    # get the binary representation of the specified letter
    def getBinaryLetter(self, letter):
        if self.binaryOrder:
            return format(self.getIndexOfLetter(letter), 'b').zfill(len(format(self.getLength() - 1, 'b')))
        else:
            return format(self.getIndexOfLetter(letter), 'b')
            
