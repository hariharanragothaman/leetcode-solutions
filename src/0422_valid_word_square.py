
from typing import List

def get_columns(mat):
    return zip(*mat)

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        mx_length = 0
        for c in words:
            mx_length = max(mx_length, len(c))

        for i in range(len(words)):
            if len(words[i]) != mx_length:
                words[i] = words[i] + 'x' * (mx_length - len(words[i]))
        print(words)

        word_cols = []
        for c in get_columns(words):
            word_cols.append(''.join(k for k in c))
        print(word_cols)

        if words == word_cols:
            return True
        else:
            return False