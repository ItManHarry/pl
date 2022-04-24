'''
Problem
    You need to perform matrix and linear algebra operations, such as matrix multiplication,
finding determinants, solving linear equations, and so on.
Solution
    The NumPy library has a matrix object that can be used for this purpose. Matrices are
somewhat similar to the array objects described in Recipe 3.9, but follow linear algebra
rules for computation. Here is an example that illustrates a few essential features:
'''
import numpy as np
m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print('m is : ', m)
'''
transpose
'''
print('Transpose m : ', m.T)
'''
Inverse
'''
print('Inverse m : ', m.I)
'''
Create a vector and multiply
'''
v = np.matrix([[2], [3], [4]])
print('v is : ', v)
print(m * v)
