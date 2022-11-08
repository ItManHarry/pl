'''
Implementing the Visitor Pattern Without Recursion
Problem
You’re writing code that navigates through a deeply nested tree structure using the visitor
pattern, but it blows up due to exceeding the recursion limit. You’d like to eliminate the
recursion, but keep the programming style of the visitor pattern.
Solution
Clever use of generators can sometimes be used to eliminate recursion from algorithms
involving tree traversal or searching. In Recipe 8.21, a visitor class was presented. Here
is an alternative implementation of that class that drives the computation in an entirely
different way using a stack and generators
'''
class Node:
    pass
import types
class NodeVisitor:
    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()
        return last_result
    def _visit(self, node):
        methname = 'visit_' + type(node).__name__
        meth = getattr(self, methname, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)
    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_'+type(node).__name__))
class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand
class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
class Add(BinaryOperator):
    pass
class Sub(BinaryOperator):
    pass
class Mul(BinaryOperator):
    pass
class Div(BinaryOperator):
    pass
class Negate(BinaryOperator):
    pass
class Number(Node):
    def __init__(self, value):
        self.value = value
class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value
    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)
    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)
    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)
    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)
    def visit_Negate(self, node):
        yield -(yield node.operand)
t1 = Sub(Number(3), Number(4))
t2 = Mul(Number(2), t1)
t3 = Div(t2, Number(5))
t4 = Add(Number(1), t3)
e = Evaluator()
print(e.visit(t4))
a = Number(0)
for i in range(1, 1000000):
    a = Add(a, Number(i))
print(e.visit(a))