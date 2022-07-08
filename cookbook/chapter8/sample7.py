'''
Calling a Method on a Parent Class
Problem
    You want to invoke a method in a parent class in place of a method that has been
overridden in a subclass.
Solution
    To call a method in a parent (or superclass), use the super() function
'''
class A:
    def __init__(self):
        self.x = 'X'
    def spam(self):
        print('Spam A')
class B(A):
    def __init__(self):
        super().__init__()
        self.y = 'Y'
    def spam(self):
        print('Spam B')
        super().spam()
b = B()
b.spam()
print('x is \'{}\', y is \'{}\' .'.format(b.x, b.y))
print('-' * 80)
class Proxy:
    def __init__(self, obj):
        self._obj = obj
    def __getattr__(self, item):
        return getattr(self._obj, item)
    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            setattr(self._obj, key, value)
p = Proxy(b)
print('x is : {}'.format(p.x))
p.x = 200
p.y = 300
p._m = 100
print('x now is : {}, y is : {},  m is : {}'.format(p.x, p.y, p._m))
print('-' * 80)
class Base:
    def __init__(self):
        print('Base init method !')
class C_A(Base):
    def __init__(self):
        #Base.__init__(self)
        super().__init__()
        print('Class A init !')
class C_B(Base):
    def __init__(self):
        #Base.__init__(self)
        super().__init__()
        print('Class B init !')
class C_C(C_A, C_B):
    def __init__(self):
        #C_A.__init__(self)
        #C_B.__init__(self)
        super().__init__()
        print('Class C init !')
c = C_C()
print(C_C.__mro__)
print('-' * 80)