'''
Problem
    You have data inside of a sequence, and need to extract values or reduce the sequence
using some criteria.
Solution
    The easiest way to filter sequence data is often to use a list comprehension. For example:
'''
ls = [1, 3, 20, 43, -1, 0, -4, 20, 34]
bz = [n for n in ls if n >= 0]
sz = [n for n in ls if n < 0]
print('Origin list : ', ls)
print('Bigger or equal zero : ', bz)
print('Smaller than zero : ', sz)
'''
One potential downside of using a list comprehension is that it might produce a large
result if the original input is large. If this is a concern, you can use generator expressions
to produce the filtered values iteratively. For example:
'''
print('-' * 80)
bz = (n for n in ls if n >= 0)
sz = (n for n in ls if n < 0)
for i in bz:
    print(i, end=',')
print('')
for i in sz:
    print(i, end=',')
print('')
print('-' * 80)
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False
int_values = list(filter(is_int, values))
print('Int values are : ', int_values)
print('-' * 80)
'''
One variation on filtering involves replacing the values that don’t meet the criteria with
a new value instead of discarding them. For example, perhaps instead of just finding
positive values, you want to also clip bad values to fit within a specified range. This is
often easily accomplished by moving the filter criterion into a conditional expression
like this:
'''
clip_nreg = [n if n > 0 else 0 for n in ls]
clip_preg = [n if n < 0 else 0 for n in ls]
print(clip_nreg)
print(clip_preg)
print('-' * 80)
'''
Another notable filtering tool is itertools.compress(), which takes an iterable and
an accompanying Boolean selector sequence as input. As output, it gives you all of the
items in the iterable where the corresponding element in the selector is True. This can
be useful if you’re trying to apply the results of filtering one sequence to another related
sequence. For example, suppose you have the following two columns of data:
'''
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
five = [n > 5 for n in counts]
print(addresses)
print(five)
from itertools import compress
print(list(compress(addresses, five)))