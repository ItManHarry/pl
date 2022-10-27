'''
Creating an Instance Without Invoking init
Problem
You need to create an instance, but want to bypass the execution of the __init__()
method for some reason.
Solution
A bare uninitialized instance can be created by directly calling the __new__() method
of a class.
'''
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __repr__(self):
        return 'Date is : {}-{}-{}'.format(self.year, self.month, self.day)

d = Date.__new__(Date)
# print(d)
'''
print(d.year)
Traceback (most recent call last):
  File "D:\Development\Python\workplaces\pl\cookbook\chapter8\sample17.py", line 18, in <module>
    print(d.year)
AttributeError: 'Date' object has no attribute 'year'

As you can see, the resulting instance is uninitialized. Thus, it is now your responsibility
to set the appropriate instance variables.
'''
data = {'year': 2012, 'month': 12, 'day': 2}
for k, v in data.items():
    setattr(d, k, v)
print(d)
