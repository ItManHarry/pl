'''
Preserving Function Metadata When Writing Decorators
Problem
You’ve written a decorator, but when you apply it to a function, important metadata
such as the name, doc string, annotations, and calling signature are lost.
Solution
Whenever you define a decorator, you should always remember to apply the @wraps
decorator from the functools library to the underlying wrapper function.
'''
import time
from functools import wraps
def time_this(func):
    @wraps(func)
    def execute_timer(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Function {} executed for {} seconds.'.format(func.__name__, end - start))
        return result
    return execute_timer
@time_this
def count_down(n):
    while n > 0:
        n -= 1
count_down(1000000)