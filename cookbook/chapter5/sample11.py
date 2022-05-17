'''
Manipulating Pathnames
Problem
    You need to manipulate pathnames in order to find the base filename, directory name,
absolute path, and so on.
Solution
    To manipulate pathnames, use the functions in the os.path module. Here is an interactive
example that illustrates a few key features
'''
import os
path = '/Users/harry/data/employees.csv'
# get last component of the path
print(os.path.basename(path))
# get directory name
print(os.path.dirname(path))
# join together
print(os.path.join('tmp', 'data', os.path.basename(path)))
# Split the file extension
print(os.path.splitext(path))