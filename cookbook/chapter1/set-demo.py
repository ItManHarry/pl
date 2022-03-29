'''
Problem
    You want to eliminate the duplicate values in a sequence, but preserve the order of the
remaining items.
Solution
    If the values in the sequence are hashable, the problem can be easily solved using a set
and a generator. For example:
'''
def deque(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
l = [1, 2, 3, 2, 20, 1, 30, 3, 42, 21, 32, 34,54, 42, 100]
print('Source list : ', l)
s = set(l)
print('Eliminate duplicate value by using set , the order is changed : ', list(s))
print('After eliminate duplicate values : ', list(deque(l)))
dl = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print('Dictionary list : ', dl)
print('Eliminate duplicate elements : ', list(deque(dl, key=lambda d: (d['x'], d['y']))))
print('Eliminate duplicate keys : ', list(deque(dl, key=lambda d: d['x'])))
'''
Problem
    Your program has become an unreadable mess of hardcoded slice indices and you want
to clean it up.
Solution
    Suppose you have some code that is pulling specific data fields out of a record string
with fixed fields (e.g., from a flat file or similar format):
'''
record = '....................100 .......513.25 ..........'
print(record[20: 32])
print(record[40: 48])
#cost = int(record[20:32]) * float(record[40:48])
#print(cost)
s = slice(2 ,4)
print(l[s])