'''
Reading Datafiles Within a Package
Problem
Your package includes a datafile that your code needs to read. You need to do this in the
most portable way possible.
Solution
Suppose you have a package with files organized as follows:
    mypackage/
        __init__.py
        somedata.dat
        spam.py
Now suppose the file spam.py wants to read the contents of the file somedata.dat. To do
it, use the following code:
    # spam.py
    import pkgutil
    data = pkgutil.get_data(__package__, 'somedata.dat')
The resulting variable data will be a byte string containing the raw contents of the file.
'''
import pkgutil
data = pkgutil.get_data(__package__, 'data.txt')
print(data)
