'''
Creating Managed Attributes
Problem
    You want to add extra processing (e.g., type checking or validation) to the getting or
setting of an instance attribute.
Solution
    A simple way to customize access to an attribute is to define it as a “property.”
'''
import math


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.set_last_name(last_name)
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expect a string !')
        self._first_name = value
    @first_name.deleter
    def first_name(self):
        raise AttributeError('Can\'t delete the property!')
    def get_last_name(self):
        return self._last_name
    def set_last_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expect a string !')
        self._last_name = value
    def del_last_name(self):
        raise AttributeError('Can\'t delete the property')
    last_name = property(get_last_name, set_last_name, del_last_name)

p = Person('Jack', 'Cheng')
print('First name : ', p.first_name)
p.first_name = 'Tom'
print('First name changed to : ', p.first_name)
try:
    del p.first_name
except:
    print('Exception occurred !!')
print('Last name is : ', p.last_name)
'''
In the preceding code, there are three related methods, all of which must have the same
name. The first method is a getter function, and establishes first_name as being a
property. The other two methods attach optional setter and deleter functions to the
first_name property. It’s important to stress that the @first_name.setter and
@first_name.deleter decorators won’t be defined unless first_name was already established
as a property using @property.
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
c = Circle(3)
print('Circle area is : ', c.area)
print('Circle perimeter is : ', c.perimeter)