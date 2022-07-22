'''
Defining an Interface or Abstract Base Class
Problem
    You want to define a class that serves as an interface or abstract base class from which
you can perform type checking and ensure that certain methods are implemented in
subclasses.
Solution
    To define an abstract base class, use the abc module.
'''
from abc import ABCMeta, abstractmethod
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass
    @abstractmethod
    def write(self, data):
        pass