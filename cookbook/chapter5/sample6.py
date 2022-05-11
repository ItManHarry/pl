'''
Performing I/O Operations on a String
Problem
    You want to feed a text or binary string to code that’s been written to operate on filelike
objects instead.
Solution
    Use the io.StringIO() and io.BytesIO() classes to create file-like objects that operate
on string data.
'''
import io
s = io.StringIO()
s.write('Hello world\n')
print('This is age test', file=s)
print(s.getvalue())
print('-' * 80)
s = io.BytesIO()
s.write(b'hello world')
print(s.getvalue())