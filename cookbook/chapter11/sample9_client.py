from socket import socket, AF_INET, SOCK_STREAM
from sample9_auth import client_authenticate
secret_key = b'banana'
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 18000))
client_authenticate(s, secret_key)
s.send(b'hello world')
resp = s.recv(1024)
print(resp)