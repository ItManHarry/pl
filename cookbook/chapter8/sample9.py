'''
Creating a New Kind of Class or Instance Attribute
Problem
    You want to create a new kind of instance attribute type with some extra functionality,
such as type checking.
Solution
    If you want to create an entirely new kind of instance attribute, define its functionality
in the form of a descriptor class
'''
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Value must be an int')
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        del instance.__dict__[self.name]
'''
A descriptor is a class that implements the three core attribute access operations (get,
set, and delete) in the form of __get__(), __set__(), and __delete__() special methods.
These methods work by receiving an instance as input. The underlying dictionary
of the instance is then manipulated as appropriate.
'''
class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y
p = Point(100, 200)
print(p.x)
print(p.y)
p.x = 500
print(p.x)
# p.y = 24.5
print('-' * 80)
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Type wrong! Expect :', str(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]
def typeassert(**kwargs):
    def decorator(cls):
        for name, expected_type in kwargs.items():
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorator
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def __repr__(self):
        return 'Stock info > name : {} ; Shares : {:,} ; Price : {:,.2f}'.format(self.name, self.shares, self.price)
s = Stock('Apple', 10500, 203.9256)
print(s)
s = Stock('Micro', 15, 1000.0)
print(s)
print('-' * 80)