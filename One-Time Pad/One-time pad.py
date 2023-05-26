# One-time Pad
# import alphabet class
from Alphabet import Alphabet


# Pass a string to encrypt the message with optional key of the same size
def encrypt(message, alphabet, key = ''):
    # generate the key
    key = generateKey(message, alphabet, key)
    # convert the message and key to binary
    binMessage = convertCharToBin(message, alphabet)
    binKey = convertCharToBin(key, alphabet)
    # encrypt the message using xor operation
    encryptedList = xorListsOfStrings(binMessage, binKey)
    # Print the encrypted list as binary concatenated
    print('Encrypted message as binary: ' + ''.join(encryptedList))
    # convert the encrypted message to string
    encryptedMessage = ''
    for i in range(len(encryptedList)):
        encryptedMessage += alphabet.getLetterByIndex(int(encryptedList[i], 2))
    return encryptedMessage

def generateKey(message, alphabet, key):
    # if the key is not the same size, generate 'autokey' by appending the message until the key is the same size
    if len(key) == 0:
        key = generateRandomKey(message, alphabet)
    elif len(key) != len(message):
        key = generateAutoKey(message, key)
    else:
        pass
    return key

def generateRandomKey(size, alphabet):
    key = ''
    for i in range(size):
        key += alphabet.getRandomLetter()
    return key

def generateAutoKey(message, key):
    # Remove spaces from the message
    message = message.replace(' ', '')
    # if the key is smaller than the message, append the message to the key until the key is the same size
    while len(key) < len(message):
        key += message[len(key)]
    print('Autokey: ' + key)
    return key

def convertCharToBin(message, alphabet):
    message = list(message)
    for i in range(len(message)):
        message[i] = alphabet.getBinaryLetter(message[i])
    return message

def xorListsOfStrings(list1, list2):
    encryptedMessage = []
    for i in range(len(list1)):
        tmpBinMessageList = list(list1[i])
        tmpBinKeyList = list(list2[i])
        tmpEncryptedMessage = ''
        for j in range(len(tmpBinMessageList)):
            tmpEncryptedMessage += str(int(tmpBinMessageList[j]) ^ int(tmpBinKeyList[j]))
        
        encryptedMessage.append(tmpEncryptedMessage)
    return encryptedMessage
# TEST
# create a new english alphabet
englishAlphabet = Alphabet('abcdefghijklmnopqrstuvwxyz ')

print(encrypt('tonto es el que hace tonterias', englishAlphabet, 'gravity'))