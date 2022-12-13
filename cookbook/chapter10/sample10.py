'''
Importing Modules Using a Name Given in a String
Problem
You have the name of a module that you would like to import, but it’s being held in a
string. You would like to invoke the import command on the string.
Solution
Use the importlib.import_module() function to manually import a module or part of
a package where the name is given as a string. For example:
    >>> import importlib
    >>> math = importlib.import_module('math')
    >>> math.sin(2)
    0.9092974268256817
    >>> mod = importlib.import_module('urllib.request')
    >>> u = mod.urlopen('http://www.python.org')
    >>>
import_module simply performs the same steps as import, but returns the resulting
module object back to you as a result. You just need to store it in a variable and use it
like a normal module afterward.
If you are working with packages, import_module() can also be used to perform relative
imports. However, you need to give it an extra argument. For example:
    import importlib
    # Same as 'from . import b'
    b = importlib.import_module('.b', __package__)
'''