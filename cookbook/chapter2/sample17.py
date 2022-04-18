'''
Problem
    You want to replace HTML or XML entities such as &entity; or &#code; with their
corresponding text. Alternatively, you need to produce text, but escape certain characters
(e.g., <, >, or &).
Solution
    If you are producing text, replacing special characters such as < or > is relatively easy if
you use the html.escape() function.
'''
s = 'Text written by tag "<h1>This is a title</h1>"'
print(s)
import html
print(html.escape(s))
print(html.escape(s, quote=False))
s = 'Spicy Jalapeño'
print(s)
print(s.encode('ascii', errors='xmlcharrefreplace'))
'''
To replace entities in text, a different approach is needed. If you’re actually processing
HTML or XML, try using a proper HTML or XML parser first. Normally, these tools
will automatically take care of replacing the values for you during parsing and you don’t
need to worry about it.
If, for some reason, you’ve received bare text with some entities in it and you want them
replaced manually, you can usually do it using various utility functions/methods associated
with HTML or XML parsers. For example:
'''
s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
