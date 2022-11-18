'''
Using a Metaclass to Control Instance Creation
Problem
You want to change the way in which instances are created in order to implement singletons,
caching, or other similar features.
Solution
As Python programmers know, if you define a class, you call it like a function to create
instances.
'''
class Spam:
    def __init__(self, name):
        self.name = name
s = Spam('AAA')
'''
If you want to customize this step, you can do it by defining a metaclass and reimplementing
its __call__() method in some way. To illustrate, suppose that you didn’t want
anyone creating instances at all:
'''
class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('Can\'t instantiate directly.')
class N(metaclass=NoInstance):
    @staticmethod
    def grok(x):
        print('Grok : ', x)
N.grok(100)
print('-' * 80)
'''
Traceback (most recent call last):
  File "D:\Development\Python\workplaces\pl\cookbook\chapter9\sample13.py", line 27, in <module>
    n = N()
  File "D:\Development\Python\workplaces\pl\cookbook\chapter9\sample13.py", line 21, in __call__
    raise TypeError('Can\'t instantiate directly.')
TypeError: Can't instantiate directly.
'''
# n = N()
'''
Now, suppose you want to implement the singleton pattern (i.e., a class where only one
instance is ever created). That is also relatively straightforward, as shown here:
'''
class Singleton(type):
    def __init__(self, *args, **kwargs):
        print('Singleton init 1 ...')
        self._instance = None
        print('Singleton init 2 ...')
        super().__init__(*args, **kwargs)
        print('Singleton init 3 ...')
    def __call__(self, *args, **kwargs):
        print('Singleton call ...')
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
            return self._instance
        else:
            return self._instance
class S(metaclass=Singleton):
    def __init__(self):
        print('Creating S instance ...')
s1 = S()
s2 = S()
print('s1 is s2 ? ', s1 is s2)
s3 = S()
print('s1 is s3 ? ', s1 is s3)
print('s2 is s3 ? ', s2 is s3)
'''
create cached instances
'''
print('-' * 80)
import weakref
class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()
    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj
class C(metaclass=Cached):
    def __init__(self, name):
        print('Creating class : {}'.format(name))
        self.name = name
c1 = C('Guido')
c2 = C('Diana')
print('c1 is c2 : ', c1 is c2)
c3 = C('Guido')
print('c1 is c3 : ', c1 is c3)