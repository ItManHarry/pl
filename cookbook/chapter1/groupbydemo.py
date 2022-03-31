rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]
from operator import itemgetter, attrgetter
from itertools import groupby
# 先排序
rows.sort(key=itemgetter('date'))
# 后分组
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('\t', i)
print('-' * 80)
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
users.sort(key=attrgetter('gender'))
for g, items in groupby(users, key=attrgetter('gender')):
    print(g)
    for i in items:
        print('\t', i)