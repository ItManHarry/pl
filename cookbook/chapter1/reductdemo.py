'''
Problem
    You need to execute a reduction function (e.g., sum(), min(), max()), but first need to
transform or filter the data.
Solution
    A very elegant way to combine a data reduction and a transformation is to use a
generator-expression argument. For example, if you want to calculate the sum of
squares, do the following:
'''
data = [1, 2, 3, 4, 5]
sum_square = sum(x * x for x in data)
print('Sum square is : ', sum_square)
stock = ('ACME', 100, 125.25)
print(','.join(str(x) for x in stock))
portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_share = min(s['shares'] for s in portfolio)
print('Mini share is : ', min_share)