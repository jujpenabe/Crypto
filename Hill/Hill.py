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


def text_split(text):
    sd = []
    text = text.replace(" ", "")

    for i in range(0, len(text), 2):
        if len(text) % 2 != 0:
            text = text[:] + "x"

        sd.append(text[i : i + 2])
    return sd


def encrypt(text, key):
    new_text = text_split(text)
    cipher_text = []

    det, gcd = inverse_key(key)

    if det == 0 and gcd == 1:
        return

    for i in range(len(new_text)):
        vector = []
        for letter in new_text[i]:
            if letter in alphabet:
                vector.append(alphabet.index(letter))

        c = np.matmul(vector, key)
        c = c % 26

        for index in c:
            cipher_text.append(alphabet[index])

    cipher_text = "".join(cipher_text)
    return cipher_text


def decrypt(text, key):  # encriptar
    new_text = text_split(text)
    cipher_text = []

    det, gcd = inverse_key(key)

    if det == 0 and gcd == 1:
        return

    for i in range(len(new_text)):
        vector = []
        for letter in new_text[i]:
            if letter in alphabet:
                vector.append(alphabet.index(letter))

        c = np.matmul(vector, key)
        c = c % 26

        for index in c:
            cipher_text.append(alphabet[index])

    cipher_text = "".join(cipher_text)
    return cipher_text


def inverse_key(key):
    det = np.linalg.det(key)
    y = 26
    gcd = det % 26
    return (det, gcd)


# TEST
key = [[7, 18], [23, 11]]
text = "vkfzrvwtiazsmisgka"
new_key = np.array(list(key))
new_key = new_key.reshape((2, 2))
# realmente estoy desencriptando
print(encrypt(text, new_key))
text = "numbertheoryiseasy"
key = [[11, 8], [3, 7]]
new_key = np.array(list(key))
new_key = new_key.reshape((2, 2))
decrypt(text, new_key)
