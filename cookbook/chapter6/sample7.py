'''
Decoding and Encoding Hexadecimal Digits
Problem
    You need to decode a string of hexadecimal digits into a byte string or encode a byte
string as hex.
Solution
    If you simply need to decode or encode a raw string of hex digits, use the binascii
module.
'''
import binascii
s = b'hello'
h = binascii.b2a_hex(s)
print(h)
# back
s = binascii.a2b_hex(h)
print(s)
# Similar functionality can also be found in the base64 module. For example
import base64
s = b'harry'
h = base64.b16encode(s)
print(h)
# back
s = base64.b16decode(h)
print(s.decode('utf-8'))