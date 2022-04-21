'''
Problem
    You have a byte string and you need to unpack it into an integer value. Alternatively,
you need to convert a large integer back into a byte string.
Solution
    Suppose your program needs to work with a 16-element byte string that holds a 128-
bit integer value.
'''
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print('Length of the data : ', len(data))
'''
To interpret the bytes as an integer, use int.from_bytes(), and specify the byte ordering
like this:
'''
print('Little data from bytes : ', int.from_bytes(data, 'little'))
print('Big data from bytes : ', int.from_bytes(data, 'big'))
'''
To convert a large integer value back into a byte string, use the int.to_bytes() method,
specifying the number of bytes and the byte order.
'''
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'little'))
print(x.to_bytes(16, 'big'))