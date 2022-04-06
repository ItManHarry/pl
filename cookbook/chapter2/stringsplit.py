'''
Problem
    You need to split a string into fields, but the delimiters (and spacing around them) aren’t
consistent throughout the string.
Solution
    The split() method of string objects is really meant for very simple cases, and does
not allow for multiple delimiters or account for possible whitespace around the delimiters.
In cases when you need a bit more flexibility, use the re.split() method:
'''
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
sl = re.split(r'[;,\s]\s*', line)
print(sl)
'''
Problem
    You need to check the start or end of a string for specific text patterns, such as filename
extensions, URL schemes, and so on.
Solution
    A simple way to check the beginning or end of a string is to use the str.starts
with() or str.endswith() methods. For example
'''
filename = 'test.txt'
print(filename.endswith('.txt'))
url = 'https://www.baidu.com'
print(url.startswith('https:'))
'''
If you need to check against multiple choices, simply provide a tuple of possibilities to
startswith() or endswith():
'''
import os
files = os.listdir('.')
for file in files:
    print('File is : ', file)
print('Is there Python file ? ', 'Yes' if any(filename.endswith('.py') for filename in files) else 'No')
print('Is there Text file ? ', 'Yes' if any(filename.endswith('.txt') for filename in files) else 'No')
print('Is there Java file ? ', 'Yes' if any(filename.endswith('.java') for filename in files) else 'No')
print('Are there Python and Text files ? ' + 'Yes' if any(filename.endswith(('.py', '.txt')) for filename in files) else 'No')
search_file = (filename for filename in files if filename.endswith(('.py', '.txt')))
for file in search_file:
    print('File is : ', file)
from urllib.request import urlopen
url = 'http://localhost/dict/enums/e2390616ab02483dbb35cc7140e4d978'
def read_data(url):
    if url.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(url, data={}).read()
    else:
        with open(url) as f:
            return f.read()
print(read_data(url))
'''import json
from urllib import parse
data_param = {

}
data_parse = parse.urlencode(data_param)
data_b = data_parse.encode('utf-8')
res = urlopen(url=url, data={})
res_str = res.read().decode('utf-8')
print(res_str)
'''
