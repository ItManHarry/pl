'''
Enforcing Type Checking on a Function Using a Decorator
Problem
You want to optionally enforce type checking of function arguments as a kind of assertion
or contract.
Solution
Before showing the solution code, the aim of this recipe is to have a means of enforcing
type contracts on the input arguments to a function.
'''
from inspect import signature
from functools import wraps
def typeassert(*ty_args, **ty_kwargs):
    def decorator(func):
        if not __debug__:
            return func
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}!'.format(name, bound_types[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorator
@typeassert(int, int)
def add(x, y):
    return x + y
print(add(10, 20))
print(add(100, 'a'))
@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)
spam(10, 20, 30)
spam(10, 30)
spam(10, 'hello')
spam(10, 'OK', 'Jack')