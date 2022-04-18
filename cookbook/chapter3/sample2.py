'''
Problem
    You need to perform accurate calculations with decimal numbers, and don’t want the
small errors that naturally occur with floats.
Solution
    A well-known issue with floating-point numbers is that they can’t accurately represent
all base-10 decimals. Moreover, even simple mathematical calculations introduce small
errors. For example:
>>> a = 4.2
>>> b = 2.1
>>> a + b
6.300000000000001
>>> (a + b) == 6.3
False
>>>
These errors are a “feature” of the underlying CPU and the IEEE 754 arithmetic performed
by its floating-point unit. Since Python’s float data type stores data using the
native representation, there’s nothing you can do to avoid such errors if you write your
code using float instances.
If you want more accuracy (and are willing to give up some performance), you can use
the decimal module:
'''
from decimal import Decimal, localcontext
x = Decimal('1.3')
y = Decimal('1.7')
s = x + y
print(s)
print(x / y)
with localcontext() as ctx:
    ctx.prec = 3
    print(x / y)
with localcontext() as ctx:
    ctx.prec = 20
    print(x / y)