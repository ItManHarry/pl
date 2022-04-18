'''
Problem
    You want to round a floating-point number to a fixed number of decimal places.
Solution
    For simple rounding, use the built-in round(value, ndigits) function. For example
'''
n = 12.23
print(round(n, 1))
n = 12.356
print(round(n, 2))
n = -1.274
print(round(n, 2))
n = 1.25364
print(round(n, 3))
n = 1632273
print(round(n, -2))
'''
When a value is exactly halfway between two choices, the behavior of round is to round
to the nearest even digit. That is, values such as 1.5 or 2.5 both get rounded to 2.
'''
print(round(1.5), round(2.5))
n = 1.23456
print(format(n, '.2f'))
print('{:.3f}'.format(n))
n = 125632.5623
print('{:.3f}'.format(n))
'''
Also, resist the urge to round floating-point numbers to “fix” perceived accuracy problems.
For example, you might be inclined to do this:
'''
n1 = 1.1
n2 = 3.2
n = n1 + n2
print(round(n, 1))
n = 1.5002
print(round(n, 2))