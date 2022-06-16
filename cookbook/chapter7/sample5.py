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
print('-' * 80)
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
import math
def distince(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2-x1, y2-y1)
d = distince(points[1], points[0])
print(d)
'''
Now suppose you want to sort all of the points according to their distance from some
other point. The sort() method of lists accepts a key argument that can be used to
customize sorting, but it only works with functions that take a single argument (thus,
distance() is not suitable). Here’s how you might use partial() to fix it
'''
point = (4, 3)
points.sort(key=partial(distince, point))
print(points)
print('-'*80)
def out_result(result, log=None):
    if log is not None:
        print('Got result : {}'.format(result))
        log.debug('Got : %r', result)
def add(x, y):
    return x+y
if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('test')
    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(out_result, log=log))
    p.close()
    p.join()