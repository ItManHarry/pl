'''
Creating a UDP Server
Problem
You want to implement a server that communicates with clients using the UDP Internet
protocol.
Solution
As with TCP, UDP servers are also easy to create using the socketserver library.
'''
from socketserver import BaseRequestHandler, UDPServer
import time
class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from : ', self.client_address)
        message, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)
if __name__ == '__main__':
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()