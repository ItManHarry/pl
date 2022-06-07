'''
Writing Functions That Only Accept Keyword Arguments
Problem
 You want a function to only accept certain arguments by keyword.
Solution
 This feature is easy to implement if you place the keyword arguments after a * argument
or a single unnamed *
'''
def recv(maxsize, *, block):
    print(maxsize)
    print(block)
recv(1, block=500)
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip < m else m
    return m
m1 = minimum(1, 2, 3, 4, -5, 10)
print(m1)
m2 = minimum(1, 2, 3, 4, -5, 10, clip=-10)
print(m2)