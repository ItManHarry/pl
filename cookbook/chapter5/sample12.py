'''
Testing for the Existence of a File
Problem
    You need to test whether or not a file or directory exists.
Solution
    Use the os.path module to test for the existence of a file or directory
'''
import os, time, datetime
path = 'c:/temp'
if os.path.exists(path):
    print('File path exist...')
    # is file
    if os.path.isfile(path):
        print('it is a file')
    else:
        print('it is not a file')
    # is directory
    if os.path.isdir(path):
        print('it is a directory')
    else:
        print('it is not a directory')
    # size
    print('size is : ', os.path.getsize(path))
    # modified time
    #print('Modified time : ', os.path.getmtime(path), datetime.datetime.strptime((time.ctime(os.path.getmtime(path))), '%Y-%m-%d'))
    print('Modified time : ', os.path.getmtime(path), time.ctime(os.path.getmtime(path)))
else:
    print('File path not exist...')