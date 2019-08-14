def generete_alphabet() -> (dict, list, list):
    a = 97
    z = 122
    A = 65
    Z = 90
    space = 32
    question_mark = 63
    comma = 44

    alphabet_list = [chr(i) for i in range(a, z + 1)] + [chr(i) for i in range(A, Z + 1)] + [chr(space),
                                                                                             chr(question_mark),
                                                                                             chr(comma)]
    alphabet_table = {key: value for (value, key) in enumerate(alphabet_list)}

    return alphabet_table


def get_encripted_txt() -> str:
    try:
        return open("encripted_text.txt", "r").read()
    except:
        print("não foi possível abrir o arquivo !!")

        return "None"


def save_file(file_name: str, message: str):
    try:
        open(file_name, "w").write(message)
    except:
        print("não foi possível salvar o arquivo !!")


# D(k,C) = (C-k) mod 26, k=1..55
def cesar_decrypt(message: str, k: int, alphabet_table: dict, pos_to_alphabet: list, alphabet_size: int) -> str:
    decrypted_text = str()

    for char in message:
        try:
            pos_char = (alphabet_table[char] - k) % alphabet_size
            new_char = pos_to_alphabet[pos_char]
            if new_char.islower():
                pos_char = (alphabet_table[new_char] + 29) % alphabet_size
                new_char = pos_to_alphabet[pos_char]
        except:
            new_char = char

        decrypted_text += new_char

    return decrypted_text


def save_files(output_file_name: str, decrypted_texts: list):
    for i, decrypted_text in enumerate(decrypted_texts):
        save_file(output_file_name.format(i), decrypted_text)


def main():
    encrypted_text = get_encripted_txt()

    alphabet_table = generete_alphabet()

    pos_to_alphabet = list(alphabet_table.keys())

    alphabet_size = len(alphabet_table)

    output_file_name = "files/cesar_output_{}.txt"

    decrypted_texts = list()

    for i in range(alphabet_size):
        decrypted_texts.append(cesar_decrypt(encrypted_text, i, alphabet_table, pos_to_alphabet, alphabet_size))

    save_files(output_file_name, decrypted_texts)


if __name__ == '__main__':
    main()
