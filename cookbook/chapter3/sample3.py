'''
Problem
    You need to format a number for output, controlling the number of digits, alignment,
inclusion of a thousands separator, and other details.
Solution
    To format a single number for output, use the built-in format() function. For example:
'''
x = 1234.56789
print(format(x, '.2f'))
print('"', format(x, '>20.3f'), '"')
print('"', format(x, '<20.3f'), '"')
print('"', format(x, '^20.3f'), '"')
print('"', format(x, ',.3f'), '"')
print('Exponential forma : ', format(x, 'e'))
print('Exponential forma : ', format(x, '0.2e'))
print('Use format method : {:,.2f}'.format(x))