'''
Decoding and Encoding Base64
Problem
    You need to decode or encode binary data using Base64 encoding.
Solution
    The base64 module has two functions—b64encode() and b64decode()—that do exactly
what you want
'''
import base64
s = 'test'.encode('utf-8')
a = base64.b64encode(s)
print(a)
s = base64.b64decode(a)
print(s.decode('utf-8'))