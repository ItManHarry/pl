'''
Putting a Wrapper Around a Function
Problem
You want to put a wrapper layer around a function that adds extra processing (e.g.,
logging, timing, etc.).
Solution
If you ever need to wrap a function with extra code, define a decorator function.
'''
import time
from functools import wraps
def time_this(func):
    @wraps(func)
    def do_timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Function {} executed {} seconds!'.format(func.__name__, end - start))
        return result
    return do_timer
@time_this
def count_down(n):
    while n > 0 :
        n -= 1
count_down(10000000)