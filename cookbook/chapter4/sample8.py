'''
Problem
    You want to iterate over items in an iterable, but the first few items aren’t of interest and
you just want to discard them.
Solution
    The itertools module has a few functions that can be used to address this task. The
first is the itertools.dropwhile() function. To use it, you supply a function and an
iterable. The returned iterator discards the first items in the sequence as long as the
supplied function returns True. Afterward, the entirety of the sequence is produced.
'''
import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
with open(os.path.join(basedir, 'files\\db-info.txt')) as f:
    for line in f:
        print(line, end='')
print('')
print('-' * 80)
from itertools import dropwhile, islice
with open(os.path.join(basedir, 'files\\db-info.txt')) as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')
print('')
print('-' * 80)
l = ['a', 'b', 'c', 'd', 1, 2, 3, 4, 5]
for e in islice(l, 4, None):
    print(e)