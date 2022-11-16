'''
Defining Decorators As Classes
Problem
You want to wrap functions with a decorator, but the result is going to be a callable
instance. You need your decorator to work both inside and outside class definitions.
Solution
To define a decorator as an instance, you need to make sure it implements the
__call__() and __get__() methods.
'''
import types
from functools import wraps
class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        print('method of the decorator class, do whatever you want!')
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)
@Profiled
def add(x, y):
    return x + y
class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)
print(add(10, 20))
print(add(50, 60))
print(add.ncalls)
s = Spam()
s.bar(100)
s.bar(200)
s.bar(300)
print(Spam.bar.ncalls)