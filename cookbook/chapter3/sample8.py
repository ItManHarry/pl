'''
Problem
    You have entered a time machine and suddenly find yourself working on elementarylevel
homework problems involving fractions. Or perhaps you’re writing code to make
calculations involving measurements made in your wood shop.
Solution
    The fractions module can be used to perform mathematical calculations involving
fractions.
'''
from fractions import Fraction
a = Fraction(5, 4)
print('Fraction a : ', a)
b = Fraction(7, 16)
print('Fraction b : ', b)
print('a + b : ', a + b)
print('a - b : ', a - b)
print('a * b : ', a * b)
print('a / b : ', a / b)
c = a * b
print('Numerator : ', c.numerator)
print('Denominator : ', c.denominator)
print('Convert to float : ', float(c))
a = 3.75
f = Fraction(*a.as_integer_ratio())
print('Float to fraction : ', f)
