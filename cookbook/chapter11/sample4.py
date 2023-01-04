from datetime import datetime, time, date
past = '2021-11-19 12:20:10'
now = datetime.now()
print(now)
pst = datetime.strptime(past, '%Y-%m-%d %H:%M:%S')
date_delta = (now - pst).days
print(past)
print('Delta days : ', round(date_delta/365, ndigits=1))
s = '1.2'
try:
    print(float(s))
except:
    print('s is not a number!')
dt = date.today()
print(type(dt), dt)
dtt = datetime.combine(dt, time())
print(type(dtt), dtt)
dt = dtt.date()
print(type(dt), dt)