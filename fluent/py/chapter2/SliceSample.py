s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])
print('' * 80)
invoice = """
... 0.....6.................................40........52...55........
... 1909 Pimoroni PiBrella $17.50 3 $52.50
... 1489 6mm Tactile Switch x20 $4.95 2 $9.90
... 1510 Panavise Jr. - PV-201 $28.00 1 $28.00
... 1601 PiTFT Mini Kit 320x240 $34.95 1 $34.95
... """
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoice.split('\n')[2:]
for item in line_items:
    print('Item : ', item)
    print('Unit price : %s, description %s' %(item[UNIT_PRICE], item[DESCRIPTION]))
    print('-' * 80)
l = list(range(10))
print('List is ', l)
print('-' * 80)
l[2:5] = [20, 30]
print('Now the list is : ', l)
print('-' * 80)
del l[5:7]
print('After delete the list is : ', l)
print('-' * 80)
# l[2:5] = 100 TypeError: can only assign an iterable
l[2:5] = [100]
print('Add one element : ', l)
l = [1, 2, 3]
l * 5 # This will generate a new list
print('Operand l is : ', l)
print('Multi operand : ', l * 5)
s = 'abc'
s * 5
print('Operand l is : ', s)
print('Multi operand : ', s * 5)
'''
Lists of lists
'''
print('-' * 80)
board1 = [['_'] * 3 for i in range(3)]
print('Board 1 is : ', board1)
board2 = [['_'] * 3] * 3
print('Board 2 is : ', board2)
print('Change element now ')
board1[1][2] = 'X'
board2[1][2] = 'Y'
print('After change board 1 is : ', board1)
print('After change board 2 is : ', board2)
l1 = [1, 2, 3]
id1 = id(l1)
print('ID of l1 is : ', id(l1))
l1 *= 2
id2 = id(l1)
print('Before the multiplication the list id is : ', id1, ', after the multiplication the list id is : ', id2, '. Result is : ', 'ID is not changed !!!' if id1 == id2 else 'ID is changed!!!')
t1 = (1, 2, 3)
id1 = id(t1)
t1 *= 2
id2 = id(t1)
print('Before the multiplication the tuple id is : ', id1, ', after the multiplication the tuple id is : ', id2, '. Result is : ', 'ID is not changed !!!' if id1 == id2 else 'ID is changed!!!')
t = (1, 2, 3, [10, 20])
t[3] += [30, 40]
print(t)