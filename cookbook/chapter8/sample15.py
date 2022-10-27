'''
Delegating Attribute Access
Problem
You want an instance to delegate attribute access to an internally held instance possibly
as an alternative to inheritance or in order to implement a proxy.
Solution
Simply stated, delegation is a programming pattern where the responsibility for implementing
a particular operation is handed off (i.e., delegated) to a different object.
'''
class A:
    def spam(self, x):
        print('A spam -> ', x)

    def foo(self, x):
        print('A foo ->', x)
class B:
    def __init__(self):
        self._o = A()

    def spam(self, x):
        return self._o.spam(x)

    def foo(self, x):
        return self._o.foo(x)

    def bar(self):
        print('B method bar')

b = B()
b.spam(100)
b.foo(100)
b.bar()
print('-' * 80)
'''
If there are only a couple of methods to delegate, writing code such as that just given is
easy enough. However, if there are many methods to delegate, an alternative approach
is to define the __getattr__() method
'''
class C:
    def __init__(self):
        self._o = A()
    def bar(self):
        print('C method bar')
    def __getattr__(self, name):
        return getattr(self._o, name)
c = C()
c.bar()
c.spam(200)
c.foo(200)
print('-' * 80)
class Proxy:
    def __init__(self, o):
        self._o = o

    def __getattr__(self, item):
        print('Get attribute : ', item)
        return getattr(self._o, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            print('set attribute :', key, ' value is :', value)
            setattr(self._o, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            super().__delattr__(item)
        else:
            print('Delete attribute : ', item)
            delattr(self._o, item)
class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('Spam bar : ', self.x, y)

s = Spam(2)
p = Proxy(s)
p.bar(3)
p.x = 10
p.bar(3)
