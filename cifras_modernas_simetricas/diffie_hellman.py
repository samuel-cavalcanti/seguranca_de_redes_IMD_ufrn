import random


class DiffieHellman:

    def __init__(self):
        self.__private_key = -1
        self.public_key = -1
        self.__prime_number = -1
        self.__alpha = -1
        self.session_key = -1

    @staticmethod
    def __poli_dress_and_landreau(n: int) -> int:
        return int(0.25 * (n ** 5 - 133 * n ** 4 + 6729 * n ** 3 - 158379 * n ** 2 + 1720294 * n - 6823316))

    def generate_prime(self):
        n = random.randint(0, 56)

        return self.__poli_dress_and_landreau(n)

    def generate_public_key(self, alpha: int, prime_number: int) -> int:
        self.__private_key = random.randint(0, prime_number)

        self.__alpha = alpha

        self.__prime_number = prime_number

        self.public_key = alpha * self.__private_key % prime_number

        return self.public_key

    def calculate_session_key(self, public_key: int) -> int:
        self.session_key = public_key ** self.__private_key % self.__prime_number

        return self.session_key


def testHellman():
    diffie_hellman = DiffieHellman()
    n = diffie_hellman.generate_prime()


if __name__ == '__main__':
    testHellman()
