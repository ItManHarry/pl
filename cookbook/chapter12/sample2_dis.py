import threading
import time
class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

ptimer = PeriodicTimer(5)
ptimer.start()
def count_down(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus : ', nticks)
        nticks -= 1
def count_up(nticks):
    n = 0
    while n < nticks:
        ptimer.wait_for_tick()
        print('T-plus : ', n)
        n += 1
threading.Thread(target=count_down, args=(10,)).start()
threading.Thread(target=count_up, args=(5, )).start()