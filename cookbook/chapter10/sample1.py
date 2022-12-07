'''
Controlling the Import of Everything
Problem
You want precise control over the symbols that are exported from a module or package
when a user uses the from module import * statement.
Solution
Define a variable __all__ in your module that explicitly lists the exported names.
'''
def spam():
    print('spam ...')
def bar():
    print('bar ...')
bath = 42
'''
If you define __all__ as an empty list, then nothing will be exported. An AttributeEr
ror is raised on import if __all__ contains undefined names.
'''
__all__ = ['spam', 'bar']