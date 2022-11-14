'''
Defining a Decorator That Takes an Optional Argument
Problem
You would like to write a single decorator that can be used without arguments, such as
@decorator, or with optional arguments, such as @decorator(x,y,z). However, there
seems to be no straightforward way to do it due to differences in calling conventions
between simple decorators and decorators taking arguments.
Solution
Here is a variant of the logging code shown in Recipe 9.5 that defines such a decorator:
'''
from functools import partial, wraps
def logged(func=None, *, level=0, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    l_name = name if name else func.__name__
    l_message = message if message else func.__name__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Name {} , message {}, level {}.'.format(l_name, l_message, level))
        return func(*args, **kwargs)
    return wrapper
@logged
def add(x, y):
    return x + y
@logged(level=5, name='L5 Test')
def spam():
    print('Spam')
add(5, 10)
spam()