'''
Defining a Decorator with User Adjustable Attributes
Problem
You want to write a decorator function that wraps a function, but has user adjustable
attributes that can be used to control the behavior of the decorator at runtime.
Solution
Here is a solution that expands on the last recipe by introducing accessor functions that
change internal variables through the use of nonlocal variable declarations. The accessor
functions are then attached to the wrapper function as function attributes
'''
from functools import wraps, partial
import time
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func
def time_dec(level=0, name=None, message=None):
    def time_exe(func):
        f_n = name if not name else func.__name__
        f_m = message if not message else func.__name__
        @wraps(func)
        def do_timer(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print('Function name {}, level {}, message {} Spend time : {} seconds'.format(f_n, level, f_m, end-start))
            return result
        @attach_wrapper(do_timer)
        def set_level(new_level):
            nonlocal level
            level = new_level
        @attach_wrapper(do_timer)
        def set_message(new_message):
            nonlocal f_m
            f_m = new_message
        return do_timer
    return time_exe
@time_dec(1, 'TTT')
def count_down(n):
    while n > 0:
        n -= 1
count_down.set_level(5)
count_down.set_message('MESSAGE CHANGED...')
count_down(100000)