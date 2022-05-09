'''
Reading and Writing Text Data
Problem
    You need to read or write text data, possibly in different text encodings such as ASCII,
UTF-8, or UTF-16.
Solution
    Use the open() function with mode rt to read a text file.
'''
import os
print('-' * 80)
path = os.path.dirname(__file__)
parent_path = os.path.dirname(path)
print(os.path.abspath(parent_path))
base_path = os.path.abspath(parent_path)
file_path = os.path.join(base_path, 'files\data.txt')
print(file_path)
print('-' * 80)
with open(file_path, 'rt') as f:
    '''data = f.read()
    print(data)'''
    for line in f:
        print(line)
print('-' * 80)
'''
Similarly, to write a text file, use open() with mode wt to write a file, clearing and
overwriting the previous contents (if any).
'''
new_file_path = os.path.join(base_path, 'files\data2.txt')
with open(new_file_path, 'wt') as f:
    f.write('This is a new file\n')
    f.write('I am writing content on it\n')
    f.write('Good!\n')
    f.write('Very Good!\n')
    f.write('Finish with some numbers\n')
    for i in range(10):
        f.write(str(i)+'\n')
'''
To append to the end of an existing file, use open() with mode at
'''
with open(new_file_path, 'at') as f:
    print('append01', file=f)
    print('append02', file=f)
    print('append03', file=f)
    for i in range(50):
        print('append {} row'.format(i), file=f)