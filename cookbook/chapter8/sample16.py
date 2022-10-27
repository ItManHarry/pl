'''
Defining More Than One Constructor in a Class
Problem
You’re writing a class, but you want users to be able to create instances in more than the
one way provided by __init__().
Solution
To define a class with more than one constructor, you should use a class method
'''
import time
class MyDate:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __repr__(self):
        return 'Year : {}, month : {}, day : {}'.format(self.year, self.month, self.day)

d = MyDate(2020, 12, 31)
print(d)
d = MyDate.today()
print(d)
class ChildDate(MyDate):
    pass
cd = ChildDate(2020, 12, 1)
print(cd)
print(cd.today())