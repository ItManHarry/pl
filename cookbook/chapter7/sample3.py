'''
Attaching Informational Metadata to Function Arguments
Problem
 You’ve written a function, but would like to attach some additional information to the
arguments so that others know more about how a function is supposed to be used.
Solution
 Function argument annotations can be a useful way to give programmers hints about
how a function is supposed to be used.
'''
def add(x:int, y:int)->int:
    return x + y
sum = add(10, 20)
print(sum)
help(add)
print(add.__annotations__)