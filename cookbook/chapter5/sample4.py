'''
Reading and Writing Binary Data
Problem
    You need to read or write binary data, such as that found in images, sound files, and so
on
Solution
    Use the open() function with mode rb or wb to read or write binary data
'''
import os
current_work_directory = os.getcwd()
print(current_work_directory)
file_path = os.path.abspath(os.path.dirname(current_work_directory))
print(file_path)
write_file_path = os.path.join(file_path, 'files\print_binary.bin')
print(write_file_path)
with open(write_file_path, 'wb') as f:
    f.write(b'Hello World')
with open(write_file_path, 'rb') as f:
    data = f.read()
    print(data)
print('-' * 80)
write_file_path = os.path.join(file_path, 'files\print_binary_encode.bin')
with open(write_file_path, 'wb') as f:
    f.write('Hello World'.encode('utf-8'))
with open(write_file_path, 'rb') as f:
    data = f.read(16)
    print(data.decode('utf-8'))