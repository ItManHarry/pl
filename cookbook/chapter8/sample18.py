'''
Implementing Stateful Objects or State Machines
Problem
You want to implement a state machine or an object that operates in a number of different
states, but don’t want to litter your code with a lot of conditionals.
Solution
In certain applications, you might have objects that operate differently according to
some kind of internal state.
'''
class Connection:
    def __init__(self):
        self.state = 'CLOSED'

    def read(self):
        if self.state != 'OPEN':
            raise RuntimeError('NOT OPENED')
        print('Reading ...')

    def write(self):
        if self.state != 'OPEN':
            raise RuntimeError('NOT OPENED')
        print('Writing ...')

    def open(self):
        if self.state == 'OPEN':
            raise RuntimeError('Already opened ...')
        self.state = 'OPEN'

    def close(self):
        if self.state == 'CLOSED':
            raise RuntimeError('Already closed ...')
        self.state = 'CLOSED'
'''
This implementation presents a couple of difficulties. First, the code is complicated by
the introduction of many conditional checks for the state. Second, the performance is
degraded because common operations (e.g., read() and write()) always check the state
before proceeding.
A more elegant approach is to encode each operational state as a separate class and
arrange for the Connection class to delegate to the state class. For example:
'''
class ConnectionExt:
    def __init__(self):
        self.new_state(ClosedConnectionState)
    def new_state(self, state):
        self._state = state
    def read(self):
        return self._state.read(self)
    def write(self):
        return self._state.write(self)
    def open(self):
        return self._state.open(self)
    def close(self):
        return self._state.close(self)
class ConnectionState:
    @staticmethod
    def read(conn):
        raise NotImplementedError()
    @staticmethod
    def write(conn):
        raise NotImplementedError()
    @staticmethod
    def open(conn):
        raise NotImplementedError()
    @staticmethod
    def close(conn):
        raise NotImplementedError()
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not Opened!')
    @staticmethod
    def write(conn):
        raise RuntimeError('Not Opened!')
    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)
    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed!')
class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('Reading ...')
    @staticmethod
    def write(conn):
        print('Writing ...')
    @staticmethod
    def open(conn):
        raise RuntimeError('Already Opened ...')
    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)
c_e = ConnectionExt()
c_e.open()
c_e.read()
c_e.write()
c_e.close()