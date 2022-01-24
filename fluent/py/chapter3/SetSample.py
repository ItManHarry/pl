'''
A set is a collection of unique objects. A basic use case is removing duplication
'''
l = ['a', 'b', 'a', 'c', 'b', 'd']
s = set(l)
print(s)
print(list(s))
s1 = {'a', 'b', 'c', 'd', 'a', 'b'}
s2 = {'a', 'b', 'e', 'f', 'g'}
print(s1 & s2)
found = len(s1 & s2)
print(found)
for e in s1:
    print('Element is : ', e)
fs = frozenset(range(10))
print(fs)
from unicodedata import name
us = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(us)