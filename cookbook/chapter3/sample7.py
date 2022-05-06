'''
Problem
    You need to create or file for the floating-point values of infinity, negative infinity, or
NaN (not a number).
Solution
    Python has no special syntax to represent these special floating-point values, but they
can be created using float(). For example
'''
import math

a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)
print('-' * 80)
'''
To file for the presence of these values, use the math.isinf() and math.isnan() functions.
For example:
'''
print(math.isinf(a))
print(math.isinf(b))
print(math.isnan(c))
print('-' * 80)
n = 102
print(math.isnan(n))