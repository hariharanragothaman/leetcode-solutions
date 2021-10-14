from typing import *

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        ctr = Counter(nums)
        for number in ctr:
            if k > 0 and number + k in ctr:
                count += 1
            if k == 0 and ctr[number] > 1:
                count += 1
        return count