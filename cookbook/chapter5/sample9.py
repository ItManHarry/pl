'''
Reading Binary Data into a Mutable Buffer
Problem
    You want to read binary data directly into a mutable buffer without any intermediate
copying. Perhaps you want to mutate the data in-place and write it back out to a file.
Solution
    To read data into a mutable array, use the readinto() method of files
'''
import os
c_p = os.getcwd()
p_p = os.path.dirname(c_p)
print(p_p)
f_p = os.path.join(p_p, 'files\data.bin')
print(f_p)
size = os.path.getsize(f_p)
print('size : ', size)
buf = bytearray(size)
with open(f_p, 'rb') as f:
    f.readinto(buf)
print(buf)
n_f = os.path.join(p_p, 'files\\new_date.bin')
with open(n_f, 'wb') as f:
    f.write(buf)