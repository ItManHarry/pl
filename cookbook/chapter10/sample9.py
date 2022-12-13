'''
Adding Directories to sys.path
Problem
You have Python code that can’t be imported because it’s not located in a directory listed
in sys.path. You would like to add new directories to Python’s path, but don’t want to
hardwire it into your code.
Solution
There are two common ways to get new directories added to sys.path. First, you can
add them through the use of the PYTHONPATH environment variable. For example:
    bash % env PYTHONPATH=/some/dir:/other/dir python3
    Python 3.3.0 (default, Oct 4 2012, 10:17:33)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sys
    >>> sys.path
    ['', '/some/dir', '/other/dir', ...]
    >>>
In a custom application, this environment variable could be set at program startup or
through a shell script of some kind.
'''
import sys
print('-' * 80)
for path in sys.path:
    print('System path : ', path)
print('-' * 80)
'''
The second approach is to create a .pth file that lists the directories like this:
    # myapplication.pth
    /some/dir
    /other/dir
This .pth file needs to be placed into one of Python’s site-packages directories, which are
typically located at /usr/local/lib/python3.3/site-packages or ~/.local/lib/python3.3/sitepackages.
On interpreter startup, the directories listed in the .pth file will be added to
sys.path as long as they exist on the filesystem. Installation of a .pth file might require
administrator access if it’s being added to the system-wide Python interpreter.
'''