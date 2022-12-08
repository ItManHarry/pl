'''
Splitting a Module into Multiple Files
Problem
You have a module that you would like to split into multiple files. However, you would
like to do it without breaking existing code by keeping the separate files unified as a
single logical module.
Solution
A program module can be split into separate files by turning it into a package. Consider
the following simple module
'''
class A:
    def spam(self):
        print('A spam!')
class B(A):
    def bar(self):
        print('A bar!')
import s4
a = s4.A()
a.spam()
b = s4.B()
b.bar()
'''
if the A is 'lazy' loaded, there will be something wrong when using
s4.A! Instead , change this into 's4.a.A', and it will work!
'''
# if isinstance(a, s4.A):
if isinstance(a, s4.a.A):
    print('Yes, it is.')
else:
    print('No, it is not.')