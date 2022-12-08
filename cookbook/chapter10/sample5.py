'''
Making Separate Directories of Code Import Under a Common Namespace
Problem
You have a large base of code with parts possibly maintained and distributed by different
people. Each part is organized as a directory of files, like a package. However, instead
of having each part installed as a separated named package, you would like all of the
parts to join together under a common package prefix.
Solution
Essentially, the problem here is that you would like to define a top-level Python package
that serves as a namespace for a large collection of separately maintained subpackages.
This problem often arises in large application frameworks where the framework developers
want to encourage users to distribute plug-ins or add-on packages.
To unify separate directories under a common namespace, you organize the code just
like a normal Python package, but you omit __init__.py files in the directories where
the components are going to join together. To illustrate, suppose you have two different
directories of Python code like this:
'''
import sys
sys.path.extend(['dp1', 'dp2'])
import spam.blash
import spam.gram
b = spam.blash
b