'''
Implementing Multiple Dispatch with Function
Annotations
Problem
You’ve learned about function argument annotations and you have a thought that you
might be able to use them to implement multiple-dispatch (method overloading) based
on types. However, you’re not quite sure what’s involved (or if it’s even a good idea).
Solution
This recipe is based on a simple observation—namely, that since Python allows arguments
to be annotated, perhaps it might be possible to write code like this
'''
class Spam:
    def bar(self, x:int, y:int):
        print('Bar 1:', x, y)
    def bar(self, s:str, n:int = 0):
        print('Bar 2:', s, n)
s = Spam()
s.bar(2, 3) # Prints Bar 1: 2 3
s.bar('hello') # Prints Bar 2: hello 0