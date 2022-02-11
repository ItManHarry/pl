'''
Both bytes and bytearray support every str method except those that do formatting
(format, format_map) and a few others that depend on Unicode data, including case
fold, isdecimal, isidentifier, isnumeric, isprintable, and encode. This means that
you can use familiar string methods like endswith, replace, strip, translate, upper,
and dozens of others with binary sequences—only using bytes and not str arguments.
In addition, the regular expression functions in the re module also work on binary
sequences, if the regex is compiled from a binary sequence instead of a str. The %
operator does not work with binary sequences in Python 3.0 to 3.4, but should be
supported in version 3.5 according to PEP 461 — Adding % formatting to bytes and bytearray.
'''
# bytes can be built from a str, given an encoding
cafe = bytes('café', encoding='utf_8')
print(cafe)
# Each item is an integer in range(256)
for c in cafe:
    print('Item : ', c)
# Slices of bytes are also bytes—even slices of a single byte.
print(cafe[:1])
# There is no literal syntax for bytearray: they are shown as bytearray() with a bytes literal as argument.
cafe_arr = bytearray(cafe)
print(type(cafe_arr))
# A slice of bytearray is also a bytearray.
print(cafe_arr[-1:])
for b in cafe_arr:
    print('Item is : ', b)
'''
Binary sequences have a class method that str doesn’t have, called fromhex, which builds
a binary sequence by parsing pairs of hex digits optionally separated by spaces:
'''
bs = bytes.fromhex('31 4B CE A9')
print('Bytes is : ', bs)
'''
Building a binary sequence from a buffer-like object is a low-level operation that may
involve type casting
'''
import array
# Typecode 'h' creates an array of short integers (16 bits).
numbers = array.array('h', [-2, -1, 0, 1, 2])
for n in numbers:
    print('Number is : ', n)
# octets holds a copy of the bytes that make up numbers
octets = bytes(numbers)
# These are the 10 bytes that represent the five short integers
print(octets)
for b in octets:
    print('Item is : ', b)
'''
The struct module provides functions to parse packed bytes into a tuple of fields of
different types and to perform the opposite conversion, from a tuple into packed bytes.
struct is used with bytes, bytearray, and memoryview objects
'''
import struct
fmt = '<3s3sHH'
with open('filter.gif', 'rb') as fp:
    img = memoryview(fp.read())
header = img[:10]
bytes(header)
struct.unpack(fmt, header)
del header
del img