'''
Problem
    You have multiple dictionaries or mappings that you want to logically combine into a
single mapping to perform certain operations, such as looking up values or checking
for the existence of keys.
Solution
    Suppose you have two dictionaries:
        a = {'x': 1, 'z': 3 }
        b = {'y': 2, 'z': 4 }
Now suppose you want to perform lookups where you have to check both dictionaries
(e.g., first checking in a and then in b if not found). An easy way to do this is to use the
ChainMap class from the collections module.
'''
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
from collections import ChainMap
c = ChainMap(b, a)
print('a : ', a)
print('b : ', b)
print('c : ', c)
for k, v in c.items():
    print('Key is : ', k, ', value : ', v)