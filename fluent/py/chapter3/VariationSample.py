from collections import Counter, UserDict
ct = Counter('abcdefadbeftfagef')
print(ct)
class StrKeyDict(UserDict):

    def __missing__(self, key):
         if isinstance(key, str):
             raise KeyError(key)
         return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, value):
        self.data[str(key)] = value
skd = StrKeyDict()
skd['a'] = 10
print(skd)
'''
Since Python 3.3, the types module provides a wrapper class called MappingProxy
Type, which, given a mapping, returns a mappingproxy instance that is a read-only but
dynamic view of the original mapping. This means that updates to the original mapping
can be seen in the mappingproxy, but changes cannot be made through it
'''
from types import MappingProxyType
d = {'a': 100}
proxy = MappingProxyType(d)
print(proxy)
for k, v in proxy.items():
    print('k is %s , v is : %s ' %(k, v))
print('-' * 80)
d['b'] = 200
for k, v in proxy.items():
    print('k is %s , v is : %s ' %(k, v))