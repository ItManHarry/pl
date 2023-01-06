'''
Implementing Remote Procedure Calls
Problem
    You want to implement simple remote procedure call (RPC) on top of a message passing
layer, such as sockets, multiprocessing connections, or ZeroMQ.
Solution
    RPC is easy to implement by encoding function requests, arguments, and return values
using pickle, and passing the pickled byte strings between interpreters.
'''
import pickle
class RPCHandler:
    def __init__(self):
        self._functions = {}
    def register_fun(self, function):
        self._functions[function.__name__] = function
    def handle_connection(self, connection):
        try:
            while True:
                # receive message
                func_name, args, kwargs = pickle.loads(connection.recv())
                # Run the RPC and send a message
                try:
                    r = self._functions[func_name](*args, **kwargs)
                    connection.send(pickle.dumps(r))
                except Exception as e:
                    connection.send(pickle.dumps(e))
        except EOFError:
            pass
from multiprocessing.connection import Listener
from threading import Thread
def rpc_server(handler, address, authkey):
    sock = Listener(address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True
        t.start()
def add(x, y):
    return x+y
def sub(x, y):
    return x-y
handler = RPCHandler()
handler.register_fun(add)
handler.register_fun(sub)
rpc_server(handler, ('localhost', 17000), authkey=b'harry')