'''
斐波那契数列
'''
def fab(max):
    n, x, y = 0, 0, 1
    while n < max:
        yield y
        x, y = y, x + y
        n += 1
for i in fab(10):
    print(i)