'''
Problem
    You want to make a dictionary that maps keys to more than one value (a so-called
“multidict”).
Solution
    A dictionary is a mapping where each key is mapped to a single value. If you want to
map keys to multiple values, you need to store the multiple values in another container
such as a list or set.
'''
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(13)
d['a'].append(23)
d['a'].append(34)
d['b'].append(10)
d['b'].append(100)
d['b'].append(150)
for k, v in d.items():
    print('Key is : ', k, ', value is : ', v)
print('-' * 80)
d = defaultdict(set)
d['a'].add(10)
d['a'].add(10)
d['a'].add(150)
d['a'].add(352)
d['a'].add(680)
d['a'].add(79)
d['b'].add(100)
d['b'].add(1000)
d['b'].add(10000)
d['b'].add(100000)
for k, v in d.items():
    print('Key is : ', k, ', value is : ', v)
print('-' * 80)
d = {}
d.setdefault('a', []).append(10)
d.setdefault('a', []).append(110)
d.setdefault('a', []).append(120)
d.setdefault('b', []).append(100)
d.setdefault('b', []).append(200)
d.setdefault('b', []).append(300)
d.setdefault('b', []).append(400)
for k, v in d.items():
    print('Key is : ', k, ', value is : ', v)
'''
Problem
    You want to create a dictionary, and you also want to control the order of items when
iterating or serializing.
Solution
    To control the order of items in a dictionary, you can use an OrderedDict from the
collections module. It exactly preserves the original insertion order of data when
iterating.
'''
print('-' * 80)
from collections import OrderedDict
od = OrderedDict()
od['a'] = 10
od['b'] = 20
od['c'] = 100
od['d'] = 80
od['e'] = 60
od['f'] = 30
for k, v in od.items():
    print('Key is : ', k, ', value is : ', v)
d = OrderedDict()
d['foo'] = 1
d['grok'] = 4
d['bar'] = 2
d['spam'] = 3
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
import json
j = json.dumps(od)
print(j)
d = {}
d['a'] = 1
d['b'] = 4
d['c'] = 2
d['d'] = 3
for key, value in d.items():
    print(key, ' - ', value)
j = json.dumps(d)
print(j)
'''
Problem
    You want to perform various calculations (e.g., minimum value, maximum value, sorting,
etc.) on a dictionary of data.
Solution
    In order to perform useful calculations on the dictionary contents, it is often useful to
invert the keys and values of the dictionary using zip().
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
min_price = min(zip(prices.values(), prices.keys()))
print('Min price is : ', min_price)
max_price = max(zip(prices.values(), prices.keys()))
print('Max price is : ', max_price)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
'''
When doing these calculations, be aware that zip() creates an iterator that can only be
consumed once. For example, the following code is an error:
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
'''
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
'''
Problem
    You have two dictionaries and want to find out what they might have in common (same
keys, same values, etc.).
Solution
    To find out what the two dictionaries have in common, simply perform common set
operations using the keys() or items() methods.
'''
d1 = {'x': 1, 'y': 2, 'z': 3}
d2 = {'x': 4, 'y': 2, 'w': 3}
sks = d1.keys() & d2.keys()
print('Dictionary 1 : ', d1)
print('Dictionary 2 : ', d2)
print('Keys in common : ', sks, ', type is : ', type(sks))
aks = d1.keys() - d2.keys() # keys in common
print('Keys only in dictionary 1 : ', aks, ', type is : ', type(aks)) # keys in d1 that are not in d2
sds = d1.items() & d2.items() # (key,value) pairs in common
print('Same dictionary element : ', sds, ', type is : ', type(sds))
nd = {key: d1[key] for key in d1.keys() - {'z'}}
print('New dictionary : ', nd)