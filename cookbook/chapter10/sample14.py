'''
Creating a New Python Environment
Problem
You want to create a new Python environment in which you can install modules and
packages. However, you want to do this without installing a new copy of Python or
making changes that might affect the system Python installation.
Solution
You can make a new “virtual” environment using the pyvenv command. This command
is installed in the same directory as the Python interpreter or possibly in the Scripts
directory on Windows. Here is an example:
bash % pyvenv Spam
bash %
The name supplied to pyvenv is the name of a directory that will be created
'''