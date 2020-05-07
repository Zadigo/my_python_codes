#!/bin/bash

from http.server import SimpleHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import time

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    """Simple multi-threaded HTTP server
    """
    pass

class Requests(SimpleHTTPRequestHandler):
    """Handler for managing requests
    """
    def do_GET(self):
        message = 'Thanks for using our server'
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.send_header('Content-length', str(len(message)))
        self.end_headers()
        # self.wfile.write(msg)

def start_server():
    server_address = ('localhost', 4000)
    server = ThreadingHTTPServer(server_address, Requests)
    print(f'Starting server on localhost.')
    server.serve_forever()

if __name__ == "__main__":
    start_server()
