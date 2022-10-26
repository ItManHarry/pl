'''
Implementing Custom Containers
Problem
You want to implement a custom class that mimics the behavior of a common built-in
container type, such as a list or dictionary. However, you’re not entirely sure what
methods need to be implemented to do it.
Solution
The collections library defines a variety of abstract base classes that are extremely
useful when implementing custom container classes. To illustrate, suppose you want
your class to support iteration. To do that, simply start by having it inherit from collections.Iterable
'''
import bisect
from collections.abc import Sequence, MutableSequence
class SortedItem(Sequence):
    def __init__(self, initial):
        self._items = sorted(initial) if initial is not None else []
    def __getitem__(self, index):
        return self._items[index]
    def __len__(self):
        return len(self._items)
    def add(self, item):
        bisect.insort(self._items, item)
items = SortedItem([1,5,3])
l = list(items)
print(l)
print(l[0])
items.add(8)
items.add(4)
print(list(items))
print('-' * 80)
class Items(MutableSequence):
    def __init__(self, initial):
        self._items = list(initial) if initial is not None else []
    def __getitem__(self, index):
        print('Getting item : ', index)
        return self._items[index]
    def __setitem__(self, index, value):
        print('Setting : index is {}, value is {}.'.format(index, value))
        self._items[index] = value
    def __delitem__(self, index):
        print('Deleting : ', index)
        del self._items[index]
    def insert(self, index, value):
        print('Insert : index {} value {}'.format(index, value))
        self._items.insert(index, value)
    def __len__(self):
        print('len')
        return len(self._items)
item = Items([1,5,2])
print(len(item))
item.append(8)
item.append('a')
print(list(item))
data = [(1, 20), (5, 30), (3, 100), (2, 200)]
new_data = sorted(data, key=lambda x: x[0])
print(new_data)