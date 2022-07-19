'''
Simplifying the Initialization of Data Structures
Problem
    You are writing a lot of classes that serve as data structures, but you are getting tired of
writing highly repetitive and boilerplate __init__() functions.
Solution
    You can often generalize the initialization of data structures into a single __init__()
function defined in a common base class.
'''
import math


class Structure:
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expect {} arguments!'.format(len(self._fields)))
        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))
class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    def __repr__(self):
        return 'Stock name : {}, shares : {:.2f}, price : {:.2f}'.format(self.name, self.shares, self.price)
class Point(Structure):
    _fields = ['x', 'y']
class Circle(Structure):
    _fields = ['radius']
    @property
    def area(self):
        return math.pi * self.radius ** 2
stock = Stock('Apple', 50, 91.1)
print(stock)
point = Point(10, 20)
circle = Circle(4.5)
print(circle.area)
stock = Stock(name='Micro', shares=200, price=500)
print(stock)
print('-' * 80)
class DataStructure:
    _fields = []
    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Need {} arguments!'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError('Duplicate values for {} : '.format(','.join(kwargs)))
class Container(DataStructure):
    _fields = ['length', 'width', 'height']
    @property
    def capacity(self):
        return self.length * self.width * self.height
c = Container(100, 20, 20, ship='A001')
print(c.capacity)
print(c.ship)