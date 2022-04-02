'''
Problem
    You want to make a dictionary that is a subset of another dictionary.
Solution
    This is easily accomplished using a dictionary comprehension.
'''
import random
prices = {'key'+str(key): random.random() * 1000 for key in range(10000000)}
from time import time
st = time()
'''
The best way!!!
'''
sub = {key: value for key, value in prices.items() if value > 500}
et = time()
#print('Parent : ', prices)
#print('Sub : ', sub)
print('Time used 1 : ', (et - st))
st = time()
sub = dict((key, value) for key, value in prices.items() if value > 500)
et = time()
print('Time used 2 : ', (et - st))