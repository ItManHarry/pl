'''
Problem
    You need to perform calculations on large numerical datasets, such as arrays or grids.
Solution
    For any heavy computation involving arrays, use the NumPy library. The major feature
of NumPy is that it gives Python an array object that is much more efficient and better
suited for mathematical calculation than a standard Python list. Here is a short example
illustrating important behavioral differences between lists and NumPy arrays:
'''
# Python list
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
print(l1 * 2)
print(l1 + l2)
print('-' * 80)
import numpy as np
nl1 = np.array([1, 2, 3, 4])
nl2 = np.array([5, 6, 7, 8])
print(nl1)
print(nl1 * 2)
print(nl1 + 10)
print('Numpy array 2 : ', nl2)
print('Numpy array 2 multi 2 : ', nl2*2)
print('-' * 80)
for i in nl1 + nl2:
    print('i is : ', i)
print('-' * 80)
for i in nl1 * nl2:
    print('i is : ', i)
print('-' * 80)
def f(x):
    return 3*x**2 - 2*x + 7
print(f(nl1))
print(f(nl2))
print('-' * 80)
print(np.sqrt(nl1))
print(np.sqrt(nl2))
print('-' * 80)
grid = np.zeros(shape=(10000, 10000), dtype=float)
print(grid)
grid += 10
print('-' * 80)
print(grid)
print('-' * 80)
td = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(td)
print('First row : ', td[0])
print('First column : ', td[:,0])
print(td[0:3, 1:3])
td[0:3, 0:3] += 10
print(td)
rp = np.where(td < 10, td, 10)
print(td)
print(rp)