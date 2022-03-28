import sys
l = [1, 2, 3, 4, 5, 5, 7, 8, 9, 3, 2, 3]
it = iter(l)
for x in it:
    print(x)
'''
print('-' * 80)
it2 = iter(l)
while True:
    try:
        print(next(it2))
    except StopIteration:
        print('Iteration has been finished')
        sys.exit()
'''
print('-' * 80)
class MyIteration:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
mi = MyIteration()
i = iter(mi)
'''print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
'''
for x in i:
    print(x)
print('' * 80)
# 斐波那契数列
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10)
while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        print('-' * 80)
        sys.exit()