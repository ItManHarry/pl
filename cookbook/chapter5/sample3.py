'''
Printing with a Different Separator or Line Ending
Problem
    You want to output data using print(), but you also want to change the separator
character or line ending.
Solution
    Use the sep and end keyword arguments to print() to change the output as you wish
'''
import os
current_file_path = os.path.dirname(__file__)
print('Current file path : ', current_file_path)
parent_dir_path = os.path.dirname(current_file_path)
print('Parent directory path : ', parent_dir_path)
write_file_path = os.path.join(os.path.abspath(parent_dir_path), 'files\print_file_2.txt')
print('Write file path : ', write_file_path)
data = (
    ('Jane', 35, 'F'),
    ('Jack', 25, 'M'),
    ('Tom', 30, 'M'),
    ('Jany', 40, 'F')
)
with open(write_file_path, 'wt') as f:
    for row in data:
        print(*row, sep=',', file=f)