'''
Turning a Dictionary into XML
Problem
    You want to take the data in a Python dictionary and turn it into XML.
Solution
    Although the xml.etree.ElementTree library is commonly used for parsing, it can also
be used to create XML documents.
'''
from xml.etree.ElementTree import Element, tostring
def dict_to_xml(tag, dic):
    e = Element(tag)
    e.set('id', '20112004')
    for key, value in dic.items():
        child = Element(key)
        child.text = str(value)
        e.append(child)
    return e
dic = {
    'Name': 'Harry',
    'Age': 25,
    'Gender': 'M'
}
e = dict_to_xml('employee', dic)
print(tostring(e))
with open('data.xml', 'w') as f:
    f.write(tostring(e).decode('utf-8'))