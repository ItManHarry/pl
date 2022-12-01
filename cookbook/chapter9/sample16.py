'''
Enforcing an Argument Signature on *args and
**kwargs
Problem
You’ve written a function or method that uses *args and **kwargs, so that it can be
general purpose, but you would also like to check the passed arguments to see if they
match a specific function calling signature.
Solution
For any problem where you want to manipulate function calling signatures, you should
use the signature features found in the inspect module. Two classes, Signature and
Parameter, are of particular interest here
'''
from inspect import Signature, Parameter
params = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
          Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
sig = Signature(params)
print(sig)
'''
Once you have a signature object, you can easily bind it to *args and **kwargs using
the signature’s bind() method
'''
def func(*args, **kwargs):
    bind_values = sig.bind(*args, **kwargs)
    for name, value in bind_values.arguments.items():
        print('Parameter name {}, value {}.'.format(name, value))
func(1, 2, z=3)
func(1)
func(1, z=3)
func(y=1, x=2)
'''
Traceback (most recent call last):
  File "D:\Development\Python\workplaces\pl\cookbook\chapter9\sample16.py", line 31, in <module>
    func(1, 2, 3, 4)
  File "D:\Development\Python\workplaces\pl\cookbook\chapter9\sample16.py", line 24, in func
    bind_values = sig.bind(*args, **kwargs)
  File "c:\program files\python38\lib\inspect.py", line 3025, in bind
    return self._bind(args, kwargs)
  File "c:\program files\python38\lib\inspect.py", line 2951, in _bind
    raise TypeError(
TypeError: too many positional arguments
'''
# func(1, 2, 3, 4)
'''
Traceback (most recent call last):
  File "D:\Development\Python\workplaces\pl\cookbook\chapter9\sample16.py", line 44, in <module>
    func(1, x=3, y=4)
  File "D:\Development\Python\workplaces\pl\cookbook\chapter9\sample16.py", line 24, in func
    bind_values = sig.bind(*args, **kwargs)
  File "c:\program files\python38\lib\inspect.py", line 3025, in bind
    return self._bind(args, kwargs)
  File "c:\program files\python38\lib\inspect.py", line 2964, in _bind
    raise TypeError(
TypeError: multiple values for argument 'x'
'''
# func(1, x=3, y=4)
print('-' * 80)
def make_sig(*names):
    params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(params)
class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            print('Parameter name {} , value {}.'.format(name, value))
class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')
class Point(Structure):
    __signature__ = make_sig('x', 'y')
import inspect
print(inspect.signature(Stock))
print(inspect.signature(Point))

