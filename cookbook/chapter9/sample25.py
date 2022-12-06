'''
Disassembling Python Byte Code
Problem
You want to know in detail what your code is doing under the covers by disassembling
it into lower-level byte code used by the interpreter.
Solution
The dis module can be used to output a disassembly of any Python function
'''
def count_down(n):
    while n > 0:
        print('T-minus : ', n)
        n -= 1
    print('Blastoff')
import dis
dis.dis(count_down)