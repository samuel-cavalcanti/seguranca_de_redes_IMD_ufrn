import socket
import _thread


class Server:
    __port = 5354
    __clients = list()

    def __init__(self):
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        orig = ("", self.__port)

        self.__tcp.bind(orig)
        self.__tcp.listen(10)

    def __chat_room(self, connection: socket.socket, addr: tuple):

        welcome_msg = "\x02Bem vindo !!\n" \
                      "comandos /des /rc4 /exit\n" \
                      "\exit para sair do chat\n" \
                      "digite: \crypt sdes para iniciar o simple des\n" \
                      "digite: \crypt rc4 para iniciar o rc4 \n" \
                      "exemplo: \crypt sdes \"1010101010\"\n" \
                      "exemplo: \crypt rc4 \"segredo\"\n" \
                      "observe que o segundo parametro: 1010101010 e segredo\n" \
                      "represeta a chave, no caso do Simple DES\n" \
                      "a chave só pode ter 10 bytes\n" \
                      "o RC4 pode ter até 256 caracters \n"

        connection.send(bytes(welcome_msg.encode()))

        while True:

            msg = connection.recv(2048)

            if not msg:
                break

            msg_to_seed = "<{}, {}> \x02{}".format(addr[0], addr[1], msg.decode()).encode()

            self.__broadcast(msg_to_seed, connection)

            print(addr, msg.decode())

        print("Finalizando conexão do cliente {}".format(addr))
        self.__remove_connection(connection)

    def __broadcast(self, message: bytes, connection: socket.socket):
        for client in self.__clients:
            client: socket.socket
            if client != connection:
                try:
                    client.send(message)
                except:
                    self.__remove_connection(client)

    def run(self):

        while True:
            con, client = self.__tcp.accept()

            self.__clients.append(con)
            print("Conectado ao ", client)

            _thread.start_new_thread(self.__chat_room, (con, client))

    def __remove_connection(self, conection: socket.socket):
        if conection in self.__clients:
            self.__clients.remove(conection)
            conection.close()

    def __del__(self):
        print("\ndesconectando o server")
        self.__tcp.close()


def start_server():
    server = Server()
    print("Precione CTRL + C para sair")
    try:
        server.run()
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    start_server()
