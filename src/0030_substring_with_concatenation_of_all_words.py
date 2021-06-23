"""
Substring with concatenation of all words

You are given a string 's' and an array of string 'words' of the same length

return all the starting indices of substring(s) in s that is a concatenation of each in 'words' exactly once,
in any order and without any intervening characters

You can return the answer in any order.
"""

class TrieNode:
    def __init__(self, end=None, children=None):
        self.end = end
        if children is None:
            children = {}
        self.children = children

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        ptr = self.root
        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = TrieNode()
            ptr = ptr.children[ch]
        ptr.end = word

def find_substring(s, words):
    pass