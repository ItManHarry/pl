'''
Defining Anonymous or Inline Functions
Problem
    You need to supply a short callback function for use with an operation such as sort(),
but you don’t want to write a separate one-line function using the def statement. Instead,
you’d like a shortcut that allows you to specify the function “in line.”
Solution
    Simple functions that do nothing more than evaluate an expression can be replaced by
a lambda expression
'''
add = lambda x, y: x + y
print(add(10, 30))
'''
Typically, lambda is used in the context of some other operation, such as sorting or a
data reduction
'''
names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))
'''
You’ve defined an anonymous function using lambda, but you also need to capture the
values of certain variables at the time of definition
Consider the behavior of the following code
'''
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y
print(a(10))
print(b(10))
'''
The problem here is that the value of x used in the lambda expression is a free variable
that gets bound at runtime, not definition time. Thus, the value of x in the lambda
expressions is whatever the value of the x variable happens to be at the time of execution
'''
x = 15
print(a(10))
x = 3
print(a(10))
print(b(10))
'''
If you want an anonymous function to capture a value at the point of definition and
keep it, include the value as a default value, like this
'''
x = 100
a = lambda y, x=x: x + y
x = 200
b = lambda y, x=x: x + y
print(a(100))
print(b(100))
'''
The problem addressed in this recipe is something that tends to come up in code that
tries to be just a little bit too clever with the use of lambda functions. For example,
creating a list of lambda expressions using a list comprehension or in a loop of some
kind and expecting the lambda functions to remember the iteration variable at the time
of definition. For example:
'''
fs = [lambda x: x+n for n in range(5)]
for f in fs:
    print(f(1))
'''
Notice how all functions think that n has the last value during iteration. Now compare
to the following:
'''
fs = [lambda x, n=n: x+n for n in range(5)]
for f in fs:
    print(f(1))
ns = (i for i in range(100) if i % 2 == 0)
for n in ns:
    print('N is : ', n)