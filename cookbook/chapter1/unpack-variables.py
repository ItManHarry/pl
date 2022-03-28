'''
Any sequence (or iterable) can be unpacked into variables using a simple assignment
operation. The only requirement is that the number of variables and structure match
the sequence
'''
p = (4, 5)
x, y = p
print('x is : ', x, ' y is : ', y)
data = ['Harry', 50, 91.1, (2022, 3, 22)]
name, shares, price, date = data
print('Name : ', name)
print('Shares : ', shares)
print('Price : ', price)
print('Date : ', date)
'''
Unpacking actually works with any object that happens to be iterable, not just tuples or
lists. This includes strings, files, iterators, and generators.
'''
a, b, c, d, e = 'Hello'
print('a is : ', a)
print('b is : ', b)
print('c is : ', c)
print('d is : ', d)
print('e is : ', e)
'''
When unpacking, you may sometimes want to discard certain values. Python has no
special syntax for this, but you can often just pick a throwaway variable name for it.
However, make sure that the variable name you pick isn’t being used for something else
already.
'''
_, shares, price, _ = data
print('Share : ', shares, ', price : ', price)
'''
Problem
    You need to unpack N elements from an iterable, but the iterable may be longer than N
elements, causing a “too many values to unpack” exception
Solution
    Python “star expressions” can be used to address this problem.
'''
records = ('Tom', 'tom@ds.com', '13785264004', '0535-562385')
name, email, *contacts = records
print('Name : ', name)
print('Email : ', email)
print('Contacts : ', contacts)
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
avg = sum(trailing) / len(trailing)
print('Average : ', avg, ' vs current : ', current)
records = [
    ('a', 1, 2),
    ('b', 'AAA'),
    ('b', 'BBB'),
    ('a', 10, 20),
]
def do_a(x, y):
    print('x is : ', x, ', y is : ', y)
def do_b(s):
    print('Str is : ', s)
for key, *args in records:
    if key == 'a':
        do_a(*args)
    elif key =='b':
        do_b(*args)
'''
Star unpacking can also be useful when combined with certain kinds of string processing
operations, such as splitting.
'''
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print('Name : ', uname)
print('Home : ', homedir)
print('Sh is : ', sh)
print('Other fields : ', fields)
'''
Sometimes you might want to unpack values and throw them away. You can’t just specify
a bare * when unpacking, but you could use a common throwaway variable name, such
as _ or ign (ignored)
'''
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*ign, year) = record
print('Name : ', name)
print('Year : ', year)
head, *tails = [10, 5, 20, 24, 49, 100]
print('head : ', head)
print('tails : ', tails)
def sum(items):
    head, *tails = items
    return head + sum(tails) if tails else head
data = [10, 5, 20, 24, 49, 100]
print('Sum is : ', sum(data))
all = 0
for i in data:
    all += i
print('Sum is : ', all)