'''
Making an N-Argument Callable Work As a Callable
with Fewer Arguments
Problem
    You have a callable that you would like to use with some other Python code, possibly as
a callback function or handler, but it takes too many arguments and causes an exception
when called.
Solution
    If you need to reduce the number of arguments to a function, you should use func
tools.partial(). The partial() function allows you to assign fixed values to one or
more of the arguments, thus reducing the number of arguments that need to be supplied
to subsequent calls
'''
def spam(a, b, c, d):
    print(a, b, c, d)
spam(1, 2, 3, 4)
from functools import partial
s1 = partial(spam, 1)
s1(2, 3, 4)
s2 = partial(spam, d=40)
s2(1, 2, 3)
s2(10, 20, 30)
s3 = partial(spam, 2, 3, d=100)
s3(200)