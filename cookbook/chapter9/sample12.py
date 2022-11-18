'''
Using Decorators to Patch Class Definitions
Problem
You want to inspect or rewrite portions of a class definition to alter its behavior, but
without using inheritance or metaclasses.
Solution
This might be a perfect use for a class decorator.
'''
def log_get_attribute(cls):
    orig_attribute = cls.__getattribute__

    def new_attribute(self, name):
        print('Getting : ', name)
        return orig_attribute(self, name)
    cls.__getattribute__ = new_attribute
    return cls
@log_get_attribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        print('Spam...')
a = A(40)
a.x
a.spam()
