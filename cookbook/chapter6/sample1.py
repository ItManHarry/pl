'''
Reading and Writing CSV Data
Problem
    You want to read or write data encoded as a CSV file.
Solution
    For most kinds of CSV data, use the csv library
'''
import csv
import os

c_p = os.getcwd()
p_p = os.path.dirname(c_p)
print(p_p)
csv_file = os.path.abspath(os.path.join(p_p, 'files/GMES-用户数量.csv'))
print(csv_file)
with open(csv_file, encoding='utf-8') as f:
    csv_data = csv.reader(f)
    print(csv_data)
    headers = next(csv_data)
    print(headers)
    for row in csv_data:
        print(row[0], '\t', row[1], '\t', row[2], '\t', row[3])
print('-' * 80)
from collections import namedtuple
user_data = []
Data = namedtuple('Data', ['Name', 'NameKR', 'Code', 'Category'])
with open(csv_file, encoding='utf-8') as f:
    csv_data = csv.reader(f)
    print(csv_data)
    headers = next(csv_data)
    for row in csv_data:
        user_data.append(Data(*row))
print(len(user_data))
for data in user_data:
    print('Chinese name : {}, Korean name : {}, code : {}, category : {}'.format(data.Name, data.NameKR, data.Code, data.Category))
    if data.Name is None or data.Name == '':
        print('\tChinese name is null')
    if data.NameKR is None or data.NameKR == '' or data.NameKR == 'NULL':
        print('\tKorean name is null')
    if data.Category is None or data.Category == '':
        print('\tCategory is null')
print('-' * 80)
with open(csv_file, encoding='utf-8') as f:
    f_csv = csv.DictReader(f)
    print(next(f_csv))
    for row in f_csv:
        for k, v in row.items():
            print(k, v)
            if k == 'Name':
                print('Name key OK')
            else:
                print('Not name key')
        print('-' * 20)
# write to csv file
headers = ['Name', 'Age', 'Gender', 'Email', 'Phone']
rows = [
    ['Harry', 24, 'F', 'email1@doosan.com', '13785642110'],
    ['Jane', 32, 'M', 'email2@doosan.com', '13785642111'],
    ['Henry', 28, 'F', 'email3@doosan.com', '13785642112'],
    ['Sam', 40, 'M', 'email4@doosan.com', '13785642113'],
    ['July', 54, 'M', 'email5@doosan.com', '13785642114'],
    ['Harry', 35, 'F', 'email6@doosan.com', '13785642115']
]
csv_file = os.path.abspath(os.path.join(p_p, 'files/employees.csv'))
with open(csv_file, 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
employees = []
with open(csv_file) as f:
    f_c = csv.reader(f)
    headers = next(f_c)
    Employee = namedtuple('Employee', headers)
    for row in f_c:
        if row:
            employees.append(Employee(*row))
for employee in employees:
    print(employee.Name)
print('-' * 80)
headers = ['code', 'name', 'parent_code']
rows = [
    {'code': '0000', 'name': 'HDICC', 'parent_code': '0000'},
    {'code': '0001', 'name': 'SALES', 'parent_code': '0000'},
    {'code': '0002', 'name': 'SALES-PART1', 'parent_code': '0001'},
    {'code': '0003', 'name': 'SALES-PART2', 'parent_code': '0001'},
]
csv_file = os.path.abspath(os.path.join(p_p, 'files/departments.csv'))
print(csv_file)
with open(csv_file, 'w') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)
departments = []
with open(csv_file) as f:
    csv_data = csv.reader(f)
    Department = namedtuple('Department', next(csv_data))
    for row in csv_data:
        if row:
            departments.append(Department(*row))
for department in departments:
    print('Department name : ', department.name)

