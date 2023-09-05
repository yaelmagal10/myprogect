import argparse
import socket
import sys
import struct

'''
we make a client that can wirte to the server encoded
'''

def send_data(server_ip, server_port, data):
    '''
    read from client and print it, can get from a number of clients
    :param server_ip: the ip of the server
    : type server_ip: int
    :param server_port: the port of the server
    :type server_port: int
    '''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    data_len = len(data)
    data_len = struct.pack('<I', data_len)
    client.sendall(data_len)
    client.sendall(data.encode())
    client.close()



def get_args():
    '''
    take the ip and port and massege from the user and make it usabule 
    :return: the port and ip and massege
    :rtype: argparse.ArgumentParser
    '''
    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the server\'s ip')
    parser.add_argument('server_port', type=int,
                        help='the server\'s port')
    parser.add_argument('data', type=str,
                        help='the data')
    return parser.parse_args()


def main():
    '''
    Implementation of CLI and sending data to server.
    '''
    args = get_args()
    try:
        send_data(args.server_ip, args.server_port, args.data)
        print('Done.')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
