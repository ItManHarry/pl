'''
Enforcing Coding Conventions in Classes
Problem
Your program consists of a large class hierarchy and you would like to enforce certain
kinds of coding conventions (or perform diagnostics) to help maintain programmer
sanity.
Solution
If you want to monitor the definition of classes, you can often do it by defining a
metaclass. A basic metaclass is usually defined by inheriting from type and redefining
its __new__() method or __init__() method.
'''
class MyMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        # clsname is name of class being defined
        # bases is tuple of base classes
        # clsdict is class dictionary
        return super().__new__(cls, clsname, bases, clsdict)
    def __init__(self, clsname, bases, clsdict):
        return super().__init__(clsname, bases, clsdict)
class Root(metaclass=MyMeta):
    pass
class A(Root):
    pass
class B(Root):
    pass
print('-' * 80)