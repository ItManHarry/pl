'''
The class collections.deque is a thread-safe double-ended queue designed for fast
inserting and removing from both ends. It is also the way to go if you need to keep a list
of “last seen items” or something like that, because a deque can be bounded—i.e., created
with a maximum length—and then, when it is full, it discards items from the opposite
end when you append new ones
'''
from collections import deque
'''
The optional maxlen argument sets the maximum number of items allowed in
this instance of deque; this sets a read-only maxlen instance attribute.
'''
dq = deque(range(10), maxlen=10)
print(dq)
'''
Rotating with n > 0 takes items from the right end and prepends them to the
left; when n < 0 items are taken from left and appended to the right.
'''
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
'''
Appending to a deque that is full (len(d) == d.maxlen) discards items from
the other end; note in the next line that the 0 is dropped
'''
dq.appendleft(-1)
dq.appendleft(-2)
print(dq)
dq.append(10)
print(dq)
'''
Adding three items to the right pushes out the leftmost
'''
dq.extend((10, 20, 30))
print(dq)
dq.extendleft([100, 200, 300])
print(dq)