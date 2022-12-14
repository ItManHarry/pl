'''
Interacting with HTTP Services As a Client
Problem
You need to access various services via HTTP as a client. For example, downloading
data or interacting with a REST-based API.
Solution
For simple things, it’s usually easy enough to use the urllib.request module. For
example, to send a simple HTTP GET request to a remote service, do something like this:
'''
from urllib import request, parse
url = 'http://localhost/dict/api/get_enums/D001'
params = {'token': '1234567890ASDFZXCV程国前', 'TEST': 'FORTEST123456'}
qs = parse.urlencode(params)
u = request.urlopen(url+'?'+qs)
resp = u.read()
print(resp)
print('-' * 80)
headers = {'User-Agent': 'ie/microsoft', 'Spam': 'egg', 'X-CSRFToken': 'ImVjYmE4ODEyZjlhMzYyOTU0NTc3NzU4NTM2NzJhZGVhYjhlNjI1NmYi.Y5kauw.ZcIIz8jgg5AoMEgMdBQ0ewesTjk'}
req = request.Request(url+'?'+qs, headers=headers)
u = request.urlopen(req)
resp = u.read()
print(type(resp))
print(resp)
print('-' * 80)
'''
If your interaction with a service is more complicated than this, you should probably
look at the requests library. For example, here is equivalent requests code for the
preceding operations:
'''
import requests
rep = requests.post(url+'?'+qs, data=qs.encode('ascii'), headers=headers)
txt = rep.text
print('Text : ', txt)
con = rep.content
print('Content : ', con)
json = rep.json()
print(type(json))
if json['code']:
    options = json['options']
    for option in options:
        print(option)
else:
    print(json['message'])
