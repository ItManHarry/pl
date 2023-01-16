from urllib import request, parse
url = 'http://localhost/api_user/get_info/57a5e9d2bf584184a89f688336f20ebc'
params = {'token': '1234567890ASDFZXCV程国前', 'TEST': 'FORTEST123456'}
qs = parse.urlencode(params)
u = request.urlopen(url+'?'+qs)
resp = u.read()
print(resp)
print('-' * 80)