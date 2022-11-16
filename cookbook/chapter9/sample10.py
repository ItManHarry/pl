'''
Applying Decorators to Class and Static Methods
Problem
You want to apply a decorator to a class or static method.
Solution
Applying decorators to class and static methods is straightforward, but make sure that
your decorators are applied after @classmethod or @staticmethod.
'''
import time
from functools import wraps
def time_it(func):
    @wraps(func)
    def exe_time(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Execute for {} seconds.'.format(end-start))
        return result
    return exe_time
class Spam:
    @time_it
    def instance_m(self, n):
        while n > 0:
            n -= 1
    @classmethod
    @time_it
    def class_m(cls, n):
        while n > 0:
            n -= 1
    @staticmethod
    @time_it
    def static_m(n):
        while n > 0:
            n -= 1
s = Spam()
s.instance_m(1000000)
Spam.class_m(10000000)
Spam.static_m(10000000)