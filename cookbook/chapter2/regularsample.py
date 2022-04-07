'''
Problem
    You want to match text using the same wildcard patterns as are commonly used when
working in Unix shells (e.g., *.py, Dat[0-9]*.csv, etc.).
Solution
    The fnmatch module provides two functions—fnmatch() and fnmatchcase()—that
can be used to perform such matching. The usage is simple
'''
print('-' * 80)
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('test.txt', '*.TXT'))
print(fnmatchcase('test.txt', '*.TXT'))
print(fnmatch('foo.py', '?oo.py'))
print(fnmatch('Dat045.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'config.ini', 'Dat2.csv', 'foo.py', 'Test.txt']
csvs = [name for name in names if fnmatch(name, 'Dat*.csv')]
for csv in csvs:
    print('Csv file : ', csv)
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
sts = [address for address in addresses if fnmatchcase(address, '* ST')]
for st in sts:
    print('St address : ', st)
print('-' * 80)
'''
Problem
    You want to match or search text for a specific pattern.
Solution
    If the text you’re trying to match is a simple literal, you can often just use the basic string
methods, such as str.find(), str.endswith(), str.startswith(), or similar. For
example:
'''
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.startswith('yeah'))
print(text.endswith('no'))
# Search for the location of the first occurrence
print(text.find('no'), '\t', text.count('no'))
'''
For more complicated matching, use regular expressions and the re module. To illustrate
the basic mechanics of using regular expressions, suppose you want to match dates
specified as digits, such as “11/27/2012.” Here is a sample of how you would do it:
'''
print('-' * 80)
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
if re.match(r'\d+/\d+/\d+', text1):
    print('Yes')
else:
    print('No')
if re.match(r'\d+/\d+/\d+', text2):
    print('Yes')
else:
    print('No')
print('-' * 80)
date_pattern = re.compile(r'\d?\d{1}/\d?\d{1}/\d{4}')
if date_pattern.match(text1):
    print('YES')
else:
    print('NO')
'''
match() always tries to find the match at the start of a string. If you want to search text
for all occurrences of a pattern, use the findall() method instead. For example:
'''
text = 'Today is 11/3/2012. PyCon starts 3/12/2013.'
dates = date_pattern.findall(text)
print(type(dates))
for date in dates:
    print('Date : ', date)
'''
When defining regular expressions, it is common to introduce capture groups by enclosing
parts of the pattern in parentheses. For example:
'''
print('-' * 80)
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
'''
Capture groups often simplify subsequent processing of the matched text because the
contents of each group can be extracted individually. For example:
'''
m = datepat.match('11/10/2021')
print(m)
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
all = datepat.findall(text)
print(all)
for day, month, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
'''
The findall() method searches the text and finds all matches, returning them as a list.
If you want to find matches iteratively, use the finditer() method instead. For example:
'''
from collections import namedtuple
DateTuple = namedtuple('DateTuple', ['day', 'month', 'year'])
for date in datepat.finditer(text):
    dt = DateTuple(*date.groups())
    # print(dt.day, dt.month, dt.year)
    print('{}-{}-{}'.format(dt.year, dt.month, dt.day))
m = datepat.match('2/12/2022adbdc')
print(m)
print(m.group())
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
m = datepat.match('2/12/2022adbdc')
print(m)
print(m.group() if m else 'Not matched')