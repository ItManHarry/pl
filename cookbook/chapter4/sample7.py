'''
Problem
    You want to take a slice of data produced by an iterator, but the normal slicing operator
doesn’t work.
Solution
    The itertools.islice() function is perfectly suited for taking slices of iterators and
generators.
'''
def count(n):
    while True:
        yield n
        n += 1
c = count(0)
'''
    print(c[10: 20])
    Traceback (most recent call last):
  File "D:/Development/Python/workplaces/pl/cookbook/chapter4/sample7.py", line 14, in <module>
    print(c[10: 20])
TypeError: 'generator' object is not subscriptable
'''
import itertools
for e in itertools.islice(c, 10, 20):
    print(e)
