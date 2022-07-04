'''
Problem
    You want an object to support customized formatting through the format() function
and string method.
Solution
    To customize string formatting, define the __format__() method on a class
'''
_fmt = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _fmt[code]
        return fmt.format(d=self)
d = Date(2022, 7, 4)
print(format(d))
print(format(d, 'mdy'))
print('{:dmy}'.format(d))
from datetime import date
d = date(2022, 7, 4)
print('{}'.format(d))
print('{:%d%m%Y}'.format(d))