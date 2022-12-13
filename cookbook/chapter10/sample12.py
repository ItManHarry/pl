'''
Patching Modules on Import
Problem
You want to patch or apply decorators to functions in an existing module. However, you
only want to do it if the module actually gets imported and used elsewhere.
Solution
The essential problem here is that you would like to carry out actions in response to a
module being loaded. Perhaps you want to trigger some kind of callback function that
would notify you when a module was loaded.
'''
