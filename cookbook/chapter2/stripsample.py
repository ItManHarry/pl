'''
Problem
    You want to strip unwanted characters, such as whitespace, from the beginning, end, or
middle of a text string.
Solution
    The strip() method can be used to strip characters from the beginning or end of a
string. lstrip() and rstrip() perform stripping from the left or right side, respectively.
By default, these methods strip whitespace, but other characters can be given. For
example:
'''
s = '  hello world   \n'
print(s, 'ok')
print(s.strip(), 'ok')
print(s.lstrip(), 'ok')
print(s.rstrip(), 'ok')
s = '-------hello==========='
print(s.lstrip('-'))
print(s.rstrip('='))
print(s.strip('-='))
'''
Be aware that stripping does not apply to any text in the middle of a string. For example:
'''
s = 'I             am          Harry'
print(s)
print(s.strip())
print(s.replace(' ', ''))
import re
print(re.sub(r'\s+', ' ', s))
print('-' * 80)
'''
Problem
    Some bored script kiddie has entered the text “pýtĥöñ” into a form on your web page
and you’d like to clean it up somehow.
Solution
    The problem of sanitizing and cleaning up text applies to a wide variety of problems
involving text parsing and data handling. At a very simple level, you might use basic
string functions (e.g., str.upper() and str.lower()) to convert text to a standard case.
Simple replacements using str.replace() or re.sub() can focus on removing or changing 
very specific character sequences. You can also normalize text using unicode
data.normalize(), as shown in Recipe 2.9.
However, you might want to take the sanitation process a step further. Perhaps, for
example, you want to eliminate whole ranges of characters or strip diacritical marks. To
do so, you can turn to the often overlooked str.translate() method. To illustrate,
suppose you’ve got a messy string such as the following:
'''
s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)
remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\r') : None # Deleted
}
a = s.translate(remap)
print(a)
import unicodedata, sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
print(len(cmb_chrs))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))
'''
Problem
    You need to format text with some sort of alignment applied.
Solution
    For basic alignment of strings, the ljust(), rjust(), and center() methods of strings
can be used. For example:
'''
print('-' * 80)
text = 'hello world'
print(text.ljust(20), 'ok')
print(text.rjust(20), 'ok')
print(text.center(20), 'ok')
print(text.ljust(20, '-'))
print(text.rjust(20, '='))
print(text.center(20, '*'))
'''
The format() function can also be used to easily align things. All you need to do is use
the <, >, or ^ characters along with a desired width. For example:
'''
print('-' * 80)
print(format(text, '<20'), 'ok')
print(format(text, '>20'), 'ok')
print(format(text, '^20'), 'ok')
print(format(text, '-<20'), 'ok')
print(format(text, '=>20'), 'ok')
print(format(text, '*^20'), 'ok')
print('{:>10}{:>10}'.format('Hello', 'World'))
print('-' * 80)
name = 'Harry'
age = 39
info = 'I am {name}, and I am {age} years old now!'.format(name=name, age=age)
print(info)
info = 'I am {}, and I am {} years old now!'.format(name, age)
print(info)
info = 'I am {1}, and I am {0} years old now!'.format(age, name)
print(info)
'''
精度控制  :.nf
'''
pi = 3.1415926
print('PI : ', pi)
print('PI is : {:.2f}'.format(pi))
print('PI is : {:.4f}'.format(pi))
print('PI is : {:.8f}'.format(pi))
'''
进制转化，b o d x 分别表示二、八、十、十六进制
'''
print('{:b}'.format(20))
print('{:o}'.format(20))
print('{:d}'.format(20))
print('{:x}'.format(20))
'''
千位分隔符：:,
'''
print('{:,}'.format(958234125.52))
print('His salary is : {:,}$.'.format(8650))
d = dict(name='Tom', age=35)
print('He is {name}, he is {age} years old.'.format(**d))
d = {'role': 'Manager', 'salary': 8525.36}
print('Role is {role}, salary is {salary:,}'.format(**d))
class Person:
    def __init__(self, role, salay):
        self.role = role
        self.salary = salay
    def __repr__(self):
        return 'Role is {}, salary is {:,}'.format(self.role, self.salary)
sm = Person('Senior Manager', 9520.36)
print(sm)
print('Role is {}, salary is {:,}'.format(sm.role, sm.salary))