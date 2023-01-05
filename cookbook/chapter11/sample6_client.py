from xmlrpc.client import ServerProxy
s = ServerProxy('http://localhost:9090', allow_none=True)
s.set('name', 'Harry')
s.set('age', 40)
s.set('hobbies', ['Movies', 'Basketball', 'Ping-Pong'])
print(s.keys())
print(s.get('name'))
print(s.get('age'))
print(s.get('hobbies'))
s.delete('hobbies')
print(s.exists('hobbies'))