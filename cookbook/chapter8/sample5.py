'''
Encapsulating Names in a Class
Problem
    You want to encapsulate “private” data on instances of a class, but are concerned about
Python’s lack of access control.
Solution
    Rather than relying on language features to encapsulate data, Python programmers are
expected to observe certain naming conventions concerning the intended usage of data
and methods. The first convention is that any name that starts with a single leading
underscore (_) should always be assumed to be internal implementation
'''
class A:
    def __init__(self):
        self._internal = 'A'
        self.__private = 'P-A'
        self.public = 'PUB-A'

    def public_method(self):
        print('Public method A')

    def _internal_method(self):
        print('Internal method A')
        self.__private_method()

    def __private_method(self):
        print('Private method A')
class B(A):
    def __init__(self):
        super().__init__()
        self._internal = 'B'
        self.__private = 'P-B'
        self.public = 'PUB-B'

    def public_method(self):
        print('Public method B')
    def _internal_method(self):
        print('Internal method B')
        self.__private_method()
    def __private_method(self):
        print('Private method B')
b = B()
print('Public variable : {0.public}, internal variable: {0._internal}'.format(b))
'''
Traceback (most recent call last):
  File "D:/Development/Python/workplaces/pl/cookbook/chapter8/sample5.py", line 41, in <module>
    print('Private variable : ', b.__priave)
AttributeError: 'B' object has no attribute '__priave'
'''
# print('Private variable : ', b.__private)
b.public_method()
print('-' * 80)
b._internal_method()
'''
Traceback (most recent call last):
  File "D:/Development/Python/workplaces/pl/cookbook/chapter8/sample5.py", line 50, in <module>
    b.__private_method()
AttributeError: 'B' object has no attribute '__private_method'
'''
# b.__private_method()