'''
Problem
    You need to perform the same operation on many objects, but the objects are contained
in different containers, and you’d like to avoid nested loops without losing the readability
of your code.
Solution
    The itertools.chain() method can be used to simplify this task. It takes a list of
iterables as input, and returns an iterator that effectively masks the fact that you’re really
acting on multiple containers.
'''
from itertools import chain
l1 = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 'c', 'd', 'e']
l3 = [12.3, 34, 35.4, 100.02, 1000]
for i in chain(l1, l2, l3):
    print('Element is : ', i)