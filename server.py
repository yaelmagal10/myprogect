import socket
def run_server (server_ip, server_port):
  serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serv.bind((server_port, server_ip))
  serv.listen(5)
  while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
      data = conn.recv(4096)
      if not data: break
      from_client += data.decode('utf8')
      print (from_client)
      conn.send("I am SERVER\n".encode())
    conn.close()
  print ('client disconnected and shutdown')
def main():
    '''
    Implementation of CLI and sending data to server.
    '''
    args = get_args()
    try:
        run_server(args.server_ip, args.server_port, args.data)
        print('Done.')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())
