'''
Determining If a Thread Has Started
Problem
    You’ve launched a thread, but want to know when it actually starts running.
Solution
    A key feature of threads is that they execute independently and nondeterministically.
This can present a tricky synchronization problem if other threads in the program need
to know if a thread has reached a certain point in its execution before carrying out
further operations. To solve such problems, use the Event object from the threading
library.
    Event instances are similar to a “sticky” flag that allows threads to wait for something
to happen. Initially, an event is set to 0. If the event is unset and a thread waits on the
event, it will block (i.e., go to sleep) until the event gets set. A thread that sets the event
will wake up all of the threads that happen to be waiting (if any). If a thread waits on an
event that has already been set, it merely moves on, continuing to execute.
'''
from threading import Thread, Event
import time
def count_down(n, started_event):
    print('Counting down is starting...')
    started_event.set()
    while n > 0:
        print('T-minus : ', n)
        n -= 1
        time.sleep(3)
started_event = Event()
t = Thread(target=count_down, args=(5, started_event))
t.start()
started_event.wait()
print('Counting down is running')