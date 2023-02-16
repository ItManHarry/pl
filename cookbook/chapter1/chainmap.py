'''
Problem
    You have multiple dictionaries or mappings that you want to logically combine into a
single mapping to perform certain operations, such as looking up values or checking
for the existence of keys.
Solution
    Suppose you have two dictionaries:
        a = {'x': 1, 'z': 3 }
        b = {'y': 2, 'z': 4 }
Now suppose you want to perform lookups where you have to check both dictionaries
(e.g., first checking in a and then in b if not found). An easy way to do this is to use the
ChainMap class from the collections module.
'''
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
from collections import ChainMap
c = ChainMap(b, a)
print('a : ', a)
print('b : ', b)
print('c : ', c)
for k, v in c.items():
    print('Key is : ', k, ', value : ', v)
s = '010102'[-2:]
codes = ['01001001', '01001002', '01001003', '01001004', '01001015', '01001150', '01001005']
new_code_num = int(max(codes)[-3:]) + 1
if new_code_num < 10:
    print('00' + str(new_code_num))
elif new_code_num < 100:
    print('0' + str(new_code_num))
else:
    print(str(new_code_num))
print(int(s))
x = dict(
    aaa=10,
    bbb=20,
)
y = {'ccc': 100, 'ddd': 200}
z = ChainMap(x, y)
for k, v in z.items():
    print('Key is : ', k, ', value is : ', v)



import time, datetime, uuid
from datetime import date
today = date.today()
print(today.strftime('%Y/%m/%d'))
date_str = '2022-01-25'
year, month, day = [int(s) for s in date_str.split('-')]
print(year)
print(month)
print(day)
date_d = date(year, month, day)
print(type(date_d), 'Date is : ', date_d)
date_d = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
print(type(date_d), 'Date is : ', date_d)
def utc_to_locale(utc_date_time, off_set=None):
    '''
    UTC时间转本地
    :param utc_date_time:   UTC时间
    :param off_set:         时区(如果为None则默认转为本地时区)
    :return:
    '''
    now_stamp = time.time()
    locale_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    # 计算时区差
    if off_set is None:
        off_set = locale_time - utc_time
    else:
        off_set = datetime.timedelta(hours=off_set)
    locale_date_time = utc_date_time + off_set
    return locale_date_time
utc_now = datetime.datetime.utcnow()
print(utc_now)
print(utc_to_locale(utc_now, 7))