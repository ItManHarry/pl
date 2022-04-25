'''
Problem
    You want a general solution for finding a date for the last occurrence of a day of the
week. Last Friday, for example.
Solution
    Python’s datetime module has utility functions and classes to help perform calculations
like this. A decent, generic solution to this problem looks like this:
'''
from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date
td = get_previous_byday('Tuesday')
print(td.strftime('%Y-%m-%d'))
td = get_previous_byday('Monday')
print(td.strftime('%Y-%m-%d'))
'''
If you’re performing a lot of date calculations like this, you may be better off installing
the python-dateutil package instead. For example, here is an example of performing
the same calculation using the relativedelta() function from dateutil:
'''
print('-' * 80)
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO, TH, TU, WE, FR, SA, SU
now = datetime.now()
# Last Friday
print('Last Friday {}.'.format((now + relativedelta(weekday=FR(-1))).strftime('%Y-%m-%d')))
# Last Monday
print('Last Monday {}.'.format((now + relativedelta(weekday=MO(-1))).strftime('%Y-%m-%d')))
# Next Friday
print('Next Friday {}.'.format((now + relativedelta(weekday=FR)).strftime('%Y-%m-%d')))
# Next Monday
print('Next Monday {}.'.format((now + relativedelta(weekday=SA)).strftime('%Y-%m-%d')))