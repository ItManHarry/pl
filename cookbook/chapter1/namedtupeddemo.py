'''
Problem
    You have code that accesses list or tuple elements by position, but this makes the code
somewhat difficult to read at times. You’d also like to be less dependent on position in
the structure, by accessing the elements by name.
Solution
    collections.namedtuple() provides these benefits, while adding minimal overhead
over using a normal tuple object. collections.namedtuple() is actually a factory
method that returns a subclass of the standard Python tuple type. You feed it a type
name, and the fields it should have, and it returns a class that you can instantiate, passing
in values for the fields you’ve defined, and so on.
'''
from collections import namedtuple
SubDescriber = namedtuple('SubDescriber', ['address', 'joined'])
sub = SubDescriber('jack@doosan.com', '2022-04-02')
print(len(sub))
print(sub.address)
print(sub.joined)
address, joined = sub
print(address)
print(joined)
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for record in records:
        s = Stock(*record)
        total += s.shares * s.price
    return total
data = (('AAA', 100, 10), ('BBB', 120, 10), ('CCC', 80, 10), ('DDD', 68, 10))
total = compute_cost(data)
print('Total is : ', total)