'''
Problem
    You want to iterate over the items contained in more than one sequence at a time.
Solution
    To iterate over more than one sequence simultaneously, use the zip() function.
'''
xs = [16, 38, 40, 11, 43, 53, 100, 200]
ys = [106, 380, 400, 101, 403]
for x, y in zip(xs, ys):
    print(x, y)
print('-' * 80)
from itertools import zip_longest
for x, y in zip_longest(xs, ys):
    print(x, y)
print('-' * 80)
'''
zip() is commonly used whenever you need to pair data together. For example, suppose
you have a list of column headers and column values like this
'''
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
for name, val in zip(headers, values):
    print(name, '=', val)
print('-' * 80)
'''
It’s less common, but zip() can be passed more than two sequences as input. For this
case, the resulting tuples have the same number of items in them as the number of input
sequences.
'''
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)
'''
Last, but not least, it’s important to emphasize that zip() creates an iterator as a result.
If you need the paired values stored in a list, use the list() function.
'''
print('-' * 80)
l = list(zip(headers, values))
print(l)