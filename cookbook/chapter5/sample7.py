'''
Reading and Writing Compressed Datafiles
Problem
    You need to read or write data in a file with gzip or bz2 compression
Solution
    The gzip and bz2 modules make it easy to work with such files. Both modules provide
an alternative implementation of open() that can be used for this purpose
'''
import gzip, bz2, os
c_p = os.getcwd()
p_p = os.path.dirname(c_p)
print(p_p)
f_p = os.path.join(p_p, 'files\data.gz')
print(f_p)
# write data
with gzip.open(f_p, 'wt') as f:
    f.write('gzip test')
# read data
with gzip.open(f_p, 'rt') as f:
    data = f.read()
    print(data)
f_p = os.path.join(p_p, 'files\data.bz2')
# write data
with bz2.open(f_p, 'wt') as f:
    print('bz2 data ', file=f)
# read data
with bz2.open(f_p, 'rt') as f:
    data = f.read()
    print(data)
