def gen(n):
    for i in range(n):
        yield i * i
g = gen(5)
print(g)
for i in g:
    print('i : ', i)
print('-' * 80)
l = [i * i for i in range(5)]
for i in l:
    print('i : ', i)
'''
列表推导式对比生成器
'''
print('-' * 80)
from time import time
import sys
bt = time()
l = [i for i in range(100000000)]
et = time()
print('开始时间 : ', bt, ', 结束时间 : ', et, '耗时 : ', et - bt, ', 占用空间 : ', sys.getsizeof(l))
bt = time()
g = (i for i in range(100000000))
# l = list(g)
et = time()
print('开始时间 : ', bt, ', 结束时间 : ', et, '耗时 : ', et - bt, ', 占用空间 : ', sys.getsizeof(g))