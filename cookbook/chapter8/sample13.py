'''
Implementing a Data Model or Type System
Problem
    You want to define various kinds of data structures, but want to enforce constraints on
the values that are allowed to be assigned to certain attributes.
Solution
    In this problem, you are basically faced with the task of placing checks or assertions on
the setting of certain instance attributes. To do this, you need to customize the setting
of attributes on a per-attribute basis. To do this, you should use descriptors.
'''
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
class Typed(Descriptor):
    expected_type = type(None)
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected : ' + str(self.expected_type))
        super().__set__(instance, value)
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected > 0')
        super().__set__(instance, value)
class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError("Missed 'size' option")
        super().__init__(name, **opts)
    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('Size must be <' + str(self.size))
        super().__set__(instance, value)
# class for check
class Integer(Typed):
    expected_type = int
class UnsignedInteger(Integer, Unsigned):
    pass
class Float(Typed):
    expected_type = float
class UnsignedFloat(Float, Unsigned):
    pass
class String(Typed):
    expected_type = str
class SizedString(String, MaxSized):
    pass
# define a class using the typed classes
class Stock:
    name = SizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def __repr__(self):
        return 'Stock name : {}, shares : {}, price : {}!'.format(self.name, self.shares, self.price)
# instance test
s = Stock('Apple', 100, 23.5)
print(s)
# s.price = 100
# print(s)
'''
There are some techniques that can be used to simplify the specification of constraints
in classes. One approach is to use a class decorator, like this:
'''
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls
    return decorate
@check_attributes(name=SizedString(size=8),
                  shares=UnsignedInteger,
                  price=UnsignedFloat)
class Stock2:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def __repr__(self):
        return 'Stock name : {}, shares : {}, price : {}!'.format(self.name, self.shares, self.price)
s = Stock2('Micro', 200, 23.45)
print(s)