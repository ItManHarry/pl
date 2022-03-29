'''
栈 ： 后进先出
队列 ：先进先出
'''
# 栈
l = [1, 30, 32, 15, 34]
print(l)
l.append(100)
print(l)
print(l.pop())
print(l)
from collections import deque
d =deque([1, 2, 4, 5])
print(d)
d.append(10)
print(d)
p = d.popleft()
print(p)
print(d)