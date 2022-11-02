'''
Calling a Method on an Object Given the Name As a
String
Problem
You have the name of a method that you want to call on an object stored in a string and
you want to execute the method.
Solution
For simple cases, you might use getattr(), like this
'''
print('{:,.2f}'.format(25008512.5236))
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Base point is ({}, {})'.format(self.x, self.y)
    def distance(self, x, y):
        import math
        return math.hypot(self.x - x, self.y - y)
p = Point(2, 3)
print(p)
print(p.distance(4, 5))
d = getattr(p, 'distance')(0, 0)
print(d)
import operator
d = operator.methodcaller('distance', 0, 0)(p)
print(d)
'''
operator.methodcaller() may be useful if you want to look up a method by name and
supply the same arguments over and over again. For instance, if you need to sort an
entire list of points
'''
points = [
    Point(1, 2),
    Point(3, 0),
    Point(0, 4),
    Point(10, 6),
    Point(25, 32),
    Point(4, 8),
    Point(9, 3)
]
print(points)
points.sort(key=operator.methodcaller('distance', 0, 0))
print(points)
sorted(points, key=operator.methodcaller('distance', 0, 0))
for p in reversed(points):
    print(p)