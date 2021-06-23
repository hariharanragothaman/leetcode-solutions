import re


class Solution:
    def numDifferentIntegers(self, s: str) -> int:
        _filtered = re.split("[a-zA-Z]+", s)
        return len(set(_filtered))


if __name__ == "__main__":
    s = Solution()
    word = input()
    s.numDifferentIntegers(word)
