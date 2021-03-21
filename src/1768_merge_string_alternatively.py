import itertools

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        for c in itertools.zip_longest(word1, word2, fillvalue=''):
            res = res + ''.join(c)
        return res