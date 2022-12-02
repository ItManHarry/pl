'''
Defining Classes Programmatically
Problem
You’re writing code that ultimately needs to create a new class object. You’ve thought
about emitting emit class source code to a string and using a function such as exec()
to evaluate it, but you’d prefer a more elegant solution.
Solution
You can use the function types.new_class() to instantiate new class objects. All you
need to do is provide the name of the class, tuple of parent classes, keyword arguments,
and a callback that populates the class dictionary with members.
'''
def __init__(self, name, shares, price):
    self.name = name
    self.shares =shares
    self.price = price
def cost(self):
    return self.shares * self.price
cls_dict = {
    '__init__': __init__,
    'cost': cost
}
import types
Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ == __name__
s = Stock('App', 50, 129.5)
print(s)
print(s.cost())