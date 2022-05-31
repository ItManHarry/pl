'''
Parsing, Modifying, and Rewriting XML
Problem
    You want to read an XML document, make changes to it, and then write it back out as
XML.
Solution
    The xml.etree.ElementTree module makes it easy to perform such tasks. Essentially,
you start out by parsing the document in the usual way.
'''
from xml.etree.ElementTree import parse, Element, tostring
doc = parse('pred.xml')
root = doc.getroot()
print(tostring(root))
root.remove(root.find('sri'))
root.remove(root.find('cr'))
nm_index = list(root).index(root.find('nm'))
print(nm_index)
e = Element('spam')
e.text = 'This is a test element'
e.set('id', '000000')
root.insert(2, e)
doc.write('new_pred.xml', xml_declaration=True)