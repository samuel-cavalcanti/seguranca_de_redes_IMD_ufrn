from s_des import SimpleDes
from rc4 import RC4
import sys


def pre_processing_s_des() -> (list, str):
    try:
        message = open(sys.argv[2], "r").read()

        message = list(format(ord(x), 'b') for x in message)


    except:
        print("não foi possível abrir o arquivo", sys.argv[1])
        exit(1)

    try:
        key = format(ord(sys.argv[3]), "b").zfill(10)
    except:
        print("a chave só pode ser um char!!")
        exit(2)

    return message, key


def pre_processing_rc4() -> (str, str):
    parameters = list()

    try:
        message = open(sys.argv[2], "r").read()
    except:
        print("não foi possível abrir o arquivo", sys.argv[2])
        exit(3)

    try:
        key = sys.argv[3]
    except:
        print("digite a chave !!")
        exit(4)

    return message, key  # message , key


def binary_list_to_ascii(text: list) -> str:
    return "".join([chr(int(i, 2)) for i in text])


def execute_des():
    message, key = pre_processing_s_des()
    s_des = SimpleDes()

    try:
        if sys.argv[4] == "d":
            execute = s_des.decrypt
            message = message[:-2]  # bug ao savar em um arquivo é adicionado mais um byte wtf !!
        elif sys.argv[4] == "e":
            execute = s_des.encrypt
        else:
            print("o ultimo argumento diz se é para encriptar ou descriptografar")
            print("digite: d  para descriptografar ou digite: e para encriptar ")
            exit(5)
    except:
        print("o ultimo argumento diz se é para encriptar ou descriptografar")
        print("digite: d  para descriptografar ou digite: e para encriptar ")
        exit(6)

    s_des_message = list()

    for byte in message:
        s_des_message.append(execute(byte.zfill(8), key))

    print(binary_list_to_ascii(s_des_message))


def execute_rc4():
    rc4 = RC4()
    message, key = pre_processing_rc4()

    try:
        if sys.argv[4] == "d":
            message = message[:-2]  # bug ao savar em um arquivo é adicionado mais um byte wtf !!
        elif sys.argv[4] == "e":
            pass
        else:
            print("o ultimo argumento diz se é para encriptar ou descriptografar")
            print("digite: d  para descriptografar ou digite: e para encriptar ")
            exit(5)
    except:
        print("o ultimo argumento diz se é para encriptar ou descriptografar")
        print("digite: d  para descriptografar ou digite: e para encriptar ")
        exit(6)

    print(rc4.execute(message, key))


def main():
    if sys.argv[1] == "des":
        execute_des()
    elif sys.argv[1] == "rc4":
        execute_rc4()
    else:
        print("o primeiro argumento pode ser: des de Simple DES ou rc4 de rc4 mesmo ")
        exit(4)


if __name__ == '__main__':
    main()
