from typing import *

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i, c in enumerate(nums):
            ls = sum(nums[:i])
            rs = sum(nums[i+1:])
            if ls == rs:
                return i
        return -1