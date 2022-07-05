'''
Problem
    You want to make your objects support the context-management protocol (the with
statement).
Solution
    In order to make an object compatible with the with statement, you need to implement
__enter__() and __exit__() methods.
'''
from socket import socket, AF_INET, SOCK_STREAM
class LazySingleConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected!!!')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None
from functools import partial
conn = LazySingleConnection(('www.python.org', 80))
with conn as s:
    s.send(b'GET /index.html HTTPS/1.0\r\n')
    s.send(b'Host:www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)
'''
The main principle behind writing a context manager is that you’re writing code that’s
meant to surround a block of statements as defined by the use of the with statement.
When the with statement is first encountered, the __enter__() method is triggered.
The return value of __enter__() (if any) is placed into the variable indicated with the
as qualifier. Afterward, the statements in the body of the with statement execute. Finally,
the __exit__() method is triggered to clean up.
    This control flow happens regardless of what happens in the body of the with statement,
including if there are exceptions. In fact, the three arguments to the __exit__() method
contain the exception type, value, and traceback for pending exceptions (if any). The
__exit__() method can choose to use the exception information in some way or to
ignore it by doing nothing and returning None as a result. If __exit__() returns True,
the exception is cleared as if nothing happened and the program continues executing
statements immediately after the with block.
'''
print('-' * 80)
class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connections.pop().close()
conn = LazyConnection(('www.python.org', 80))
with conn as s:
    s.send(b'GET /index.html HTTPS/1.0\r\n')
    s.send(b'Host:www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    print(resp)
    with conn as s2:
        s2.send(b'GET /index.html HTTPS/1.0\r\n')
        s2.send(b'Host:www.python.org\r\n')
        s2.send(b'\r\n')
        resp2 = b''.join(iter(partial(s2.recv, 8192), b''))
        print(resp2)