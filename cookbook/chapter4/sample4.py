'''
Problem
    You are building custom objects on which you would like to support iteration, but would
like an easy way to implement the iterator protocol.
Solution
    By far, the easiest way to implement iteration on an object is to use a generator function.
In Recipe 4.2, a Node class was presented for representing tree structures. Perhaps you
want to implement an iterator that traverses nodes in a depth-first pattern
'''
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node-{}'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
root = Node('0')
c1 = Node('1')
c2 = Node('2')
c11 = Node('1-1')
c12 = Node('1-2')
c21 = Node('2-1')
c22 = Node('2-2')
c1.add_child(c11)
c1.add_child(c12)
c2.add_child(c21)
c2.add_child(c22)
root.add_child(c1)
root.add_child(c2)
for child in root.depth_first():
    print(child)