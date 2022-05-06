'''
Problem
    You want to process data iteratively in the style of a data processing pipeline (similar to
Unix pipes). For instance, you have a huge amount of data that needs to be processed,
but it can’t fit entirely into memory.
Solution
    Generator functions are a good way to implement processing pipelines.
'''
import os
# 获取当前文件夹路径
print('-' * 80)
work_dir = os.getcwd()
print('Work directory : ', work_dir)
print('-' * 80)
# 某文件路径下所有的文件及文件夹
dir_list = os.listdir(work_dir)
print(dir_list)
print('-' * 80)
# 深层遍历文件夹及子文件夹
for path, dirs, files in os.walk(work_dir):
    print('Path : {}'.format(path))
    print('\tDirectories {}'.format(dirs))
    for dir in dirs:
        for sub_path, sub_dirs, sub_files in os.walk(dir):
            print('\t\tSub path : {}'.format(os.path.join(path,sub_path)))
            print('\t\t\tSub directories {}'.format(sub_dirs))
            print('\t\t\tSub files {}'.format(sub_files))
    print('\tFiles {}'.format(files))
    #print('Salary is : {:,.2f}'.format(251362.3215))
print('-' * 80)
path = r'c:\temp2'
# 判断文件夹、文件是否存在
if os.path.exists(path):
    print('Path exists!')
    # 判断是否是文件夹
    if os.path.isdir(path):
        print('It is a directory!')
    else:
        print('It is a file!')
else:
    print('Path not exists, create folder')
    # 创建单层文件夹
    os.mkdir(path)
    print('Create folder successfully!')
# 创建深层目录
path = r'c:\temp3\test\ddd'
if os.path.exists(path):
    print('File or directory exists.')
else:
    print('Create...')
    os.makedirs(path)
    print('Create successfully...')
# 删除刚才新建的目录
os.rmdir(path)
print('Remove folder successfully.')
#传入两个path路径，将该路径拼接起来，形成一个新的完整路径
new_path = os.path.join(path, 'a.jpg')
print('New path is : ', new_path)
# 拆分路径为文件夹路径和文件名
folder_path, file_name = os.path.split(new_path)
print('Folder : \'{}\', file : \'{}\'!'.format(folder_path, file_name))
#传入一个完整的文件路径，只获取其绝对路径
path = os.path.dirname(__file__)
print('Current file folder path : ', path)
parent_path = os.path.dirname(path)
print('Parent path is : ', parent_path)
absolute_path = os.path.abspath(parent_path)
print('Absolute path is : ', absolute_path)
print(os.path.join(absolute_path, 'ad'))
#传入一个完整的文件路径，只获取其文件名
base_name = os.path.basename(os.path.join(absolute_path, 'aaa.jpg'))
print('Base name : ', base_name)
# 首先判断文件是否存在
file = os.path.join(absolute_path, 'aaa.jpg')
if os.path.exists(file):
    # 而后判断是否是文件
    if os.path.isfile(file):
        print('A file')
    else:
        print('Not a file')
else:
    print('Path is not exist!')
# 当前操作系统的分隔符
print('System separator is : ', os.path.sep)
file = os.path.join(os.getcwd(), 'sample13.py')
file_size = os.path.getsize(file)
print('File size is : {} kb'.format(file_size))