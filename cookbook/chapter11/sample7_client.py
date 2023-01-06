from multiprocessing.connection import Client
c = Client(('localhost', 7070), authkey=b'peekaboo')
c.send('Hello')
print(c.recv())
c.send(40)
print(c.recv())
c.send([1, 2, 3, 4, 5])
print(c.recv())