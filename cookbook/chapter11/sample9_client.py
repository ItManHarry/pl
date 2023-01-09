from socket import socket, AF_INET, SOCK_STREAM
from sample9_auth import client_authenticate
secret_key = b'banana'
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 18000))
client_authenticate(s, secret_key)
message = '世界，你好！'
s.send(message.encode('utf-8'))
resp = s.recv(1024)
print(type(resp))
message = resp.decode('utf-8')
print(type(message))
print(message)