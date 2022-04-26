'''
Problem
    You want to implement a custom iteration pattern that’s different than the usual builtin
functions (e.g., range(), reversed(), etc.).
Solution
    If you want to implement a new kind of iteration pattern, define it using a generator
function.
'''
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step
for f in frange(0, 4, 0.5):
    print(f)
l = list(frange(0, 2, 0.25))
print(l)