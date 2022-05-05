'''
Problem
    You want to iterate over a sequence, but would like to keep track of which element of
the sequence is currently being processed.
Solution
    The built-in enumerate() function handles this quite nicely
'''
l = ['a', 'b', 'c', 'd']
for index, element in enumerate(l):
    print('Index is : ', index, ', element is : ', element)