import math

def caesar_cipher( text, perm, option=0 ):
    cipher_text = []
    sign = 1
    if option == 1:
        sign = -1
    for i in range(len(text)):
        ascii = (ord(text[i]))
        new_ascii = 32
        if (ascii >= 97 and ascii <= 122):
            # First subtract the value to range 0 - # of characters
            new_ascii = ascii - 97
            # Apply modulo tosnap the value into the range
            new_ascii = (new_ascii + (perm * sign)) % 26
            # Lastly add the same subtracted value
            new_ascii = new_ascii + 97
        elif (ascii >= 65 and ascii <= 90):
            # Same as above but with different value
            new_ascii = ascii - 65
            new_ascii = (new_ascii + (perm * sign)) % 26
            new_ascii = new_ascii + 65
        caesar = chr(new_ascii)
        cipher_text.append(caesar)
        output = "".join(cipher_text)
    if (option == 0):
        print( "Texto cifrado:")
    else:
        print("Texto decifrado:")
    print(output)

if __name__ == '__main__':
    while True:
        try:
            print("Para encriptar su mensaje presione 0 \n para decifrar el mensaje presione 1")
            option = int(input())
            if (option < 0 and option > 1):
                print("Por favor ingrese un valor entre 0 y 1")
                continue
            break
        except ValueError:
            print("Por favor ingrese solo valores enteros...")
            continue
    while True:
        try:
            print("Ingrese el numero de permutaciones (k): ")
            permutaciones = int(input())
            if (permutaciones > 0):
                break
            print ("Por favor ingrese valores positivos y distinto de 1")
            continue
        except ValueError:
            print("Por favor ingrese solo valores enteros...")
    if option == 1:
        print("Ingrese el texto a decifrar: ")
        plaintext = input()
        caesar_cipher(plaintext, permutaciones, option)
    else:
        print("Ingrese el texto a cifrar: ")
        plaintext = input()
        caesar_cipher(plaintext, permutaciones, option)
