'''
Problem
    You want to combine many small strings together into a larger string.
Solution
    If the strings you wish to combine are found in a sequence or iterable, the fastest way
to combine them is to use the join() method. For example:
'''
sl = ['Is', 'Chicago', 'Not', 'Chicago']
print(','.join(sl))
'''
Problem
    You want to create a string in which embedded variable names are substituted with a
string representation of a variable’s value.
Solution
    Python has no direct support for simply substituting variable values in strings. However,
this feature can be approximated using the format() method of strings. For example
'''
vm = {'name': 'Jack', 'age': 32}
print('Info : name is {name} age is {age}!'.format(**vm))
print('Name is {name}, age is {age}!'.format(name='Sam', age=25))
print('Name is {}, age is {}!'.format('Tom', 28))
print('Name is {1}, age is {0}!'.format(32, 'Jame'))
s = 'Name is {name}, age is {age}!'
name = 'Jane'
age = 20
print(s.format_map(vars()))
'''
Problem
    You have long strings that you want to reformat so that they fill a user-specified number
of columns.
Solution
    Use the textwrap module to reformat text for output. For example, suppose you have
the following long string:
'''
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
import textwrap
print(s)
print('-' * 80)
print(type(textwrap.fill(s, 70)))
print('-' * 80)
print(textwrap.fill(s, 70))
print('-' * 80)
print(textwrap.fill(s, 40))
print('-' * 80)
print(textwrap.fill(s, 50, initial_indent='  '))
print('-' * 80)
print(textwrap.fill(s, 60, subsequent_indent='  '))
print('-' * 80)
'''
This should be done in the system terminals , or it won't work.
'''
#import os
#cc = os.get_terminal_size()
#print(os.get_terminal_size().columns)
#print(textwrap.fill(s, cc))

