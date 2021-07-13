from typing import *

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(0, n-2):
            t = s[i:i+3]
            ctr = Counter(t)
            v = list(ctr.values())
            if len(v) == 3:
                cnt += 1
        return cnt