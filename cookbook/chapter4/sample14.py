'''
Problem
    You have a nested sequence that you want to flatten into a single list of values.
Solution
    This is easily solved by writing a recursive generator function involving a yield from
statement.
'''
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
items = [1, 2, [3, 4, 5], 6, 7, 8, [9, 10, 11, 12, 13], 100, 200, [1000, 2000]]
print('-' * 80)
for item in flatten(items):
    print('Item is : ', item)
print('-' * 80)
def flatten2(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten2(x):
                yield i
        else:
            yield x
for item in flatten(items):
    print('Item is : ', item)
print('-' * 80)