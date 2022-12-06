'''
Parsing and Analyzing Python Source
Problem
You want to write programs that parse and analyze Python source code.
Solution
Most programmers know that Python can evaluate or execute source code provided in
the form of a string. For example:
'''
x = 12
r = eval('2 + 3*4 + x')
print(r)
exec('for i in range(10): print(i)')
exec('''
for i in range(20): 
    print('i is : ', i)
''')
