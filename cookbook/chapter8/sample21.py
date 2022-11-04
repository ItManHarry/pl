'''
Implementing the Visitor Pattern
Problem
You need to write code that processes or navigates through a complicated data structure
consisting of many different kinds of objects, each of which needs to be handled in a
different way. For example, walking through a tree structure and performing different
actions depending on what kind of tree nodes are encountered.
Solution
The problem addressed by this recipe is one that often arises in programs that build
data structures consisting of a large number of different kinds of objects. To illustrate,
suppose you are trying to write a program that represents mathematical expressions.
To do that, the program might employ a number of classes, like this
'''
class Node:
    pass
class UnaryNode(Node):
    def __init__(self, operand):
        self.operand = operand

class BinaryNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
class Add(BinaryNode):
    pass
class Sub(BinaryNode):
    pass
class Mul(BinaryNode):
    pass
class Div(BinaryNode):
    pass
class Negate(BinaryNode):
    pass
class Number(Node):
    def __init__(self, value):
        self.value = value
# Representation of 1 + 2 * (3 - 4) / 5
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)
class NodeVisitor:
    def visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)
    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))
class Evalutor(NodeVisitor):
    def visit_Number(self, node):
        return node.value
    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)
    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)
    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)
    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)
    def visit_Negate(self, node):
        return -node.operand
e = Evalutor()
r = e.visit(t4)
print(r)