# import socket

# SERVER = socket.gethostbyname(socket.gethostname())

# PORT = 5050

# server = socket.create_connection((SERVER, PORT))
# # server.send(b'Hello')

# FILE_PATH = 'C:\\Users\\Pende\\Documents\\myapps\\my_python_codes\\socket\\test.txt'

# with open(FILE_PATH, 'rb') as f:
#     server.sendfile(f)

import asyncio
import threading
import time
from collections import OrderedDict, deque
from queue import Queue
import argparse

import requests

from bs4 import BeautifulSoup

# async def test():
#     urls = [
#         'https://example.com',
#         'https://example.com'
#     ]
#     for url in urls:
#         return requests.get(url)

# async def testa(response):
#     print(response)

# async def main():
#     response = await test()
#     await testa(response)

# asyncio.run(main())
