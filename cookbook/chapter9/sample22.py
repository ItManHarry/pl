'''
Defining Context Managers the Easy Way
Problem
You want to implement new kinds of context managers for use with the with statement.
Solution
One of the most straightforward ways to write a new context manager is to use the
@contextmanager decorator in the contextlib module.
'''
import time
from contextlib import contextmanager
@contextmanager
def time_this(label):
    start = time.time()
    try:
        yield
    except:
        pass
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))
with time_this('counting'):
    n = 1000000
    while n > 0:
        n -= 1
@contextmanager
def list_transaction(org_list):
    working = list(org_list)
    yield working
    org_list[:] = working
items = [1, 2, 3]
with list_transaction(items) as working:
    working.append(4)
    working.append(5)
print(items)