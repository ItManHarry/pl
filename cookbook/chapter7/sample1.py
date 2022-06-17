'''
Writing Functions That Accept Any Number of Arguments
Problem
    You want to write a function that accepts any number of input arguments.
Solution
    To write a function that accepts any number of positional arguments, use a * argument
'''
def fun1(n1, *args):
    print(args)
    return (n1 + sum(args)) / (1 + len(args))
r = fun1(100, 200, 300, 400, 500)
print(r)
'''
To accept any number of keyword arguments, use an argument that starts with **.
'''
import html
def make_dom(name, value, **attrs):
    key_vals = [' {}="{}"'.format(key, value) for key, value in attrs.items()]
    #key_vals2 = [' %s="%s"' % item for item in attrs.items()]
    #print(''.join(key_vals2))
    attr_str = ''.join(key_vals)
    print(attr_str)
    dom = '<{name}{attrs}>{value}</{name}>'.format(name=name, value=html.escape(value), attrs=attr_str)
    return dom
dom = make_dom('item', 'Albatross', size='large', quantity='6')
print(dom)
'''
If you want a function that can accept both any number of positional and keyword-only
arguments, use * and ** together
'''
def anyparms(*args, **kwargs):
    print(args)
    print(kwargs)
anyparms(1, 2, 3, 4, name='Harry', age=34)
'''
A * argument can only appear as the last positional argument in a function definition.
A ** argument can only appear as the last argument. A subtle aspect of function definitions
is that arguments can still appear after a * argument
Such arguments are known as keyword-only arguments
'''
def x(a, *args, b):
    print(a)
    print(args)
    print(b)
def y(a, *args, b, **kwargs):
    print(a)
    print(args)
    print(b)
    print(kwargs)
x(1, 2, 3, 4, 5, 6, b='100')
y(1, 2, 3, 4, 5, 6, b=1000, x='a', y='b', z='c')