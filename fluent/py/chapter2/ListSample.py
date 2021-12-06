symbols = '@#$%^&'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
for code in codes:
    print('Code is : ', code)
print('-' * 80)
codes = [ord(symbol) for symbol in 'abcdefg']
for code in codes:
    print('Code is : ', code)
print('-' * 80)
codes = [ord(c) for c in 'abcdefg' if ord(c) <= 100]
for code in codes:
    print('Code is : ', code)
print('-' * 80)
codes = list(filter(lambda c: c < 100, map(ord, 'abcdefg')))
for code in codes:
    print('Code is : ', code)
list_2d = [[i, j] for i in range(5) for j in range(10)]
print(list_2d)
symbols = '$@%#^&*'
t = tuple(ord(symbol) for symbol in symbols)
print('Tuple is : ', t)
import array
arr = array.array('I', (ord(symbol) for symbol in symbols))
print('Array is : ', arr)
colors = ['black', 'white']
sizes = ['S', 'M', 'L', 'XL', 'XXL']
shirts = ['%s %s' %(c, s) for c in colors for s in sizes]
for shirt in shirts:
    print('Shirt : ', shirt)
'''
Tuple for data storage
'''
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
print('City : ', city, ' year ', year, ' pop ', pop, ' chg ', chg, 'area ', area)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342564'), ('ESP', 'XDA205856')]
'''
The % formatting operator understands tuples and treats each item as a separate
field.
'''
for passport in traveler_ids:
    print('%s/%s' % passport)
'''
The for loop knows how to retrieve the items of a tuple separately—this is called
“unpacking.” Here we are not interested in the second item, so it’s assigned to
_, a dummy variable
'''
for county, _ in traveler_ids:
    print(county)
for country, id in traveler_ids:
    print('Country %s , id is %s' %(country, id))
'''
    divmod() 函数返回当参数 1 除以参数 2 时包含商和余数的元组
'''
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
'''
Sometimes when we only care about certain parts of a tuple when unpacking, a dummy
variable like _ is used as placeholder, as in the preceding example
'''
import os
_, filename = os.path.split('/home/harry/.ssh/idra.pub')
print('File name is : ' + filename)
'''
Using * to grab excess items
'''
a, b, *rest = range(5)
print(a)
print(b)
print(rest)
a, b, *rest = range(3)
print(a)
print(b)
print(rest)
a, b, *rest = range(2)
print(a)
print(b)
print(rest)
a, b, c = [1, 2, 3]
print(a, b, c)
a, *body, c, d = range(5)
print(a)
print(body)
print(c)
print(d)
*head, b, c, d = range(5)
print(head)
print(b)
print(c)
print(d)
*head, b, c, d = range(3)
print(head)
print(b)
print(c)
print(d)
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),   #1
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:    #2
    if longitude <= 0:  #3
        print(fmt.format(name, latitude, longitude))
#1 Each tuple holds a record with four fields, the last of which is a coordinate pair.
#2 By assigning the last field to a tuple, we unpack the coordinates
#3 if longitude <= 0: limits the output to metropolitan areas in the Western hemisphere
'''
As designed, tuples are very handy. But there is a missing feature when using them as
records: sometimes it is desirable to name the fields. That is why the namedtuple function
was invented
'''
from collections import namedtuple
'''
Two parameters are required to create a named tuple: a class name and a list of
field names, which can be given as an iterable of strings or as a single spacedelimited
string  
'''
City = namedtuple('City', 'name country population coordinates')
'''
Data must be passed as positional arguments to the constructor (in contrast, the
tuple constructor takes a single iterable)
'''
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
'''
You can access the fields by name or position
'''
print('City name : ', tokyo.name)
print('Country : ', tokyo[1])
print('Population : ', tokyo.population)
print('Latitude and longitude : ', tokyo[3])
'''
A named tuple type has a few attributes in addition to those inherited from tuple.
Example 2-10 shows the most useful: the _fields class attribute, the class method
_make(iterable), and the _asdict() instance method
'''
#_fields is a tuple with the field names of the class
print(City._fields)
LatLong = namedtuple('LatLong', ['lat', 'long'])
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.643889, 77.208889))
beijing_data = ('BeiJin', 'CH', 25.965, (36.658594, 85.695623))
#_make() allow you to instantiate a named tuple from an iterable; City(*delhi_data) would do the same
delhi = City._make(delhi_data)
beijing = City(*beijing_data)
#_asdict() returns a collections.OrderedDict built from the named tuple instance. That can be used to produce a nice display of city data
for key, value in delhi._asdict().items():
    print('Key is : ', key, ', value is : ', value)
for key, value in beijing._asdict().items():
    print('Key is : ', key, ', value is : ', value)