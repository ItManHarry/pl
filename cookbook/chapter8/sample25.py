'''
Creating Cached Instances
Problem
When creating instances of a class, you want to return a cached reference to a previous
instance created with the same arguments (if any).
Solution
The problem being addressed in this recipe sometimes arises when you want to ensure
that there is only one instance of a class created for a set of input arguments. Practical
examples include the behavior of libraries, such as the logging module, that only want
to associate a single logger instance with a given name.
'''
import logging
a = logging.getLogger('foo')
b = logging.getLogger('bar')
c = logging.getLogger('foo')
print('a is b ?', a is b)
print('a is c ?', a is c)
'''
To implement this behavior, you should make use of a factory function that’s separate
from the class itself.
'''
# class Spam:
#     def __init__(self, name):
#         self.name = name
# import weakref
# _spam_cache = weakref.WeakValueDictionary()
# def get_spam(name):
#     if name not in _spam_cache:
#         s = Spam(name)
#         _spam_cache[name] = s
#     else:
#         s = _spam_cache[name]
#     return s
# a = get_spam('foo')
# b = get_spam('bar')
# c = get_spam('foo')
# print('a is b ?', a is b)
# print('a is c ?', a is c)
import weakref

class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()
    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s
    def clear(self):
        self._cache.clear()
class Spam:
    manager = CachedSpamManager()
    def __init__(self, *args, **kwargs):
        raise RuntimeError('Can\'t initial the instance by init method!!!')
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
def get_spam(name):
    return Spam.manager.get_spam(name)
a = Spam._new('foo')
b = Spam._new('foo')
print('a is b ? ', a is b)