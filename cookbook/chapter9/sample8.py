'''
Defining Decorators As Part of a Class
Problem
You want to define a decorator inside a class definition and apply it to other functions
or methods.
Solution
Defining a decorator inside a class is straightforward, but you first need to sort out the
manner in which the decorator will be applied. Specifically, whether it is applied as an
instance or a class method.
'''
from functools import wraps
class A:
    def decrator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Class decorator 1')
            return func(*args, **kwargs)
        return wrapper
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Class decorator 2')
            return func(*args, **kwargs)
        return wrapper
a = A()
@a.decrator1
def meth1():
    pass
@A.decorator2
def meth2():
    pass
meth1()
meth2()