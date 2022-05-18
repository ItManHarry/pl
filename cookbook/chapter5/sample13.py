'''
Getting a Directory Listing
Problem
    You want to get a list of the files contained in a directory on the filesystem.
Solution
    Use the os.listdir() function to obtain a list of files in a directory
'''
import os, time
path = 'D:\Development\eclipse-workplace-kepler'
print(os.listdir(path))
print('-' * 80)
names = (name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name)))
print('Files : ')
for name in names:
    print('\t', name)
print('-' * 80)
print('Directories : ')
dirs = (dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir)))
for dir in dirs:
    print('\t', dir)
print('-' * 80)
def all_files(path, files):
    if os.path.isdir(path):
        for sub_path in os.listdir(path):
            new_path = os.path.abspath(os.path.join(path, sub_path))
            if os.path.isdir(new_path):
                all_files(new_path, files)
            else:
                files.append(new_path)
    else:
        files.append(path)
        return files
files = []
s_t1 = time.time()
all_files(path, files)
print('File size : ', len(files))
for file in files:
    print('\tFile : ', file)
e_t1 = time.time()
print('-' * 80)
def all_files2(path):
    for path, dirlist, filelist in os.walk(path):
        for file in filelist:
            yield os.path.abspath(os.path.join(path, file))
s_t2 = time.time()
for file in all_files2(path):
    print('File is : ', file)
e_t2 = time.time()
print('File size : {}, time 1 : {:.2f} seconds, time2 : {:.2f} seconds.'.format(len(files), e_t1-s_t1, e_t2-s_t2))