import numpy as np

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
# latin alphabet, alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, key, t):
    text = text.lower()
    text = text.replace(" ", "")
    key = key.lower()
    new_text = []
    new_key = []

    if len(text) > len(key):
        for i in range(len(text)):
            index = i % len(key)
            new_key.append(key[index])
    key = "".join(new_key)
    new_key.clear()

    for i in range(0, len(text), t):
        new_text.append(text[i : i + t])
        new_key.append(key[i : i + t])

    ciphered_text = []
    for i in range(len(new_text)):
        new_group = []
        for j in range(t):
            index_text = alphabet.index(new_text[i][j])
            index_key = alphabet.index(new_key[i][j])
            new_letter = table[index_text][index_key]
            new_group.append(new_letter)
        ciphered_text.append("".join(new_group))

    return ciphered_text


def decrypt(text, key, t):
    text = text.lower()
    text = text.replace(" ", "")
    key = key.lower()
    new_key = []

    if len(text) > len(key):
        for i in range(len(text)):
            index = i % len(key)
            new_key.append(key[index])
    key = "".join(new_key)
    new_key.clear()

    plain_text = []
    for i in range(len(text)):
        first = table[alphabet.index(key[i])]
        second = first.index(text[i])
        new_letter = table[second][0]
        plain_text.append(new_letter)

    plain_text = "".join(plain_text)
    return plain_text


def create_table():
    global table
    table = [""] * 26
    for i in range(26):
        my_list = []
        for j in range(26):
            new_index = i + j  # hop + letra actual que se quiere
            new_index = new_index % 26
            my_list.append(alphabet[new_index])
        table[i] = my_list
