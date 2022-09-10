def playfair_cipher(keyword, plaintext, option=0):
    def combine_keyword(keyword):
        list_string = list(keyword)
        key = []
        for char in list_string:
            if char not in key:
                if char == 'i' or char == 'j':
                    key.append('ij')
                else:
                    key.append(char)
        return key

    # square = [['a', 'b', 'c', 'd', 'e'],
    #           ['f', 'g', 'h', 'ij', 'k'],
    #           ['l', 'm', 'n', 'o', 'p'],
    #           ['q', 'r', 's', 't', 'u'],
    #           ['v', 'w', 'x', 'y', 'z'],]

    def generate_square(key):
        for char in alphabet:
            if char not in key:
                key.append(char)
        newSquare = []
        for i in range(5):
            newRowSquare = []
            for j in range(5):
                newRowSquare.append(key[j + (5 * i)])
            newSquare.append(newRowSquare)
        return newSquare

    def convert_plaintext(text):
        list_message = list(text.lower())
        new_message = []
        for i in range(len(list_message)):
            if list_message[i] in originalalphabet:
                new_message.append(list_message[i])
            if i + 1 < len(list_message):
                if list_message[i + 1] == list_message[i]:
                    new_message.append('x')
        if len(new_message) % 2 == 1:
            new_message.append('x')
        return new_message

    def encrypt_message(square, twos):
        encrypted_message = []
        for i in range(len(twos)):
            if (i % 2) == 0:
                fi = twos[i]
                se = twos[i + 1]

                if fi == 'i' or fi == 'j': fi = 'ij'
                if se == 'i' or se == 'j': se = 'ij'
                for i in range(5):
                    for j in range(5):
                        if square[i][j] == fi:
                            ficol = j
                            firow = i
                        if square[i][j] == se:
                            secol = j
                            serow = i
                # First Rule: Same Column, down one row
                if ficol == secol:
                    fi = square[(firow + 1) % 5][ficol]
                    se = square[(serow + 1) % 5][secol]
                # Second Rule: Same Row, right one column
                elif firow == serow:
                    fi = square[firow][(ficol + 1) % 5]
                    se = square[serow][(secol + 1) % 5]
                # Third Rule: Same Row, diferent column
                else:
                    fi = square[firow][secol]
                    se = square[serow][ficol]
                encrypted_message.append(fi)
                encrypted_message.append(se)
        print("Encrypted Message: \n" + ''.join(encrypted_message))
        return encrypted_message

    def decrypt_message(square, encrypted):
        decrypted_message = []
        for i in range(len(encrypted)):
            if (i % 2) == 0:
                fi = encrypted[i]
                se = encrypted[i + 1]
                if fi == 'i' or fi == 'j': fi = 'ij'
                if se == 'i' or se == 'j': se = 'ij'
                for i in range(5):
                    for j in range(5):
                        if square[i][j] == fi:
                            ficol = j
                            firow = i
                        if square[i][j] == se:
                            secol = j
                            serow = i
                # Inversed First Rule: Same Column, up one row
                if ficol == secol:
                    fi = square[(firow - 1) % 5][ficol]
                    se = square[(serow - 1) % 5][secol]
                # Inversed Second Rule: Same Row, left one column
                elif firow == serow:
                    fi = square[firow][(ficol - 1) % 5]
                    se = square[serow][(secol - 1) % 5]
                # Inversed Third Rule: Same Row, different column
                else:
                    fi = square[firow][secol]
                    se = square[serow][ficol]
                decrypted_message.append(fi)
                decrypted_message.append(se)
        print("Decrypted Message: \n" + ''.join(decrypted_message))
        return decrypted_message

    alphabet = ['a', 'b', 'c', 'd', 'e',
                'f', 'g', 'h', 'ij', 'k',
                'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']

    originalalphabet = ['a', 'b', 'c', 'd', 'e',
                        'f', 'g', 'h', 'i', 'k',
                        'l', 'm', 'n', 'o', 'p',
                        'q', 'r', 's', 't', 'u',
                        'v', 'w', 'x', 'y', 'z']

    key = combine_keyword(keyword)  #
    newSquare = generate_square(key)  # Should be merged
    if option == 0:
        converted_plaintext = convert_plaintext(plaintext)
        encrypt_message(newSquare, converted_plaintext)
    elif option == 1:
        decrypt_message(newSquare, plaintext)

if __name__ == '__main__':
    print("Para encriptar su mensaje presione 0 \n para decifrar el mensaje presione 1")
    option = input()
    if option == '1':
        print("Ingrese la palabra clave (o frase sin espacios): ")
        keyword = input()
        print("Ingrese el texto a decifrar: ")
        plaintext = input()
        playfair_cipher(keyword, plaintext, 1)
    else:
        print("Ingrese una palabra clave (o frase sin espacios): ")
        keyword = input()
        print("Ingrese el texto a cifrar: ")
        plaintext = input()
        playfair_cipher(keyword, plaintext, 0)
    # encipher_key('yoanpinzon', 'THIS SECRET MESSAGE IS ENCRYPTED')
