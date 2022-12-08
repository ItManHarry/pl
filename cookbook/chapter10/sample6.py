'''
Reloading Modules
Problem
You want to reload an already loaded module because you’ve made changes to its source.
Solution
To reload a previously loaded module, use imp.reload(). For example:
    >>> import spam
    >>> import imp
    >>> imp.reload(spam)
    <module 'spam' from './spam.py'>
    >>>
Discussion
Reloading a module is something that is often useful during debugging and development,
but which is generally never safe in production code due to the fact that it doesn’t
always work as you expect.
Under the covers, the reload() operation wipes out the contents of a module’s underlying
dictionary and refreshes it by re-executing the module’s source code. The identity
of the module object itself remains unchanged. Thus, this operation updates the module
everywhere that it has been imported in a program.
'''