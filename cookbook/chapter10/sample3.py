'''
Importing Package Submodules Using Relative
Names
Problem
You have code organized as a package and want to import a submodule from one of the
other package submodules without hardcoding the package name into the import
statement.
Solution
To import modules of a package from other modules in the same package, use a packagerelative
import. For example, suppose you have a package mypackage organized as follows
on the filesystem:
    mypackage/
        __init__.py
        A/
            __init__.py
            spam.py
            grok.py
        B/
            __init__.py
            bar.py
If the module mypackage.A.spam wants to import the module grok located in the same
directory, it should include an import statement like this:
    # mypackage/A/spam.py
    from . import grok
If the same module wants to import the module B.bar located in a different directory,
it can use an import statement like this:
    # mypackage/A/spam.py
    from ..B import bar
Both of the import statements shown operate relative to the location of the spam.py file
and do not include the top-level package name.
'''