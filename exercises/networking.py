import socket
import argparse
from threading import Thread
import time

HOST = '127.0.0.1'

PORT = 5000

def retrieve_file(host, port):
    pass

def create_server(**kwargs):
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(5)

    print('Server started.')

    while True:
        c, addr = s.accept()
        print('Server connected to ', str(addr))

        t = Thread(target=retrieve_file, args=('retrieve_file', c))
        t.start()
    
    s.close()

if __name__ == "__main__":
    args = argparse.ArgumentParser(description='args')
    args.add_argument('--port')
    args.add_argument('--host')
    args.add_argument('--stop', help='A timestamp representing a time to end server')
    parsed_args = args.parse_args()

    if parsed_args.host:
        HOST = parsed_args.host

    if parsed_args.port:
        PORT = parsed_args.port

    create_server()
