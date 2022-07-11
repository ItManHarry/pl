'''
Extending a Property in a Subclass
Problem
    Within a subclass, you want to extend the functionality of a property defined in a parent
class.
Solution
    Consider the following code, which defines a property
'''
class Person:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Need a string!')
        self._name = name
    @name.deleter
    def name(self):
        raise AttributeError('Can\'t delete this attribute!')
p = Person('Harry')
print(p.name)
class Child(Person):
    @property
    def name(self):
        print('Get name')
        return super().name
    @name.setter
    def name(self, name):
        print('Set name to ', name)
        super(Child, Child).name.__set__(self, name)
    @name.deleter
    def name(self):
        print('Delete the name')
        super(Child, Child).name.__delete__(self)
c = Child('Jack')
print(c.name)
c.name = 'Tom'
print(c.name)
# c.name = 43
# print(c.name)
del c.name