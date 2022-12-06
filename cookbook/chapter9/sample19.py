'''
Initializing Class Members at Definition Time
Problem
You want to initialize parts of a class definition once at the time a class is defined, not
when instances are created.
Solution
Performing initialization or setup actions at the time of class definition is a classic use
of metaclasses. Essentially, a metaclass is triggered at the point of a definition, at which
point you can perform additional steps.
'''
import operator
class StructTupleMeta(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i, name in enumerate(self._fields):
            setattr(self, name, property(operator.itemgetter(i)))
class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required!'.format(len(cls._fields)))
        return super().__new__(cls, args)
class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']
    def __repr__(self):
        return 'Stock name {}, shares {} price {}!'.format(self.name, self.shares, self.price)
class Point(StructTuple):
    _fields = ['x', 'y']
    def __repr__(self):
        return 'Point x is {}, y is {}!'.format(self.x, self.y)
s = Stock('DEL', 50, 90.1)
print(s)
p = Point(10, 20)
print(p)
ps = [Point(i*10, i*20) for i in range(5)]
for i, p in enumerate(ps):
    print(i+1, p)