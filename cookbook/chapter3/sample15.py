'''
Problem
    Your application receives temporal data in string format, but you want to convert those
strings into datetime objects in order to perform nonstring operations on them.
Solution
    Python’s standard datetime module is typically the easy solution for this. For example:
'''
from datetime import datetime
date_str = '2022-04-23'
date_time = datetime.strptime(date_str, '%Y-%m-%d')
print(date_time)
date_now = datetime.now()
d = date_now - date_time
print(type(d))
print('Days {}, hours {:.2f}, minutes {:.2f} seconds {:,.2f}!'.format(d.days, d.seconds/3600, d.seconds/60, d.seconds))
def str_to_date(date_str):
    year, month, day = date_str.split('-')
    return datetime(int(year), int(month), int(day))
d = str_to_date('2022-04-25')
print(d)