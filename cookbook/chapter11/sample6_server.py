'''
Implementing a Simple Remote Procedure Call with XML-RPC
Problem
    You want an easy way to execute functions or methods in Python programs running on
remote machines.
Solution
    Perhaps the easiest way to implement a simple remote procedure call mechanism is to
use XML-RPC.
'''
from xmlrpc.server import SimpleXMLRPCServer
class KeyValueServer:
    _rpc_methods = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, address):
        self._data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]
    def set(self, name, value):
        self._data[name] = value
    def delete(self, name):
        del self._data[name]
    def exists(self, name):
        return name in self._data
    def keys(self):
        return list(self._data)
    def serv_forever(self):
        self._serv.serve_forever()
if __name__ == '__main__':
    kvserver = KeyValueServer(('', 9090))
    kvserver.serv_forever()