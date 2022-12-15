'''
Creating a TCP Server
Problem
You want to implement a server that communicates with clients using the TCP Internet
protocol.
Solution
An easy way to create a TCP server is to use the socketserver library.
'''
from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler
class EchoBaseHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from : ', self.client_address)
        while True:
            message = self.request.recv(8192)
            if not message:
                break
            self.request.send(message)
class EchoStreamHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from : ', self.client_address)
        for line in self.rfile:
            self.wfile.write(line)
            self.request.send(line)
if __name__ == '__main__':
    # server = TCPServer(('', 20000), EchoBaseHandler)
    server = TCPServer(('', 20000), EchoStreamHandler)
    server.serve_forever()