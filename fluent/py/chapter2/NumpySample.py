import numpy
a = numpy.arange(12)
print('Array is : ', a)
print('Type is : ', type(a))
print('Array shape is : ', a.shape)
a.shape = 3, 4
print(a)
print(a[2])
print('-' * 80)
for array in a:
    print(array)
print('-' * 80)
print(a[2])
print('-' * 80)
print(a[2, 1])
print('-' * 80)
print(a[:, 1])
print('-' * 80)
print(a.transpose())
print('-' * 80)
print(a)