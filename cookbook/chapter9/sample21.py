'''
Avoiding Repetitive Property Methods
Problem
You are writing classes where you are repeatedly having to define property methods that
perform common tasks, such as type checking. You would like to simplify the code so
there is not so much code repetition.
Solution
Consider a simple class where attributes are being wrapped by property methods
'''
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age =age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Name must be a string!')
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('Age must be an int!')
        self._age = value
p = Person('Harry', 39)
print('My name is {}, and I am {} years old now!'.format(p.name, p.age))
p.name = 'Tom'
p.age = 35
print('My name is {}, and I am {} years old now!'.format(p.name, p.age))
print('-' * 80)
def typed_property(name, expected_type):
    storage_name = '_' + name
    @property
    def prop(self):
        return getattr(self, storage_name)
    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}!'.format(name, expected_type))
        setattr(self, storage_name, value)
    return prop
class Human:
    name = typed_property('name', str)
    age = typed_property('age', int)
    def __init__(self, name, age):
        self.name = name
        self.age = age
h = Human('Jack', 25)
print('I am {} ,and I am {} years old.'.format(h.name, h.age))
