'''
Memory Mapping Binary Files
Problem
    You want to memory map a binary file into a mutable byte array, possibly for random
access to its contents or to make in-place modifications.
Solution
    Use the mmap module to memory map files. Here is a utility function that shows how to
open a file and memory map it in a portable manner:
'''
import os, mmap
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)
size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')
m = memory_map('data')
print(len(m))
print(m[0:10])
m[0:11] = b'hellopython'
print(m[0:11])
m.close()
with open('data', 'rb') as f:
    print(f.read(11))
'''
The mmap object returned by mmap() can also be used as a context manager, in which
case the underlying file is closed automatically.
'''
with memory_map('data') as m:
    print(len(m))
    print(m[0:11])