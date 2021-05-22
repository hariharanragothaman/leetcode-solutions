class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        result = [0] * len(arr)

        for i, c in enumerate(arr):
            idx = int(c[-1]) - 1
            val = c[:-1]
            result[idx] = val
        return ' '.join(result)