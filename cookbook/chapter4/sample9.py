'''
Problem
    You want to iterate over all of the possible combinations or permutations of a collection
of items.
Solution
    The itertools module provides three functions for this task. The first of these—iter
tools.permutations()—takes a collection of items and produces a sequence of tuples
that rearranges all of the items into all possible permutations (i.e., it shuffles them into
all possible configurations).
'''
items = ['a', 'b', 'c']
from itertools import combinations, permutations
for p in permutations(items):
    print(p)
'''
If you want all permutations of a smaller length, you can give an optional length argument.
'''
print('-' * 80)
for p in permutations(items, 2):
    print(p)
print('-' * 80)
for c in combinations(items, 3):
    print(c)
for c in combinations(items, 2):
    print(c)