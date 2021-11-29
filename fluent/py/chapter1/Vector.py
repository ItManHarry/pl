from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Vector info : X is %r, Y is :%r' %(self.x, self.y)
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)
    def __abs__(self):
        return hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))
v1 = Vector(2, 4)
v2 = Vector(2, 1)
v3 = v1 + v2
print(v3)
v4 = Vector(3, 4)
print(abs(v4))
print(v4 * 3)
print(abs(v4 * 3))