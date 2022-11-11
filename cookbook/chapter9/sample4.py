'''
Defining a Decorator That Takes Arguments
Problem
You want to write a decorator function that takes arguments.
Solution
Let’s illustrate the process of accepting arguments with an example. Suppose you want
to write a decorator that adds logging to a function, but allows the user to specify the
logging level and other details as arguments.
'''
from functools import wraps
import time
def time_dec(name=None, message=None):
    def time_exe(func):
        dec_name = name if name else func.__name__
        dec_message = message if message else func.__name__
        @wraps(func)
        def do_time(*args, **kwargs):
            print('Name is : ', name)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print('Function \'{}\' execute for {} seconds. The message is \'{}\'!'.format(dec_name, (end - start), dec_message))
            return result
        return do_time
    return time_exe
@time_dec('CountDownFunction', 'it is a test wrapper function')
def count_down(n):
    while n > 0:
        n -= 1
count_down(1100000)
@time_dec()
def count_up(n):
    b = 0
    while b < n:
        b += 1
count_up(100000)
