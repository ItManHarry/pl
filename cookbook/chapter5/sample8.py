'''
Iterating Over Fixed-Sized Records
Problem
    Instead of iterating over a file by lines, you want to iterate over a collection of fixedsized
records or chunks.
Solution
    Use the iter() function and functools.partial() using this neat trick
'''
from functools import partial
import os
c_p = os.getcwd()
p_p = os.path.dirname(c_p)
f_p = os.path.join(p_p, 'files\data.bin')
print(f_p)
# write binary data
with open(f_p, 'wb') as f:
    for i in range(20):
        bt = 'text'+str(i)+'\n'
        f.write(bt.encode('utf-8'))
print('write finished...')
# read data
RECORD_SIZE = 64
with open(f_p, 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for record in records:
        print('Record: ', record.decode('utf-8'))