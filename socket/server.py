import asyncio
import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())

PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))

async def do_something():
    print('Kendall Jenner')

async def main():
    await do_something()

def connection_handler(conn, addr):
    print('[MESSAGE] Received message')
    with conn:
        message = conn.recv(1024)
        asyncio.run(main())
        print(message.decode('utf-8'))
        conn.close()

def start_server():
    server.listen()
    print(f'[SERVER] Started on {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=connection_handler, args=(conn, addr))
        thread.start()

start_server()
