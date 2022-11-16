'''
Writing Decorators That Add Arguments to Wrapped
Functions
Problem
You want to write a decorator that adds an extra argument to the calling signature of
the wrapped function. However, the added argument can’t interfere with the existing
calling conventions of the function.
Solution
Extra arguments can be injected into the calling signature using keyword-only arguments.
'''
from functools import wraps
def option_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling functiong :', func.__name__)
        return func(*args, **kwargs)
    return wrapper
@option_debug
def spam(x, y, z):
    print(x, y, z)
spam(10, 20, 30)
spam(10, 20, 30, debug=True)