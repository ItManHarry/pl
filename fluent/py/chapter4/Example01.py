# Encoding & Decoding
'''
If you need a memory aid to help distinguish .decode()
from .encode(), convince yourself that byte sequences can be
cryptic machine core dumps while Unicode str objects are “human”
text. Therefore, it makes sense that we decode bytes to str
to get human-readable text, and we encode str to bytes for storage
or transmission
'''
s = 'café'
# The str 'café' has four Unicode characters
print(len(s))
# Encode str to bytes using UTF-8 encoding
bs = s.encode('utf-8')
# bytes literals start with a b prefix
print(bs)
# bytes b has five bytes (the code point for “é” is encoded as two bytes in UTF-8)
print(len(bs))
#  Decode bytes to str using UTF-8 encoding
sb = bs.decode('utf-8')
print(sb)
me = '冰敦敦'
bs = me.encode('utf-8')
print(bs)
print('我是:', bs.decode('utf-8'))