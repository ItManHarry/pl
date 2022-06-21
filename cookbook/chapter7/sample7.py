'''
Carrying Extra State with Callback Functions
Problem
    You’re writing code that relies on the use of callback functions (e.g., event handlers,
completion callbacks, etc.), but you want to have the callback function carry extra state
for use inside the callback function.
Solution
    This recipe pertains to the use of callback functions that are found in many libraries
and frameworks—especially those related to asynchronous processing. To illustrate and
for the purposes of testing, define the following function, which invokes a callback
'''
def async_apply(func, args, *, callback):
    # compute result
    result = func(*args)
    # invoke callback function with result
    callback(result)
def print_result(result):
    print('Got the result {}'.format(result))
def add(x, y):
    return x + y
async_apply(add, (10, 20), callback=print_result)
async_apply(add, ('Harry', 'Jane'), callback=print_result)
'''
As you will notice, the print_result() function only accepts a single argument, which
is the result. No other information is passed in. This lack of information can sometimes
present problems when you want the callback to interact with other variables or parts
of the environment.
One way to carry extra information in a callback is to use a bound-method instead of
a simple function. For example, this class keeps an internal sequence number that is
incremented every time a result is received
'''
print('-'*80)
class ResultHandler:
    def __init__(self):
        self.sequence = 0
    def handler(self, result):
        self.sequence += 1
        print('[{}] Got : {}'.format(self.sequence, result))
'''
To use this class, you would create an instance and use the bound method handler as
the callback
'''
r = ResultHandler()
async_apply(add, (10, 20), callback=r.handler)
async_apply(add, (100, 200), callback=r.handler)
async_apply(add, (1000, 2000), callback=r.handler)
async_apply(add, (10000, 20000), callback=r.handler)
'''
As an alternative to a class, you can also use a closure to capture state. For example
'''
print('-'*80)
def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got : {}'.format(sequence, result))
    return handler
handler = make_handler()
async_apply(add, ('10', '20'), callback=handler)
async_apply(add, ('100', '200'), callback=handler)
async_apply(add, ('1000', '2000'), callback=handler)
async_apply(add, ('10000', '20000'), callback=handler)
print('-'*80)
'''
As yet another variation on this theme, you can sometimes use a coroutine to accomplish
the same thing
'''
def yield_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got : {}'.format(sequence, result))
# For a coroutine, you would use its send() method as the callback,
handler = yield_handler()
next(handler)
async_apply(add, ('A', 'B'), callback=handler.send)
async_apply(add, ('AA', 'BB'), callback=handler.send)
async_apply(add, ('AAA', 'BBB'), callback=handler.send)
async_apply(add, ('AAAA', 'BBBB'), callback=handler.send)
'''
Last, but not least, you can also carry state into a callback using an extra argument and
partial function application. For example
'''
print('-'*80)
class SequenceNO:
    def __init__(self):
        self.sequence = 0
def s_handler(result, seq):
    seq.sequence += 1
    print('[{}] Got : {}'.format(seq.sequence, result))
seq = SequenceNO()
from functools import partial
async_apply(add, ('X', 'Y'), callback=partial(s_handler, seq=seq))
async_apply(add, ('XX', 'YY'), callback=partial(s_handler, seq=seq))
async_apply(add, ('XXX', 'YYY'), callback=partial(s_handler, seq=seq))
async_apply(add, ('XXXX', 'YYYY'), callback=partial(s_handler, seq=seq))
'''
Instead of using partial(), you’ll sometimes see the same thing accomplished
with the use of a lambda
'''
print('-'*80)
seq = SequenceNO()
seq2 = SequenceNO()
async_apply(add, ('a', 'b'), callback=lambda r: s_handler(r, seq))
async_apply(add, ('aa', 'bb'), callback=lambda r: s_handler(r, seq))
async_apply(add, ('aaa', 'bbb'), callback=lambda r: s_handler(r, seq2))
async_apply(add, ('aaaa', 'bbbb'), callback=lambda r: s_handler(r, seq2))
import time, random
def gen_bill_no(prefix):
    date_str = time.strftime('%Y%m%d')
    random_num = random.randint(1000, 10000)
    return prefix+date_str+str(random_num)
bill_no = gen_bill_no('CK')
print(bill_no)