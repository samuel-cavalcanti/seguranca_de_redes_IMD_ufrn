class RC4:
    __s = None
    __size = 256

    def execute(self, plain_text: str, key: str) -> str:
        self.__initialize(key)
        encrypted_text = str()

        i = 0
        j = 0

        for char in plain_text:
            int_value = ord(char)

            i = (i + 1) % self.__size

            j = (j + self.__s[i]) % self.__size

            self.__s[i], self.__s[j] = self.__s[j], self.__s[i]

            t = (self.__s[i] + self.__s[j]) % self.__size

            k = self.__s[t]

            encrypted_byte = int_value ^ k

            encrypted_text += chr(encrypted_byte)

        return encrypted_text

    def __initialize(self, key: str):
        size = len(key)

        self.__s = list(range(256))

        j = 0

        for i in range(self.__size):
            t_i = ord(key[i % size])

            j = (j + self.__s[i] + t_i) % self.__size

            self.__s[i], self.__s[j] = self.__s[j], self.__s[i]


def test_rc4():
    message = "oi eu sou rc4"
    key = "segredo"

    rc4 = RC4()

    encrypted_text = rc4.execute(message, key)

    decrypted_text = rc4.execute(encrypted_text, key)

    print("decrypted_text", decrypted_text)

    print("encrypted_text", encrypted_text)
    
    
    


if __name__ == '__main__':
    test_rc4()
