'''
Problem
    You have built a custom container object that internally holds a list, tuple, or some other
iterable. You would like to make iteration work with your new container.
Solution
    Typically, all you need to do is define an __iter__() method that delegates iteration to
the internally held container.
'''
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    @property
    def is_leaf(self):
        return False if self._children else True
    def __repr__(self):
        return 'Node-{}'.format(self._value)
    def add_child(self, node):
        self._children.append(node)
    def __iter__(self):
        return iter(self._children)
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
for n in root:
    print(n)
print('-' * 80)
# 递归打印子节点
def print_node(node):
    print(node)
    if node.is_leaf:
        return
    else:
        for child in node:
            print_node(child)
print_node(root)