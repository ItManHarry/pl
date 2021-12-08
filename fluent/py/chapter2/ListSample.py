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
shirt_list = [[c, s] for c in colors for s in sizes]
print('Shirt list is : ', shirt_list)
for shirt in shirt_list:
    print('Shirt : ', shirt)