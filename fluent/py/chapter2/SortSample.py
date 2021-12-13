'''
The list.sort method sorts a list in place—that is, without making a copy. It returns
None to remind us that it changes the target object, and does not create a new list. This
is an important Python API convention: functions or methods that change an object in
place should return None to make it clear to the caller that the object itself was changed,
and no new object was created.
In contrast, the built-in function sorted creates a new list and returns it. In fact, it
accepts any iterable object as an argument, including immutable sequences and generators
Both list.sort and sorted take two optional, keyword-only arguments
reverse
    If True, the items are returned in descending order (i.e., by reversing the comparison
of the items). The default is False.
key
    A one-argument function that will be applied to each item to produce its sorting
key. For example, when sorting a list of strings, key=str.lower can be used to
perform a case-insensitive sort, and key=len will sort the strings by character
length. The default is the identity function (i.e., the items themselves are compared).
'''
fruits = ['grape', 'raspberry', 'apple', 'banana', 'watermelon']
sorted_fruits = sorted(fruits)
print('Fruits are : ', fruits)
print('Sorted fruits are : ', sorted_fruits)
fruits.sort()
print('Now the fruits are : ', fruits)
num_list = [10, 50, 5, 30, 25, 100, 60]
sorted_num_list1 = sorted(num_list)
sorted_num_list2 = sorted(num_list, reverse=True)
print('Sorted number list 1 : ', sorted_num_list1)
print('Sorted number list 2 : ', sorted_num_list2)
fruits = ['grape', 'raspberry', 'apple', 'banana', 'watermelon']
sorted_fruits_by_len = sorted(fruits, key=len)
print('Sorted fruit list by length : ', sorted_fruits_by_len)
sorted_by_len_and_reversed = sorted(fruits, reverse=True, key=len)
print('Sorted fruit by length and reversed : ', sorted_by_len_and_reversed)
