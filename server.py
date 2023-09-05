import argparse
import sys
import socket
import struct

def recv_all (sock, bufsize, flags=0):
  result =b''
  while (lenght_diff :=bufsize -len(result))>0:
    result += sock.recv(lenght_diff, flags)
  return result

def run_server (server_ip, server_port):
  serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serv.bind((server_ip, server_port))
  serv.listen(5)
  while True:
    conn, addr = serv.accept()
    message_len, =  struct.unpack('<I', recv_all(conn, 4))
    message = recv_all(conn, message_len).decode()
    print (message)
    conn.send("I am SERVER\n".encode())
    conn.close()
  print ('client disconnected and shutdown')

def get_args():
    parser = argparse.ArgumentParser(description='Send data to server.')
    parser.add_argument('server_ip', type=str,
                        help='the server\'s ip')
    parser.add_argument('server_port', type=int,
                        help='the server\'s port')
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
