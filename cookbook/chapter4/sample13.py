'''
Problem
    You want to process data iteratively in the style of a data processing pipeline (similar to
Unix pipes). For instance, you have a huge amount of data that needs to be processed,
but it can’t fit entirely into memory.
Solution
    Generator functions are a good way to implement processing pipelines.
'''
import os, fnmatch, gzip, bz2, re
def gen_find(file_pattern, file_top_path):
    for path, dirlist, filelist in os.walk(file_top_path):
        for name in fnmatch.filter(filelist, file_pattern):
            yield os.path.join(path, name)
for file_path in gen_find('Apriso*', 'C:\Temp'):
    print('File path : ', file_path)
def gen_opener(file_paths):
    for file_path in file_paths:
        f = open(file_path, 'rt')
        yield f
        f.close()
def gen_concatenate(iterators):
    for it in iterators:
        yield from it
def gen_grep(pattern, lines):
    p = re.compile(pattern)
    for line in lines:
        if p.search(line):
            yield line
print('-' * 80)
log_file_paths = gen_find('Apriso*', 'C:\Temp')
log_files = gen_opener(log_file_paths)
all_lines = gen_concatenate(log_files)
apriso_lines = gen_grep('FlexNet*', all_lines)
# apriso_lines = gen_grep('.*', all_lines) # 遍历所有
row = 0
from time import time
start_time = time()
for line in apriso_lines:
    row += 1
    print('Row : {} -> content : {}'.format(row, line))
finish_time = time()
print('Total {} rows, used time {:.2f} seconds.'.format(row, (finish_time-start_time)))
print('-' * 80)