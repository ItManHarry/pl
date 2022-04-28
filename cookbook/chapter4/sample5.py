'''
Problem
    You want to iterate in reverse over a sequence.
Solution
    Use the built-in reversed() function.
'''
l = [1, 2, 3, 4, 5]
print(l)
for e in reversed(l):
    print(e)
import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
with open(os.path.join(basedir, 'files\\data.txt')) as f:
    for line in f:
        print(line)
print('-' * 80)
with open(os.path.join(basedir, 'files\\data.txt')) as f:
    for line in reversed(list(f)):
        print(line)
print('-' * 80)
'''
Many programmers don’t realize that reversed iteration can be customized on userdefined
classes if they implement the __reversed__() method. For example:
'''
class Countdown:
    def __init__(self, start):
        self.start = start
    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1
    @property
    def forward_n(self):
        return self.__iter__()
    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
    @property
    def reverse_n(self):
        return self.__reversed__()
ct = Countdown(10)
for i in ct.forward_n:
    print(i)
print('' * 80)
for i in ct.reverse_n:
    print(i)