'''
Problem
    You want to keep a limited history of the last few items seen during iteration or during
some other kind of processing.
Solution
    Keeping a limited history is a perfect use for a collections.deque. For example, the
following code performs a simple text match on a sequence of lines and yields the
matching line along with the previous N lines of context when found
'''
from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
def search2(lines, pattern):
    for line in lines:
        if pattern in line:
            yield line
import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print('Base directory is : ', os.path.join(basedir, 'files\\data.txt'))
with open(os.path.join(basedir, 'files\\data.txt')) as f:
    search_result = list(search(f, 'Python', 5))
    print('Search result : ', search_result)
    print('-' * 80)
    for line, previous_lines in search_result:
        for pline in previous_lines:
            print('Previous line is : ', pline, end='')
        print('')
        print('Line is : ', line,  end='')
        print('-' * 80)
print('-' * 30, 'Search result 2 ', '-' * 30)
with open(os.path.join(basedir, 'files\\data.txt')) as f:
    search_result = list(search2(f, 'Python'))
    print('Search result 2 : ', search_result)
'''
Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and
the queue is full, the oldest item is automatically removed
'''
print('-' * 80)
d = deque(maxlen=3)
d.append(1)
d.append(2)
d.append(3)
print(d)
d.append(4)
print(d)
'''
Although you could manually perform such operations on a list (e.g., appending, deleting,
etc.), the queue solution is far more elegant and runs a lot faster.
More generally, a deque can be used whenever you need a simple queue structure. If
you don’t give it a maximum size, you get an unbounded queue that lets you append
and pop items on either end.
'''
print('-' * 80)
d = deque()
d.append(1)
d.append(2)
d.append(3)
print(d)
d.appendleft(5)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
'''
Problem
    You want to make a list of the largest or smallest N items in a collection.
Solution
    The heapq module has two functions—nlargest() and nsmallest()—that do exactly
what you want.
'''
import heapq
nums = [10, 20, 34, 2, 45, 100, 43, 65, 87, 68, 55, 32, 32, 20]
three_largest = heapq.nlargest(3, nums)
three_smallest = heapq.nsmallest(3, nums)
print('Numbers : ', nums)
print('Three largest elements : ', three_largest)
print('Three smallest elements : ', three_smallest)
'''
Both functions also accept a key parameter that allows them to be used with more
complicated data structures.
'''
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print('Cheap : ', cheap)
print('Expensive : ', expensive)
print('-' * 80)
print('Numbers are : ', nums)
print('Max element : ', max(nums))
print('Min element : ', min(nums))
print('Sorted : ', sorted(nums)[:3])
nums.sort()
print('Numbers are : ', nums)
'''
Problem
    You want to implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation.
Solution
    The following class uses the heapq module to implement a simple priority queue:
'''
class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, priority, item):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
class Item():
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item{!r}'.format(self.name)
q = PriorityQueue()
q.push(1, Item('Jack'))
q.push(5, Item('Sam'))
q.push(3, Item('Jame'))
q.push(6, Item('Harry'))
q.push(1, Item('Jane'))
print(q._queue)
h = []
index = 0
for i in range(5):
    heapq.heappush(h, (-i, i, 'element'+str(i)))
print(h)
heapq.heappush(h, (-8, index, 'write code'))
index += 1
heapq.heappush(h, (-7, index, 'release product'))
index += 1
heapq.heappush(h, (-1, index, 'write spec'))
index += 1
heapq.heappush(h, (-3, index, 'create tests'))
print(h)