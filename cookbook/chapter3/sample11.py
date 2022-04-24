'''
Problem
    You want to pick random items out of a sequence or generate random numbers.
Solution
    The random module has various functions for random numbers and picking random
items. For example, to pick a random item out of a sequence, use random.choice():
'''
import random
l = [1, 2, 3, 4, 5, 6, 7]
'''
single element
'''
print(random.choice(l))
'''
multiply elements
'''
print(random.sample(l, 2))
print(random.sample(l, 3))
'''
If you simply want to shuffle items in a sequence in place, use random.shuffle():
'''
random.shuffle(l)
print(l)
random.shuffle(l)
print(l)
'''
To produce random integers, use random.randint(x, y):
include x and y
'''
n = random.randint(10, 100)
print('n is : ', n)
'''
To produce uniform floating-point values in the range 0 to 1, use random.random():
'''
f = random.random()
print(f)
'''
To get N random-bits expressed as an integer, use random.getrandbits():
'''
b = random.getrandbits(200)
print('b is : ', b)