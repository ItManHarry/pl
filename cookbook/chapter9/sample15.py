'''
Defining a Metaclass That Takes Optional Arguments
Problem
You want to define a metaclass that allows class definitions to supply optional arguments,
possibly to control or configure aspects of processing during type creation.
Solution
When defining classes, Python allows a metaclass to be specified using the metaclass
keyword argument in the class statement.
'''
from abc import ABCMeta, abstractmethod
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass
    @abstractmethod
    def writhe(self, data):
        pass
class MyMeta(type):
    @classmethod
    def __prepare__(metacls, name, bases, *, debug=False, synchronize=False):
        print('__prepare__ method.')
        return super().__prepare__(name, bases)
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        print('__new__ method.')
        return super().__new__(cls, name, bases, ns)
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        print('__init__ method.')
        super().__init__(name, bases, ns)
class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    pass
s = Spam()