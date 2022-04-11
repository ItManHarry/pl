'''
Problem
    You’re trying to match a text pattern using regular expressions, but it is identifying the
longest possible matches of a pattern. Instead, you would like to change it to find the
shortest possible match.
Solution
    This problem often arises in patterns that try to match text enclosed inside a pair of
starting and ending delimiters (e.g., a quoted string). To illustrate, consider this example
'''
import re
str_pat = re.compile(r'\"(.*)\"')
s1 = 'Computer says "no."'
all = str_pat.findall(s1)
print(all)
s2 = 'Computer says "no.", and Phone says "yes."'
print(str_pat.findall(s2))
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(s2))
'''
Problem
    You’re trying to match a block of text using a regular expression, but you need the match
to span multiple lines.
Solution
    This problem typically arises in patterns that use the dot (.) to match any character but
forget to account for the fact that it doesn’t match newlines. For example, suppose you
are trying to match C-style comments:
'''
print('-' * 80)
comment = re.compile(r'/\*(.*?)\*/')
c1 = '/* this is a comment */'
c2 = '''
    /*
        this is a 
        multiline comment
    */
'''
print(comment.findall(c1))
print(comment.findall(c2))
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(c2))
comment = re.compile(r'/\*(.*?)\*/', flags=re.DOTALL)
print(comment.findall(c2))
'''
Problem
    You’re working with Unicode strings, but need to make sure that all of the strings have
the same underlying representation.
Solution
    In Unicode, certain characters can be represented by more than one valid sequence of
code points. To illustrate, consider the following example:
'''
print('-' * 80)
s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1, ' length : ', len(s1))
print(s2, ' length : ', len(s2))
print(s1 == s2)
'''
Having multiple representations is a problem for programs that compare strings. In
order to fix this, you should first normalize the text into a standard representation using
the unicodedata module:
'''
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1, ' length : ', len(t1), ' ascii : ', ascii(t1))
print(t2, ' length : ', len(t2), ' ascii : ', ascii(t2))
print(t1 == t2)
t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)
print(t1, ' length : ', len(t1), ' ascii : ', ascii(t1))
print(t2, ' length : ', len(t2), ' ascii : ', ascii(t2))
print(t1 == t2)
s = '\ufb01' # A single character
print(s)
print(unicodedata.normalize('NFD', s))
print(unicodedata.normalize('NFKD', s))
print(unicodedata.normalize('NFKC', s))