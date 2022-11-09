'''
Managing Memory in Cyclic Data Structures
Problem
Your program creates data structures with cycles (e.g., trees, graphs, observer patterns,
etc.), but you are experiencing problems with memory management.
Solution
A simple example of a cyclic data structure is a tree structure where a parent points to
its children and the children point back to their parent. For code like this, you should
consider making one of the links a weak reference using the weakref library.
'''
import weakref
class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()
    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)
    def add_child(self, node):
        self.children.append(node)
        node.parent = self
    def __repr__(self):
        return 'Node {}'.format(self.value)
root = Node('Root')
print(root)
c1 = Node('C-Node-1')
c1_1 = Node('C-Node-1-1')
c1_2 = Node('C-Node-1-2')
c1.add_child(c1_1)
c1.add_child(c1_2)
c2 = Node('C-Node-2')
c2_1 = Node('C-Node-2-1')
c2_2 = Node('C-Node-2-2')
c2_3 = Node('C-Node-2-3')
c2_4 = Node('C-Node-2-4')
c2.add_child(c2_1)
c2.add_child(c2_2)
c2.add_child(c2_3)
c2.add_child(c2_4)
c3 = Node('C-Node-3')
c3_1 = Node('C-Node-3-1')
c3_2 = Node('C-Node-3-2')
c3_3 = Node('C-Node-3-3')
c3.add_child(c3_1)
c3.add_child(c3_2)
c3.add_child(c3_3)
root.add_child(c1)
root.add_child(c2)
root.add_child(c3)
print('Child {}\'s parent is {}'.format(c1, c1.parent))
print('Child {}\'s parent is {}'.format(c2, c2.parent))
print('Child {}\'s parent is {}'.format(c3, c3.parent))
for child in root.children:
    print(child)
print('-' * 80)
def show_nodes(node):
    if node.children:
        for child in node.children:
            print(child)
            show_nodes(child)
    else:
        #print('No child anymore!!!')
        return
show_nodes(root)