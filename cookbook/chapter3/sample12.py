'''
Problem
    You have code that needs to perform simple time conversions, like days to seconds,
hours to minutes, and so on.
Solution
    To perform conversions and arithmetic involving different units of time, use the date
time module. For example, to represent an interval of time, create a timedelta instance,
like this:
'''
from datetime import timedelta, datetime, date
a = timedelta(days=2, hours=6, minutes=2, seconds=20)
b = timedelta(hours=4.5)
c = a + b
print('Days : ', c.days)
print('Seconds : ', c.seconds)
print('Total seconds : ', c.total_seconds())
print('Hours : ', c.seconds/3600)
print('Total hours : ', c.total_seconds()/3600)
'''
If you need to represent specific dates and times, create datetime instances and use the
standard mathematical operations to manipulate them. For example:
'''
today = date.today()
now = datetime.now()
print('Today {} type is {}'.format(today, type(today)))
print('Now {} type is {}'.format(now, type(now)))
# datetime to string
print('Now is {} '.format(now.strftime('%Y-%m-%d %H:%M:%S')))
eight_days_before = today - timedelta(days=8)
eight_days_after = today + timedelta(days=8)
print('Eight days before : {}, after : {}'.format(eight_days_before, eight_days_after))
# string to datetime
day = datetime.strptime('2022-05-06', '%Y-%m-%d')
print('Day {} type is {}'.format(day, type(day)))
print('Day {} type is {}'.format(day.date(), type(day.date())))
cd = day.date() - today
print('Days is : ', cd.days)
