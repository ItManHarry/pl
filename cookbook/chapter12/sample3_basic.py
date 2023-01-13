'''
Communicating Between Threads
Problem
    You have multiple threads in your program and you want to safely communicate or
exchange data between them.
Solution
    Perhaps the safest way to send data from one thread to another is to use a Queue from
the queue library. To do this, you create a Queue instance that is shared by the threads.
Threads then use put() or get() operations to add or remove items from the queue.
'''
from queue import Queue
from threading import Thread
class DataProducer:
    def __init__(self, data):
        self._data = data
    def produce(self, out_q):
        while True:
            if self._data:
                out_q.put(self._data)
    def empty(self):
        self._data = None
    def fill(self, data):
        self._data = data
def producer(out_q):
    # while True:
    #     data = [i for i in range(50)]
    #     out_q.put(data)
    data = [i for i in range(50)]
    out_q.put(data)
def consumer(in_q, id):
    data = in_q.get()
    # while data:
    for i in data:
        print('Consumer {}\'s data is {}.'.format(id, i))
        # in_q.empty()
        # data = in_q.get()
q = Queue()
c1 = Thread(target=consumer, args=(q, 'C1'))
c2 = Thread(target=consumer, args=(q, 'C2'))
# dp = DataProducer([i for i in range(20)])
p = Thread(target=producer, args=(q, ))
c1.start()
c2.start()
p.start()