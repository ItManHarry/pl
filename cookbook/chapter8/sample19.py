'''
Extending Classes with Mixins
Problem
You have a collection of generally useful methods that you would like to make available
for extending the functionality of other class definitions. However, the classes where
the methods might be added aren’t necessarily related to one another via inheritance.
Thus, you can’t just attach the methods to a common base class.
Solution
The problem addressed by this recipe often arises in code where one is interested in the
issue of class customization. For example, maybe a library provides a basic set of classes
along with a set of optional customizations that can be applied if desired by the user.
'''
class LoggedMappingMixin:
    __slots__ = ()

    def __getitem__(self, item):
         print('Getting : ' + str(item))
         return super().__getitem__(item)

    def __setitem__(self, key, value):
         print('Setting {} = {!r}'.format(key, value))
         return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('Delete ' + str(key))
        return super().__delitem__(key)
class SetOnceMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + ' key already set')
        return super().__setitem__(key, value)


class StringKeyMappingMixin:
    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError('Key must be string')
        return super().__setitem__(key, value)

class LoggedDict(LoggedMappingMixin, dict):
    pass
ld = LoggedDict()
ld['x'] = 100
print(ld['x'])
from collections import defaultdict, OrderedDict
class SetOnceMappingDict(SetOnceMappingMixin, defaultdict):
    pass
sd = SetOnceMappingDict(list)
sd['x'].append(10)
sd['x'].append(20)
sd['x'].append(30)
sd['x'].append(100)
sd['y'].append(200)
'''
Traceback (most recent call last):
  File "D:\Development\Python\workplaces\pl\cookbook\chapter8\sample19.py", line 58, in <module>
    sd['x'] = 100
  File "D:\Development\Python\workplaces\pl\cookbook\chapter8\sample19.py", line 32, in __setitem__
    raise KeyError(str(key) + ' key already set')
KeyError: 'x key already set'
'''
# sd['x'] = 100
class StringMappingDict(StringKeyMappingMixin, SetOnceMappingMixin, OrderedDict):
    pass
sm = StringMappingDict()
sm['x'] = 23
'''
Traceback (most recent call last):
  File "D:\Development\Python\workplaces\pl\cookbook\chapter8\sample19.py", line 63, in <module>
    sm[52] = 100
  File "D:\Development\Python\workplaces\pl\cookbook\chapter8\sample19.py", line 41, in __setitem__
    raise KeyError('Key must be string')
KeyError: 'Key must be string'
'''
# sm[52] = 100