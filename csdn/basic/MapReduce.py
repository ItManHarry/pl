x = [1, 3, 5, 7, 20, 21, 32]
def f(x):
    return x ** 3
m = map(f, x)
print(type(m))
print('List is : ', x)
print(list(m))
# 计算圆面积
rs = [1, 2, 3, 4, 5, 6]
def circle(r):
    return 3.14 * r ** 2
cs = map(circle, rs)
print('Rs is : ', rs)
print('Cs is : ', tuple(cs))
from functools import reduce
def m(x, y):
    return x if x > y else y
l = [10, 30, 450, 400, 200,490, 500, 1002]
r = reduce(m, l)
print('Max element is : ', r)
# 计算数的阶乘
def r(n):
    return reduce(lambda x, y: x * y, range(1, n+1))
print(r(6))
