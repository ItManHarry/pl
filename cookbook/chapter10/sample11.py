'''
Loading Modules from a Remote Machine Using
Import Hooks
Problem
You would like to customize Python’s import statement so that it can transparently load
modules from a remote machine.
Solution
First, a serious disclaimer about security. The idea discussed in this recipe would be
wholly bad without some kind of extra security and authentication layer. That said, the
main goal is actually to take a deep dive into the inner workings of Python’s import
statement. If you get this recipe to work and understand the inner workings, you’ll have
a solid foundation of customizing import for almost any other purpose. With that out
of the way, let’s carry on.
'''