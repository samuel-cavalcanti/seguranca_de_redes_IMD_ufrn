class SimpleDes:
    ########### 2  4  3  1
    __p4_key = [1, 3, 2, 0]
    ##########  6  3  7  4  8  5  10 9
    __p8_key = [5, 2, 6, 3, 7, 4, 9, 8]

    ############ 3  5  2  7  4 10  1  9  8  6
    __p10_key = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]

    ####### 2  6  3  1  4  8  5  7
    __IP = [1, 5, 2, 0, 3, 7, 4, 6]
    ####### 4  1  3  5  7  2  8  6
    __FP = [3, 0, 2, 4, 6, 1, 7, 5]
    ###### 4  1  2  3  2  3  4  1
    __E = [3, 0, 1, 2, 1, 2, 3, 0]

    __s0 = [[1, 0, 3, 2],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 3, 2]]

    __s1 = [[1, 1, 2, 3],
            [2, 0, 1, 3],
            [3, 0, 1, 0],
            [2, 1, 0, 3]]

    __to_binary = {0: "00", 1: "01", 2: "10", 3: "11"}

    def __permutation(self, text: str, key: list) -> str:
        permutation_string = str()

        for index in key:
            permutation_string += text[index]

        return permutation_string

    def __split_bytes(self, text: str):
        half = int(len(text) / 2)

        return text[0:half], text[half:]

    def __left_shift(self, value: str):
        head = value[0]

        tail = value[1:]

        return tail + head

    def __xor(self, text: str, key: str) -> str:

        xor_string = str()
        for i, j in zip(text, key):
            if i == j:
                xor_string += "0"
            else:
                xor_string += "1"

        return xor_string

    def __box(self, text: str, matrix: list) -> str:

        row = int(text[0] + text[-1], 2)
        col = int(text[1] + text[2], 2)

        int_value = matrix[row][col]

        return self.__to_binary[int_value]

    def __make_keys(self, key: str) -> (str, str):
        left, right = self.__split_bytes(self.__permutation(key, self.__p10_key))

        left_shift = self.__left_shift(left)

        right_shift = self.__left_shift(right)

        k1 = left_shift + right_shift

        k1 = self.__permutation(k1, self.__p8_key)

        double_left_shift = self.__left_shift(self.__left_shift(left_shift))

        double_right_shift = self.__left_shift(self.__left_shift(right_shift))

        k2 = double_left_shift + double_right_shift

        k2 = self.__permutation(k2, self.__p8_key)

        return k1, k2

    def __f_k(self, left_plain_text: str, right_plain_text: str, key: str):

        expanded = self.__permutation(right_plain_text, self.__E)

        left, right = self.__split_bytes(self.__xor(expanded, key))

        left_box = self.__box(left, self.__s0)
        right_box = self.__box(right, self.__s1)

        output_p4 = self.__permutation(left_box + right_box, self.__p4_key)

        f_k = self.__xor(output_p4, left_plain_text)

        return f_k, right_plain_text

    def encrypt(self, plain_text: str, key: str) -> str:

        left, right = self.__split_bytes(self.__permutation(plain_text, self.__IP))

        keys = self.__make_keys(key)

        for key in keys:
            right, left = self.__f_k(left, right, key)

        return self.__permutation(right + left, self.__FP)

    def decrypt(self, plain_text: str, key: str) -> str:

        left, right = self.__split_bytes(self.__permutation(plain_text, self.__IP))

        keys = self.__make_keys(key)[::-1]

        for key in keys:
            right, left = self.__f_k(left, right, key)

        return self.__permutation(right + left, self.__FP)


def tests():
    # https://terenceli.github.io/assets/file/mimaxue/SDES.pdf
    key = "1100011110"
    plain_text = "00101000"

    print("size text", len(plain_text))
    print("size  key", len(key))

    k1_true = "11101001"
    k2_true = "10100111"
    encrypted_true = "10001010"

    sim = SimpleDes()

    encrypted_text = sim.encrypt(plain_text, key)

    if encrypted_text == encrypted_true:
        print("encryption works !")
    else:
        print("encryption fail ", encrypted_text)

    text = sim.decrypt(encrypted_true, key)

    if text == plain_text:
        print("decrypt works !")
    else:
        print("decrypt fail", text)


if __name__ == '__main__':
    tests()
