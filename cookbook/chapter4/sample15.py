'''
Problem
    You have a collection of sorted sequences and you want to iterate over a sorted sequence
of them all merged together.
Solution
    The heapq.merge() function does exactly what you want
'''
import heapq
l1 = [1, 4, 7, 10]
l2 = [2, 5, 8, 13]
for i in heapq.merge(l1, l2):
    print(i)