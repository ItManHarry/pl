'''
Writing to a File That Doesn’t Already Exist
Problem
    You want to write data to a file, but only if it doesn’t already exist on the filesystem
Solution
    This problem is easily solved by using the little-known x mode to open() instead of the
usual w mode
'''
import os
current_work_directory = os.getcwd()
print(current_work_directory)
file_path = os.path.abspath(os.path.dirname(current_work_directory))
print(file_path)
write_file_path = os.path.join(file_path, 'files\print_binary.txt')
print(write_file_path)
with open(write_file_path, 'xt') as f:
    f.write('Hello World')
print('-' * 80)