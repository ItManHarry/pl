'''
Starting and Stopping Threads
Problem
    You want to create and destroy threads for concurrent execution of code.
Solution
    The threading library can be used to execute any Python callable in its own thread. To
do this, you create a Thread instance and supply the callable that you wish to execute
as a target.
'''
import time
def count_down(id, n):
    while n > 0:
        print('{}, minus :{}'.format(id, n))
        n -= 1
        time.sleep(1)
from threading import Thread
t = Thread(target=count_down, args=('Single', 10))
# t.start()
# print('Create 5 threads...')
# ts = [Thread(target=count_down, args=('Thread-'+str(i), i * 10)) for i in range(5)]
# for t in ts:
#     t.start()
def do_print():
    for i in range(5):
        print('Print : ', i)
# t = Thread(target=do_print, daemon=True)
# t.start()
'''
If you want to be able to terminate threads, the thread must be programmed to poll for
exit at selected points.
'''
class CountTask:
    def __init__(self):
        self._run = True
    def terminate(self):
        self._run = False
    def start(self, n):
        while self._run and n > 0:
            print('Count down : ', n)
            n -= 1
            '''
            if n == 3 , the thread will terminated.
            '''
            if n == 3:
                self._run = False
            time.sleep(2)
c = CountTask()
t = Thread(target=c.start, args=[10])
t.start()
# print('Count class started to count number...')
# c.terminate()
# t.join()
# print('Count thread terminated by the class method...')