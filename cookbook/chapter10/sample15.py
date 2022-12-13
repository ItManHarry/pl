'''
Distributing Packages
Problem
You’ve written a useful library, and you want to be able to give it away to others.
Solution
If you’re going to start giving code away, the first thing to do is to give it a unique name
and clean up its directory structure. For example, a typical library package might look
something like this:
projectname/
README.txt
Doc/
documentation.txt
projectname/
__init__.py
foo.py
bar.py
utils/
__init__.py
spam.py
grok.py
examples/
helloworld.py
...
To make the package something that you can distribute, first write a setup.py file that
looks like this:
# setup.py
from distutils.core import setup
setup(name='projectname',
version='1.0',
author='Your Name',
author_email='you@youraddress.com',
url='http://www.you.com/projectname',
packages=['projectname', 'projectname.utils'],
)
Next, make a file MANIFEST.in that lists various nonsource files that you want to include
in your package:
# MANIFEST.in
include *.txt
recursive-include examples *
recursive-include Doc *
Make sure the setup.py and MANIFEST.in files appear in the top-level directory of your
package. Once you have done this, you should be able to make a source distribution by
typing a command such as this:
% bash python3 setup.py sdist
This will create a file such as projectname-1.0.zip or projectname-1.0.tar.gz, depending
on the platform. If it all works, this file is suitable for giving to others or uploading to
the Python Package Index.
'''