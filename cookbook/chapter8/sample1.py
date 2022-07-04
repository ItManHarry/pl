'''
Problem
    You want to change the output produced by printing or viewing instances to something
more sensible.
Solution
    To change the string representation of an instance, define the __str__() and
__repr__() methods
'''
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Pair {0.x!r}, {0.y!r}'.format(self)

    def __str__(self):
        return '{0.x!s}, {0.y!s}'.format(self)

p = Pair(10, 20)
print('{0!r}'.format(p))
print('{}'.format(p))
print(p)
s = 1200.52398
print('{:,.3f}'.format(s))