'''
Problem
    Your code for interacting with the latest web authentication scheme has encountered a
singularity and your only solution is to go around it in the complex plane. Or maybe
you just need to perform some calculations using complex numbers.
Solution
    Complex numbers can be specified using the complex(real, imag) function or by
floating-point numbers with a j suffix. For example:
'''
x = complex(5, 9)
y = 3 - 5j
print(x)
print(y)
'''
The real, imaginary, and conjugate values are easy to obtain, as shown here
'''
print('x real : ', x.real)
print('x imaginary : ', x.imag)
print('x conjugate : ', x.conjugate())
print('y real : ', y.real)
print('y imaginary : ', y.imag)
print('y conjugate : ', y.conjugate())
'''
In addition, all of the usual mathematical operators work:
'''
print('x + y : ', x + y)
print('x - y : ', x - y)
print('x * y : ', x * y)
print('x / y : ', x / y)
print('abs x : ', abs(x))
'''
To perform additional complex-valued functions such as sines, cosines, or square roots,
use the cmath module:
'''
import cmath
print('Sin : ', cmath.sin(x))
print('Cos : ', cmath.cos(x))
print('Exp : ', cmath.exp(x))