'''
Problem
    You need to process items in an iterable, but for whatever reason, you can’t or don’t want
to use a for loop.
Solution
    To manually consume an iterable, use the next() function and write your code to catch
the StopIteration exception
'''
import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
with open(os.path.join(basedir, 'files\\data.txt')) as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        print('Reading finished ...')
print('-' * 80)
with open(os.path.join(basedir, 'files\\data.txt')) as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')
print('-' * 80)
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lt = iter(l)
try:
    while True:
        e = next(lt)
        print('Element : ', e)
except StopIteration:
    print('No more elements!')
print('-' * 80)
lt = iter(l)
while True:
    e = next(lt, None)
    if e is None:
        print('No more elements!!!')
        break
    print('Element : ', e)
