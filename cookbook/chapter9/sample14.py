'''
Capturing Class Attribute Definition Order
Problem
You want to automatically record the order in which attributes and methods are defined
inside a class body so that you can use it in various operations (e.g., serializing, mapping
to databases, etc.).
Solution
Capturing information about the body of class definition is easily accomplished through
the use of a metaclass.
'''
from collections import OrderedDict
# A set of descriptors for various types
class Typed:
    _expected_type = type(None)
    def __init__(self, name=None):
        self._name = name
    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expected ' + str(self._expected_type))
        instance.__dict__[self._name] = value
class Integer(Typed):
    _expected_type = int
class Float(Typed):
    _expected_type = float
class String(Typed):
    _expected_type = str
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)
    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()
class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self,name)) for name in self._order)
# Example use
class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
s = Stock('GOOG',100,490.1)
print(s.name)
print(s.as_csv())