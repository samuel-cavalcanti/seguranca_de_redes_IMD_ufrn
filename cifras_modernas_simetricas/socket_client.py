import socket
import select
import sys
from s_des import SimpleDes

class Client:
    __port = 5354

    def __init__(self):
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host: str):
        dest = (host, self.__port)

        self.__tcp.connect(dest)

        sockets_list = [sys.stdin, self.__tcp]

        print("para sair use  CTRL +X")

        while True:
            read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])

            for socks in read_sockets:
                if socks == self.__tcp:
                    socks: socket.socket
                    message: bytes = socks.recv(2048)
                    print(message.decode())
                else:
                    message: str = sys.stdin.readline()
                    self.__tcp.send(bytes(message.encode()))
                    sys.stdout.write("<You> {}".format(message))
                    sys.stdout.flush()

        # self.__tcp.close()


def start_client():
    client = Client()

    client.connect("127.0.0.1")


if __name__ == '__main__':
    start_client()
