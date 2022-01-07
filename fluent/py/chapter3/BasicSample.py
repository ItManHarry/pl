from collections import abc
my_dict = {}
print('', isinstance(my_dict, abc.Mapping))
'''
What is hashable ? 
    An object is hashable if it has a hash value which never changes during its lifetime (it
needs a __hash__() method), and can be compared to other objects (it needs an
__eq__() method). Hashable objects which compare equal must have the same hash
value. […]
'''
tt = (1, 2, (10, 20))
print(hash(tt))
tl = (1, 2, [10, 20])
# TypeError: unhashable type: 'list'
# print(hash(tl))
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))
print('-' * 80)
'''
Building a dict by various ways
'''
a = {'a': 10, 'b': 20, 'c': 30}
b = dict(a=10, b=20, c=30)
'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
我们可以使用 list() 转换来输出列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
'''
c = dict(zip(['a', 'b', 'c'], [10, 20, 30]))
d = dict([('a', 10), ('c', 30), ('b', 20)])
e = dict([['a', 10], ['c', 30], ['b', 20]])
f = dict((('a', 10), ('c', 30), ('b', 20)))
g = dict((['a', 10], ['c', 30], ['b', 20]))
h = dict({'a': 10, 'b': 20, 'c': 30})
print(a == b == c == d == e == f == g == h)
print('-' * 80)
dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
country_codes = {country: code for code, country in dial_codes}
print(country_codes)
for k, v in country_codes.items():
    print('Key is : ', k, ' value is : ', v)
print('-' * 80)
r_country_codes = {code: country.upper() for country, code in country_codes.items() if code > 20}
for k, v in r_country_codes.items():
    print('Key is : ', k, ' value is : ', v)
print('-' * 80)
index = {}
keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'B', 'C', 'C', 'B', 'A', 'F']
for i in range(len(keys)):
    print('Key : ', keys[i],  ', index : ', i)
    for v in values:
        if keys[i] == v:
            index.setdefault(keys[i], []).append(v)
        else:
            index.setdefault(keys[i], [])
for k, v in index.items():
    print('Key is : ', k, ', value : ', v)