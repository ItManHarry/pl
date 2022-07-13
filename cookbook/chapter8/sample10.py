'''
Using Lazily Computed Properties
Problem
    You’d like to define a read-only attribute as a property that only gets computed on access.
However, once accessed, you’d like the value to be cached and not recomputed on each
access.
Solution
    An efficient way to define a lazy attribute is through the use of a descriptor class
'''
class LazyProperty:
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @LazyProperty
    def area(self):
        print('Compute the circle area...')
        return math.pi * self.radius ** 2
    @LazyProperty
    def perimeter(self):
        print('Compute the circle perimeter...')
        return 2 * math.pi * self.radius
c = Circle(4.0)
print('Circle radius is : {:.2f}, area is {:.4f}, perimeter is {:.4f}'.format(c.radius, c.area, c.perimeter))
print('Circle radius is : {:.2f}, area is {:.4f}, perimeter is {:.4f}'.format(c.radius, c.area, c.perimeter))
print('Circle radius is : {:.2f}, area is {:.4f}, perimeter is {:.4f}'.format(c.radius, c.area, c.perimeter))
print('Circle radius is : {:.2f}, area is {:.4f}, perimeter is {:.4f}'.format(c.radius, c.area, c.perimeter))
'''
In many cases, the whole point of having a lazily computed attribute is to improve
performance. For example, you avoid computing values unless you actually need them
somewhere. The solution shown does just this, but it exploits a subtle feature of descriptors
to do it in a highly efficient way.
As shown in other recipes (e.g., Recipe 8.9), when a descriptor is placed into a class
definition, its __get__(), __set__(), and __delete__() methods get triggered on attribute
access. However, if a descriptor only defines a __get__() method, it has a much weaker 
binding than usual. In particular, the __get__() method only fires if the attribute
being accessed is not in the underlying instance dictionary.
The lazyproperty class exploits this by having the __get__() method store the computed
value on the instance using the same name as the property itself. By doing this,
the value gets stored in the instance dictionary and disables further computation of the
property.
'''