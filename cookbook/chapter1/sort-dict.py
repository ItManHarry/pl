'''
Problem
    You have a list of dictionaries and you would like to sort the entries according to one
or more of the dictionary values.
Solution
    Sorting this type of structure is easy using the operator module’s itemgetter function.
Let’s say you’ve queried a database table to get a listing of the members on your website,
and you receive the following data structure in return:
'''
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003, 'salary': 1020},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002, 'salary': 2030},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001, 'salary': 1500},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004, 'salary': 1000}
]
from operator import itemgetter, attrgetter
sorted_by_fname = sorted(rows, key=itemgetter('fname'))
sorted_by_uid = sorted(rows, key=itemgetter('uid'))
print('*' * 80)
for row in rows:
    for k, v in row.items():
        print('Key : ', k, ', value : ', v)
        print('-' * 80)
print('*' * 80)
for row in sorted_by_fname:
    for k, v in row.items():
        print('Key : ', k, ', value : ', v)
        print('-' * 80)
print('*' * 80)
for row in sorted_by_uid:
    for k, v in row.items():
        print('Key : ', k, ', value : ', v)
        print('-' * 80)
print('*' * 80)
sorted_by_lname = sorted(rows, key=itemgetter('lname', 'fname'))
for row in sorted_by_lname:
    for k, v in row.items():
        print('Key : ', k, ', value : ', v)
        print('-' * 80)
print('*' * 80)
min_salary = min(rows, key=itemgetter('salary'))
max_salary = max(rows, key=itemgetter('salary'))
print('Min salary : ', min_salary)
print('Max salary : ', max_salary)
print('*' * 80)
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return 'Name : ' + self.name + '; age : ' + str(self.age) + '; gender : ' + self.gender
users = [
    User('Jane', 23, 'F'),
    User('Harry', 39, 'M'),
    User('Jany', 21, 'F'),
    User('Sam', 52, 'M'),
    User('Tom', 32, 'M'),
    User('Jerry', 48, 'F'),
    User('Henry', 23, 'M')
]
sorted_by_name = sorted(users, key=attrgetter('name'))
for user in users:
    print(user)
print('-' * 80)
for user in sorted_by_name:
    print(user)
sorted_by_name_and_age = sorted(users, key=attrgetter('age', 'name'))
print('-' * 80)
for user in sorted_by_name_and_age:
    print(user)
min_age_user = min(users, key=attrgetter('age'))
max_age_user = max(users, key=attrgetter('age'))
print('Youngest user : ', min_age_user)
print('Oldest user : ', max_age_user)
