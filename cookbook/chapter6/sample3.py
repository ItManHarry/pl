'''
Parsing Simple XML Data
Problem
    You would like to extract data from a simple XML document.
Solution
    The xml.etree.ElementTree module can be used to extract data from simple XML
documents.
'''
from urllib.request import urlopen
from xml.etree.ElementTree import parse
print('start read xml resource .')
u = urlopen('https://planetpython.org/rss20.xml')
doc = parse(u)
for index, item in enumerate(doc.iterfind('channel/item')):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print('Index', index+1)
    print('\t'+title)
    print('\t'+date)
    print('\t'+link)
    print('-' * 80)
from lxml.etree import parse
u = urlopen('https://planetpython.org/rss20.xml')
doc = parse(u)
for index, item in enumerate(doc.iterfind('channel/item')):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print('LXML index : {}'.format(index+1))
    print('\t' + title)
    print('\t' + date)
    print('\t' + link)
    print('=' * 80)
print('Read XML File')
with open('rss.xml', encoding='utf-8') as f:
    doc = parse(f)
    for index, item in enumerate(doc.iterfind('clients/item')):
        name = item.findtext('name')
        phone = item.findtext('phone')
        print('\t' + name)
        print('\t' + phone)
        '''date = item.findtext('pubDate')
        link = item.findtext('link')
        print('LXML index : {}'.format(index + 1))
        print('\t' + title)
        print('\t' + date)
        print('\t' + link)'''
        print('=' * 80)