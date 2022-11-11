'''
Unwrapping a Decorator
Problem
A decorator has been applied to a function, but you want to “undo” it, gaining access to
the original unwrapped function.
Solution
Assuming that the decorator has been implemented properly using @wraps (see
Recipe 9.2), you can usually gain access to the original function by accessing the __wrap
ped__ attribute.
'''
import time
from functools import wraps
def time_this(func):
    @wraps(func)
    def exe_timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Function {} executed for {} seconds.'.format(func.__name__, end - start))
        return result
    return exe_timer
@time_this
def count_down(n):
    while n > 0:
        n -= 1
count_down(1000000)
c_d = count_down.__wrapped__
print('-' * 80)
c_d(100000)
print('Finished')