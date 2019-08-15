from itertools import cycle


def generate_vigenere_matrix() -> dict:
    a = 97
    z = 122
    alphabet_list = [chr(i) for i in range(a, z + 1)]
    alphabet_size = len(alphabet_list)

    vigenere_matrix = dict()
    for i, char_row in enumerate(alphabet_list):
        column = dict()
        for j, char_col in enumerate(alphabet_list):
            column[char_col] = alphabet_list[(j + i) % alphabet_size]
        vigenere_matrix[char_row] = column

    return vigenere_matrix



def generete_decrypted_vigenere_matrix() -> dict:
    a = 97
    z = 122
    alphabet_list = [chr(i) for i in range(a, z + 1)]
    alphabet_size = len(alphabet_list)

    decrypted_matrix = dict()
    for i, key in enumerate(alphabet_list):
        column = dict()
        for j, decrypted_char in enumerate(alphabet_list):
            value = alphabet_list[(j + i) % alphabet_size]
            column[value] = decrypted_char
        decrypted_matrix[key] = column

    return decrypted_matrix
    # matrix[key][value] == decrypted_char

def print_vigenere_matrix(matrix: dict):
    for row in matrix:
        txt = ""
        for col in matrix[row]:
            txt += matrix[row][col] + " "
        print(txt)


# matrix[chave|linha ][valor]= coluna
def decrypt_message(encrypted_message: str, key: str) -> str:
    decrypted_matrix = generete_decrypted_vigenere_matrix()
    iter_encrypted_message = iter(encrypted_message)
    decrypted_message = str()

    for key_char in cycle(key):
        encrypted_char = next(iter_encrypted_message, None)

        while encrypted_char == " ":
            decrypted_message += encrypted_char
            encrypted_char = next(iter_encrypted_message, None)

        if encrypted_char is None:
            break

        decrypted_message += decrypted_matrix[key_char][encrypted_char]

    return decrypted_message


def main():
    encrypted_message = "w gags domj a esgpi so eiu dm goze qnyjaaxa hikinq frmh tvkdea irvwfea eaee frmh peefoa se gvugw"
    key = "ipanema"

    decrypted_message = decrypt_message(encrypted_message, key)

    print(decrypted_message)


# print(message)


pass

if __name__ == '__main__':
    main()
