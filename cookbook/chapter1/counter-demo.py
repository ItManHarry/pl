'''
Problem
    You have a sequence of items, and you’d like to determine the most frequently occurring
items in the sequence.
Solution
    The collections.Counter class is designed for just such a problem. It even comes with
a handy most_common() method that will give you the answer.
'''
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
print('Words : ', word_counts)
top_three = word_counts.most_common(3)
print('Top three are : ', top_three)
print('Count look is : ', word_counts['look'])
print('Count look is : ', words.count('look'))
print('Eyes count is : ', word_counts['eyes'])
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print('Eyes count is : ', word_counts['eyes'])
word_counts.update(morewords)
print('Eyes count is : ', word_counts['eyes'])
more_words_counts = Counter(morewords)
combine_counts = word_counts + more_words_counts
print('Eyes count is : ', combine_counts['eyes'])
sub_counts = word_counts - more_words_counts
print('Eyes count is : ', sub_counts['eyes'])