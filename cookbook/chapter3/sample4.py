'''
Problem
    You need to convert or output integers represented by binary, octal, or hexadecimal
digits.
Solution
    To convert an integer into a binary, octal, or hexadecimal text string, use the bin(),
oct(), or hex() functions, respectively:
'''
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))
print('-' * 80)
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))
print('-' * 80)
x = -1234
print(bin(x))
print(oct(x))
print(hex(x))
print('-' * 80)
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))
