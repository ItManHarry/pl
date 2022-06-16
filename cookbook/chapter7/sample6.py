'''
Replacing Single Method Classes with Functions
Problem
    You have a class that only defines a single method besides __init__(). However, to
simplify your code, you would much rather just have a simple function.
Solution
    In many cases, single-method classes can be turned into functions using closures. Consider,
as an example, the following class, which allows a user to fetch URLs using a kind
of templating scheme
'''
class Person:
    def __init__(self, name):
        self.name = name
    def info(self, **kwargs):
        return 'Name : '+self.name+', age : '+kwargs['age']
#headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
#template = Request(url='http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}',headers=headers)
person = Person('Harry')
print(person.info(age='39'))
for line in person.info(age='39'):
    print(line)
def people(name):
    def info(**kwargs):
        return 'Name : '+name+', age : '+kwargs['age']
    return info
p = people('Tom')
print(p(age='39'))