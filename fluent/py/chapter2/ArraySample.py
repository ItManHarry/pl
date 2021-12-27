'''
A Python array is as lean as a C array. When creating an array, you provide a typecode,
a letter to determine the underlying C type used to store each item in the array. For
example, b is the typecode for signed char. If you create an array('b'), then each item
will be stored in a single byte and interpreted as an integer from –128 to 127. For large
sequences of numbers, this saves a lot of memory. And Python will not let you put any
number that does not match the type for the array.
Type code
'b' -> int
'B' -> int
'u' -> Unicode character
'h' -> int
'H' -> int
'i' -> 2
'I' -> int
'L' -> int
'q' -> 8
'Q' -> int
'f' -> float
'd' -> float
Methods：
    append() -- append a new item to the end of the array
    buffer_info() -- return information giving the current memory info
    byteswap() -- byteswap all the items of the array
    count() -- return number of occurrences of an object
    extend() -- extend array by appending multiple elements from an iterable
    fromfile() -- read items from a file object
    fromlist() -- append items from the list
    frombytes() -- append items from the string
    index() -- return index of first occurrence of an object
    insert() -- insert a new item into the array at a provided position
    pop() -- remove and return item (default last)
    remove() -- remove first occurrence of an object
    reverse() -- reverse the order of the items in the array
    tofile() -- write all items to a file object
    tolist() -- return the array converted to an ordinary list
    tobytes() -- return the array converted to a string
'''

from array import array
from random import random
floats = array('d', (random() for i in range(10 ** 7)))
print('Length of floats : ', len(floats), ', type code is : ', floats.typecode)
print('Last element is : ', floats[-1])
fp = open('d:\\floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('d:\\floats.bin', 'rb')
floats2.fromfile(fp, 10 ** 7)
fp.close()
print('Last element is : ', floats2[-1])
print('Float1 == floats2 ? ', floats == floats2)
print('-' * 80)
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print('Length of memory view is : ', len(memv))
print('Memory view : ', memv)
memv_oct = memv.cast('B')
print(memv_oct.tolist())