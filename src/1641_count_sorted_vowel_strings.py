from itertools import accumulate

class Solution:
    def countVowelStrings(self, n: int) -> int:
        initial = [1, 1, 1, 1, 1]
        for i in range(n):
            initial = list(accumulate(initial))
            print(initial)
        return initial[-1]

if __name__ == '__main__':
    s = Solution()
    s.countVowelStrings(1)