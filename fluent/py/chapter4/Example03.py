# Basic Encoders and Decoders
for codec in ['latin1', 'utf-8', 'utf-16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')
# Coping with UnicodeEncodeError
city = 'São Paulo'
print(city.encode('utf-8'))
print(city.encode('utf-16'))
print(city.encode('iso8859-1'))
'''
Traceback (most recent call last):
  File "D:/Development/Python/workplaces/pl/fluent/py/chapter4/Example03.py", line 9, in <module>
    print(city.encode('cp437'))
  File "c:\program files\python38\lib\encodings\cp437.py", line 12, in encode
    return codecs.charmap_encode(input,errors,encoding_map)
UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>
'''
# print(city.encode('cp437'))
# Coping the exception
'''
Way 1:The error='ignore' handler silently skips characters that cannot be encoded;
this is usually a very bad idea.
'''
print(city.encode('cp437', errors='ignore'))
'''
Way 2:When encoding, error='replace' substitutes unencodable characters with '?';
data is lost, but users will know something is amiss.
'''
print(city.encode('cp437', errors='replace'))
'''
Way 2:'xmlcharrefreplace' replaces unencodable characters with an XML entity.
'''
print(city.encode('cp437', errors='xmlcharrefreplace'))
print('-' * 80)
# Coping with UnicodeDecodeError
octets = b'Montr\xe9al'
print('Octet bytes : ', octets)
print('Decode cp1252 : ', octets.decode('cp1252'))
print('Decode iso8859-7 : ', octets.decode('iso8859-7'))
print('Decode kor8-r : ', octets.decode('koi8-r'))
'''
Traceback (most recent call last):
  File "D:/Development/Python/workplaces/pl/fluent/py/chapter4/Example03.py", line 40, in <module>
    print('Decode utf-8 : ', octets.decode('utf-8'))
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte
'''
#print('Decode utf-8 : ', octets.decode('utf-8'))
print('Decode utf-8 : ', octets.decode('utf-8', errors='replace'))
'''
UTF-8 is the default source encoding for Python 3, just as ASCII was the default for
Python 2 (starting with 2.5). If you load a .py module containing non-UTF-8 data and
no encoding declaration, you get a message like this:
SyntaxError: Non-UTF-8 code starting with '\xe1' in file ola.py on line
1, but no encoding declared; see http://python.org/dev/peps/pep-0263/
for details
Because UTF-8 is widely deployed in GNU/Linux and OSX systems, a likely scenario
is opening a .py file created on Windows with cp1252. Note that this error happens even
in Python for Windows, because the default encoding for Python 3 is UTF-8 across all
platforms.
To fix this problem, add a magic coding comment at the top of the file, as shown in
Example 4-8.
Example 4-8. ola.py: “Hello, World!” in Portuguese
# coding: cp1252
print('Olá, Mundo!')
'''