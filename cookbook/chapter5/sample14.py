'''
Bypassing Filename Encoding
Problem
    You want to perform file I/O operations using raw filenames that have not been decoded
or encoded according to the default filename encoding.
Solution
    By default, all filenames are encoded and decoded according to the text encoding returned
by sys.getfilesystemencoding().
'''
import os
import sys
f_e = sys.getfilesystemencoding()
print(f_e)
'''
If you want to bypass this encoding for some reason, specify a filename using a raw byte
string instead.
'''
with open('jalape\xf1o.txt', 'w') as f:
    f.write('Spicy!')
print(os.listdir())
print(os.listdir(b'.'))
with open(b'jalape\xc3\xb1o.txt') as f:
    print(f.read())