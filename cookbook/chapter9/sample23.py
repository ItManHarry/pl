'''
Executing Code with Local Side Effects
Problem
You are using exec() to execute a fragment of code in the scope of the caller, but after
execution, none of its results seem to be visible.
Solution
To better understand the problem, try a little experiment. First, execute a fragment of
code in the global namespace:
'''
a = 13
exec('b = a +1')
print(b)
def cal():
    a = 13
    loc = locals()
    exec('c = a + 1')
    c = loc['c']
    print(c)
cal()