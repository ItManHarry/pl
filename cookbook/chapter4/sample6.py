'''
Problem
    You would like to define a generator function, but it involves extra state that you would
like to expose to the user somehow.
Solution
    If you want a generator to expose extra state to the user, don’t forget that you can easily
implement it as a class, putting the generator function code in the __iter__() method.
'''
from collections import deque
class LineHistory:
    def __init__(self, lines, history_len=1):
        self.lines = lines
        self.history = deque(maxlen=history_len)
    def __iter__(self):
        for line_no, line in enumerate(self.lines, 1):
            self.history.append((line_no, line))
            yield line
    def clear(self):
        self.history.clear()
import os
basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
with open(os.path.join(basedir, 'files\\data.txt')) as f:
    lines = LineHistory(f)
    for line in lines:
        if 'Python' in line:
            #print(line)
            for line_no, hline in lines.history:
                print('{}:{}'.format(line_no, hline), end='')
            print('-' * 80)