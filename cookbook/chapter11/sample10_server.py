'''
Adding SSL to Network Services
Problem
    You want to implement a network service involving sockets where servers and clients
authenticate themselves and encrypt the transmitted data using SSL.
Solution
    The ssl module provides support for adding SSL to low-level socket connections. In
particular, the ssl.wrap_socket() function takes an existing socket and wraps an SSL
layer around it. For example, here’s an example of a simple echo server that presents a
server certificate to connecting clients
'''
from socket import socket, AF_INET, SOCK_STREAM
import ssl
KEYFILE = 'server_key.pem'
CERTFILE = 'server_cert.pem'
def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('Connection closed!')
def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)
    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE, server_side=True)
    while True:
        try:
            c, a = s_ssl.accept()
            print('Got connection ', c, a)
            echo_client(c)
        except Exception as e:
            print('{}: {}'.format(e.__class__.__name__, e))
echo_server(('', 20000))