"""
Given a set of non-empty words, find the top K frequent words

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.

"""
from collections import Counter
def top_K_frequent_words(words, k):
    hash_map = Counter(words)
    # Here -ve sign signifies that you want to order values in reverse - 1st priority
           # then the key - which is second priority
    result = sorted(hash_map, key=lambda x:(-hash_map[x], x))
    return result[:k]

words = ["i", "love", "coding", "i", "love", "hello"]
result = top_K_frequent_words(words, 3)
print(result)