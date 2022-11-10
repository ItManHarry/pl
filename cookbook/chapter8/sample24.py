'''
Making Classes Support Comparison Operations
Problem
You’d like to be able to compare instances of your class using the standard comparison
operators (e.g., >=, !=, <=, etc.), but without having to write a lot of special methods.
Solution
Python classes can support comparison by implementing a special method for each
comparison operator. For example, to support the >= operator, you define a __ge__()
method in the classes. Although defining a single method is usually no problem, it
quickly gets tedious to create implementations of every possible comparison operator.
The functools.total_ordering decorator can be used to simplify this process. To use
it, you decorate a class with it, and define __eq__() and one other comparison method
(__lt__, __le__, __gt__, or __ge__). The decorator then fills in the other comparison
methods for you.
'''
from functools import total_ordering
class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width

@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()
    @property
    def living_space_feet(self):
        return sum(r.square_feet for r in self.rooms)
    def add_room(self, room):
        self.rooms.append(room)
    def __repr__(self):
        return 'House name {}, living space feet {}, style {}.'.format(self.name, self.living_space_feet, self.style)

    '''
        必须编写至少两个比较函数(eq/lt;gt;le;ge任意一个即可),否则会报ValueError
        Traceback (most recent call last):
          File "D:\Development\Python\workplaces\pl\cookbook\chapter8\sample24.py", line 25, in <module>
            class House:
          File "c:\program files\python38\lib\functools.py", line 187, in total_ordering
            raise ValueError('must define at least one ordering operation: < > <= >=')
        ValueError: must define at least one ordering operation: < > <= >=
    '''
    def __eq__(self, other):
        return self.living_space_feet == other.living_space_feet
    def __lt__(self, other):
        return self.living_space_feet < other.living_space_feet
h1 = House('H1', 'Cape')
h1.add_room(Room('Master bed room', 14, 21))
h1.add_room(Room('Living room', 18, 20))
h1.add_room(Room('Kitchen', 12, 16))
h1.add_room(Room('Office', 12, 12))
h2 = House('H2', 'Ranch')
h2.add_room(Room('Master bed room', 14, 21))
h2.add_room(Room('Living room', 18, 20))
h2.add_room(Room('Kitchen', 12, 16))
h3 = House('H3', 'Split')
h3.add_room(Room('Master bed room', 14, 21))
h3.add_room(Room('Living room', 18, 20))
h3.add_room(Room('Kitchen', 12, 16))
h3.add_room(Room('Office', 12, 16))
h4 = House('H4', 'Cape')
h4.add_room(Room('Master bed room', 14, 21))
h4.add_room(Room('Living room', 18, 20))
h4.add_room(Room('Kitchen', 12, 16))
h4.add_room(Room('Office', 12, 12))
houses = [h1, h2, h3, h4]
for house in houses:
    print('House : ', house)
print('H1 bigger than H2 ? ', 'Yes' if h1 > h2 else 'No')
print('H2 smaller than H3 ? ', 'Yes' if h2 < h3 else 'No')
print('H2 bigger or equal to H1 ? ', 'Yes' if h2 >= h1 else 'No')
print('H1 is as big as H4 ? ', 'Yes' if h1 == h4 else 'No')
print('Biggest house is : ', max(houses))
print('Smallest house is : ', min(houses))