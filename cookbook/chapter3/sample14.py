'''
Problem
    You have some code that needs to loop over each date in the current month, and want
an efficient way to calculate that date range.
Solution
    Looping over the dates doesn’t require building a list of all the dates ahead of time. You
can just calculate the starting and stopping date in the range, then use datetime.time
delta objects to increment the date as you go.
'''
from datetime import date, datetime, timedelta
import calendar
def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_of_month = calendar.monthrange(start_date.year, start_date.month)
    last_date = start_date + timedelta(days=days_of_month)
    return (start_date, last_date)
date_range = get_month_range()
print(date_range)
one_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print('Day : {}'.format(first_day))
    first_day += one_day
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step
for d in date_range(datetime(2022, 4, 1), datetime(2022, 4, 30), timedelta(hours=6)):
    print(d)