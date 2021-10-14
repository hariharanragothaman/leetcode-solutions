import itertools


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        for _, v in itertools.groupby(s):
            groups.append(len(list(v)))

        ans = 0
        for a, b in zip(groups, groups[1:]):
            ans += min(a, b)
        return ans