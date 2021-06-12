from typing import List
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        full = set(range(left, right+1))
        s = set()
        for a, b in ranges:
            for i in range(a, b+1):
                s.add(i)
        tmp = [c for c in full if c not in s]
        if not tmp:
            return True
        else:
            return False