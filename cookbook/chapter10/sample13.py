'''
Installing Packages Just for Yourself
Problem
You want to install a third-party package, but you don’t have permission to install packages
into the system Python. Alternatively, perhaps you just want to install a package
for your own use, not all users on the system.
Solution
Python has a per-user installation directory that’s typically located in a directory such
as ~/.local/lib/python3.3/site-packages. To force packages to install in this directory, give
the --user option to the installation command. For example:
    python3 setup.py install --user
    or
    pip install --user packagename
'''