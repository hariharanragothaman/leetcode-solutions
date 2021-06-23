from typing import *


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        n = len(chalk)
        q = k // s
        r = k % s

        tmp = 0
        for i in range(n):
            tmp += chalk[i]
            if tmp > r:
                break
        return i
