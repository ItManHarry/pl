'''
Printing to a File
Problem
    You want to redirect the output of the print() function to a file.
Solution
    Use the file keyword argument to print()
'''
import os
current_path = os.path.dirname(__file__)
print('Current file path is : ', current_path)
absolute_path = os.path.abspath(os.path.dirname(current_path))
print('Absolute path : ', absolute_path)
file_path = os.path.join(absolute_path, r'files\print_file.txt')
print('File path : ', file_path)
with open(file_path, 'wt') as f:
    for i in range(10):
        print('Row {}'.format(i), file=f)