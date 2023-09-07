import argparse
import socket
import struct
import sys
import threading
THE_UMOUNT_OF_WRONG_CONECTOIN = 5
THE_UMOUNT_OF_BITES_IN_NUMER_OF_LEN = 4


'''
we make a server that can acssept several clients and read an encoded massege
'''
def recv_all (sock, bufsize, flags=0):
    '''
    get the massege from client and make it readabol
    :param sock: the massege from client
    : type sock: socket.socket
    :param bufsize: the length of massege from client
    :type bufsize: int
    :param flags: the flags in revc
    :type flags: int
    :return: the massege from client
    :rtype: string
    '''
    result =b''
    while (lenght_diff :=bufsize -len(result))>0:
        result += sock.recv(lenght_diff, flags)
    return result


def run_server (server_ip, server_port):
    '''
    read from client and print it, can get from a number of clients
    :param server_ip: the ip of the server
    : type server_ip: int
    :param server_port: the port of the server
    :type server_port: int
    '''
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((server_ip, server_port))
    serv.listen(THE_UMOUNT_OF_WRONG_CONECTOIN)
    while True:
        conn, addr = serv.accept()
        t = threading.Thread(target=run_server, args=(server_ip, server_port+1))
        t.start()
        #make a another thread to get another client
        message_len, =  struct.unpack('<I', recv_all(conn, THE_UMOUNT_OF_BITES_IN_NUMER_OF_LEN))
        message = recv_all(conn, message_len).decode()
        print(message)
        conn.send("I am SERVER\n".encode())
        conn.close()
    print ('client disconnected and shutdown')


def get_args():
    '''
    take the ip and port from the user and make it usabule 
    :return: the port and ip
    :rtype: argparse.ArgumentParser
    '''
    parser = argparse.ArgumentParser(description="Send data to server.")
    parser.add_argument("server_ip", type=str,
                        help="the server\'s ip")
    parser.add_argument("server_port", type=int,
                        help="the server\'s port")
    print(type(parser))
    return parser.parse_args()


def main():
    '''
    Implementation of CLI and sending data to server.
    '''
    args = get_args()
    try:
        run_server(args.server_ip, args.server_port)
        print('Done.')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
